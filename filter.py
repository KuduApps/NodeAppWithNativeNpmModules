import os

# http://stackoverflow.com/a/1724723/3234163
def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))
    return result

lines = []
files = find_all("common.gypi", "D:\\local\\UserProfile")

for file in files:
	with open(file) as in_file:
		lines = in_file.readlines()
		lines = [line for line in lines if "'/MP', # compile across multiple CPUs" not in line]

	with open(file, "w") as out_file:
		out_file.writelines(lines)