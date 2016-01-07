from os import listdir
from os.path import isfile, join
from os import walk
from os import rename
from os import remove

# Scrubs the delim from the target file at direct
def scrub(direct):
	newf = direct[0:-4] + "1" + direct[-4:]

	lines = []
	with open(direct, 'r') as input:
		lines = input.readlines()

	printed = False

	with open(newf, "w") as output:
		for l in lines:
			name = ""
			if l.find("-") > 0:
				pos = l.find("-")
				name = l[:pos]
				if printed == True:
					output.write("}\n")
				output.write("public class " + name + "\n{\n")
			elif l == "Name	Data Type	Description\n":
				pass
			else:
				words = l.split("	")
				obj = words[1]
				if obj == "boolean":
					obj = "bool"
				elif "Map" in obj:
					obj = obj.replace("Map", "Dictionary")
				elif "Set" in obj:
					obj = obj.replace("Set", "HashSet")
				obj = obj.replace("[", "<")
				obj = obj.replace("]", ">")
				towrite = "	public " + obj + " " + words[0] + " { get; set; }\n"
				output.write(towrite)
				printed = True
		output.write("}")

def main():
	path = "C:\\Users\\tomto\\Documents\\lolapidoc.txt"
	scrub(path) 


if __name__ == "__main__":
	main()