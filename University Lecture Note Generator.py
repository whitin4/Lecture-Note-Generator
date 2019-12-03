from datetime import date
import os

# Populate this with fully-qualified module titles. E.g., "CO310 Introduction to Object Oriented Programming".
# These should always contain a 5 character module code followed by a module title.
modules = []

def getModule():
    mod = input('Enter module (or "NONE"): ')
    if mod.upper() == "NONE":
        return None
    for i in range (len(modules)):
        if modules[i][0:5] == mod:
            return modules[i]        
    return getModule()

# List options
for i in range(len(modules)):
    print(modules[i])
    
requestedModule = getModule()

# Establish today's date in form yyyy-mm-dd
today = date.today().strftime("%Y-%m-%d")

lecTitle = input("Lecture title: ")

filename = ""
subdir = ""
if not requestedModule is None:
    filename += requestedModule[0:5] + " "
    subdir = requestedModule + "/Lecture Notes"
filename += date.today().strftime("%y%m%d")
if lecTitle != "":
    filename += " " + lecTitle
filename += ".md"

filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), subdir, filename)

print("filepath: " + filepath)

myFile = open(filepath, "w")

# Load the template file
templateFile = open("Lecture Note Template.md", "r")
lines = templateFile.readlines()

# Replace placeholder values from the template with correct values
if requestedModule is None:
    requestModule = lecTitle
    
switcher = {
    1: "# " + lecTitle + " #\n",
    9: "*" + today + "*\n",
    11: "**" + requestedModule + "**"
}
    
for i in range (0, len(lines)):
    if switcher.get(i + 1, None) != None:
        lines[i] = switcher.get(i + 1)

myFile.writelines(lines)
myFile.close()

os.startfile(filepath)
