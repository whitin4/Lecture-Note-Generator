from datetime import date
import os

modules = ["CO510 Software Engineering", "CO518 Algorithms, Correctness and Efficiency",
           "CO519 Theory of Computing", "CO527 Operating Systems and Architecture",
           "CO532 Database Systems", "CO539 Web Development", "CO545 Functional Programming"]

def getModule():
    for i in range(len(modules)):
        print(modules[i])
    mod = input('Enter module: CO5')
    for i in range (len(modules)):
        if modules[i][0:5] == "CO5" + mod:
            return modules[i]        
    return getModule()

def validLectureTitle(title):
    validChars = list("-()qwertyuiopasdfghjklzxcvbnm1234567890 ")
    for char in title:
        if char.lower() not in validChars:
            print("Invalid char: " + char)
            return False
    return True

def getLectureTitle():
    lecTitle = input("Lecture title: ")
    while validLectureTitle(lecTitle) == False:
        lecTitle = input("Lecture title: ")
    return lecTitle

def getFileLines(module, title):
    templateFile = open("Lecture Note Template.md", "r")
    lines = templateFile.readlines()

    lines[0] = "# " + title + " #\n"
    lines[8] = "*" + date.today().strftime("%Y-%m-%d") + "*\n"
    lines[10] = "**" + module + "**"
    return lines
    
def createFile(filepath, lines):
    print("filepath: " + filepath)
    myFile = open(filepath, "w")
    myFile.writelines(lines)
    myFile.close()

def getFilename(module, title):
    filename = ""
    if not module is None:
        filename += module[0:5] + " "
    else:
        module = title
    filename += date.today().strftime("%y%m%d")
    if title != "":
        filename += " " + title
    return filename + ".md"

# Get the module

requestedModule = getModule()

# Get the lecture title

lecTitle = getLectureTitle()

# Prepare the filename and filepath

subdir = ""

subdir = requestedModule + "/Lecture Notes"

filename = getFilename(requestedModule, lecTitle)

filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), subdir, filename)

# Prepare the file template

lines = getFileLines(requestedModule, lecTitle)

# Create the file

createFile(filepath, lines)

# Run the file

os.startfile(filepath)
