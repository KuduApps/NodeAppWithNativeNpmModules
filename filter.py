import os

# http://stackoverflow.com/a/1724723/3234163
def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result

def filter_lines(line):
    if "'DebugInformationFormat': 3," in line:
        return line.replace("3", "0")
    else:
        return line

lines = []
files = find_all("common.gypi", "D:\\local\\UserProfile")

for file in files:
    with open(file) as in_file:
        lines = in_file.readlines()
        lines = [filter_lines(l) for l in lines]

    with open(file, "w") as out_file:
        out_file.writelines(lines)