import os

listOfCorruptedFiles = []

def CheckForCorruptedFiles(currentDirectory):
 
    for element in os.listdir(currentDirectory):

        potentialPath = currentDirectory + "\\" + element

        if os.path.isdir(potentialPath):
            CheckForCorruptedFiles(potentialPath)
            
        elif element.endswith(".uasset"):
            if(os.stat(potentialPath).st_size <= 1024):
                listOfCorruptedFiles.append(potentialPath)
        
            
            

print("This python script will scan the current working directory and all sub directories to search for uasset files with a small enough size to be considered corrupted. It will then print the directory and name of that file so you can deal with it accordingly.")

print("\n")

os.chdir("..")
searchInDirectory = os.getcwd()

print("Search directory :", searchInDirectory, "\n")

CheckForCorruptedFiles(searchInDirectory)

if len(listOfCorruptedFiles) > 0:
        print("Some files were found to be corrupted!. See below:")

        for element in listOfCorruptedFiles:
            print("\t" + element)
else:
    print("No corrupted files were found, and the Git LFS Overlords are sad!\n")

print("\n")
