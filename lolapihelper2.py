from os import listdir
from os.path import isfile, join
from os import walk
from os import rename
from os import remove

def scrub(direct):
	newf = direct[0:-4] + "2" + direct[-4:]

	lines = []
	with open(direct, 'r') as input:
		lines = input.readlines()

	variables = []
	with open(newf, "w") as output:
		for line in lines:
			line = line.strip()

			if "class" in line:
				t = line.split(" ")[2].strip()
				output.write(line.strip() + " : IEquatable<" + t + ">\n{\n")
				continue
			elif line.strip() == "}":
				output.write("\n	public bool Equals(")
				output.write(t + " other)\n	{\n")
				output.write("		if (")
				for var in variables:
					if variables[variables.index(var)] == variables[0]:
						output.write("this." + var + " == other." + var)
					else:
						output.write("		this." + var + " == other." + var)

					if variables.index(var) == len(variables)-1:
						output.write(")\n")
						output.write("			return true;\n")
						output.write("		return false;\n")
					else:
						output.write(" &&\n")

				output.write("	}\n")
				output.write("}\n")
				variables = []
				continue
			elif line.strip() == "{":
				continue
			elif line.strip() == "":
				output.write("\n")
				continue
			elif "#" in line or "//" in line:
				output.write(line + "\n")
				continue
			else:
				output.write("	" + line + "\n")
				if "Dictionary" in line:
					variables.append( str(line.strip().split(" ")[3]) )
				else:
					variables.append( str(line.strip().split(" ")[2]) )
				continue

		# output.write("}")

def main():
	path = "C:\\Users\\tomto\\Documents\\lolapidoc1.txt"
	scrub(path) 


if __name__ == "__main__":
	main()