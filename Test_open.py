from pathlib import Path
import os

lowerexclusions = ["a","and","by","of","or","the","with"]

#dump list of words from file into variable
upperexclusions =  open(Path.cwd() / "exclusions.txt", "r")
upperexclusionslist = upperexclusions.readlines()
upperexclusions.close()

#create new variable, iterate thru list, lowercase
lowerupperexclusionslist = []
for x in upperexclusionslist:
    lowerupperexclusionslist.append(x.lower())

#more succinct version of code above
#lowercaseupperexclusionslist = [x.lower() for x in upperexclusionslist]
#lowercaseupperexclusionslist = map(str.lower, upperexclusionslist)

#add to new variable list

newfile = Path.cwd() / "newwords.txt" #cwd:current working directory
file_handler = open(Path.cwd() / "words.txt", "r")

#add logic to delete file and make new file
if os.path.exists("newwords.txt"):
    os.remove("newwords.txt")
file_handler2 = open(newfile, "x")
lines = file_handler.readlines()
modifiedLines = []

#iterate thru file to check for lower
for line in lines:
    words = line.replace("\n","").split(" ")
    modwords = []
    for word in words:
        #exception list for lowercase
        if (words.index(word) != 0) and (word.lower() in lowerexclusions): #exception list for uppercase  
            modwords.append(word.lower())      
        else:
            modwords.append(word.capitalize()) #add uppercase
    capline = " ".join(modwords) + "\n"    
    modifiedLines.append(capline)
    
file_handler2.writelines(modifiedLines)
file_handler.close()
file_handler2.close()


    # For later
    #   give user option to append to file
    #   add values in multiple columns


