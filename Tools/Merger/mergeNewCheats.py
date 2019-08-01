import os
import io
import re
import shutil

def copyCheat(src, dest):
    try:
        os.makedirs(os.path.dirname(dest))
    except:
        return

    shutil.copyfile(src, dest)

def mergeCheat(src, dest):
    newCheats = {}
    currCheats = {}
    mergedCheats = {}

    with open(src, "r", encoding="utf8") as newCheatFile:
        currCheatName = ""
        for line in newCheatFile:
            if re.match("\[.+\]", line) or re.match("{.+}", line):
                currCheatName = line.strip()
                newCheats[currCheatName.strip()] = []
            elif currCheatName != "" and re.match("([0-9A-Za-z]{8} *)+", line):
                newCheats[currCheatName.strip()].append(line.strip())

    with open(dest, "r", encoding="utf8") as currCheatFile:
        currCheatName = ""
        for line in currCheatFile:
            if re.match("\[.+\]", line) or re.match("{.+}", line):
                currCheatName = line.strip()
                currCheats[currCheatName] = []
            elif currCheatName != "" and re.match("([0-9A-Za-z]{8} *)+", line):
                currCheats[currCheatName].append(line.strip())

    for newCheatName, newCheatCodes in newCheats.items():
        foundDuplicateCheat = False
        foundDuplicateName = False

        duplicateCheatName = ""
        duplicateCheatCodes = []

        for currCheatName, currCheatCodes in currCheats.items():
            duplicateCheatName = currCheatName.strip()
            duplicateCheatCodes = [code.strip() for code in currCheatCodes]

            if newCheatName.strip() == currCheatName.strip():
                foundDuplicateName = True

            if len(newCheats[newCheatName]) == len(currCheats[currCheatName]):
                for i in range(0, len(newCheats[newCheatName])):
                    if newCheats[newCheatName][i].strip() != currCheats[currCheatName][i].strip():
                        foundDuplicateCheat = True
        
        # Two different cheats with the same name
        if foundDuplicateName and not foundDuplicateCheat:
            decision = askUser(duplicateCheatName, duplicateCheatCodes, newCheatName, newCheatCodes, True, False)

            if decision == 1:
                mergedCheats[duplicateCheatName] = duplicateCheatCodes
            elif decision == 2:
                mergedCheats[duplicateCheatName] = newCheatCodes
            elif decision == 3:
                while True:
                    currCheatNameNew = input(f"Enter a new name for the current cheat ({duplicateCheatName}):")
                    newCheatNameNew = input(f"Enter a new name for the new cheat ({newCheatName}):")

                    if currCheatNameNew != newCheatNameNew:
                        break
                    else:
                        print("Cheat names can't be the same!")

                mergedCheats[currCheatNameNew] = currCheatCodes
                mergedCheats[newCheatNameNew] = newCheatCodes
        
        # Two cheats with different names but the same set of cheat codes
        elif not foundDuplicateName and foundDuplicateCheat:
            decision = askUser(duplicateCheatName, duplicateCheatCodes, newCheatName, newCheatCodes, False, True)

            if decision == 1:
                mergedCheats[duplicateCheatName] = duplicateCheatCodes
            elif decision == 2:
                mergedCheats[duplicateCheatName] = duplicateCheatCodes

        # Two identical cheats
        elif foundDuplicateName and foundDuplicateCheat:
            mergedCheats[duplicateCheatName] = duplicateCheatCodes
        
        # New cheat was found
        elif not foundDuplicateName and not foundDuplicateCheat:
            mergedCheats[newCheatName] = newCheatCodes

def askUser(cheatNameCurr, cheatCodesCurr, cheatNameNew, cheatCodesNew, duplicateName, duplicateCodes):
    if not duplicateName and duplicateCodes:
        while True:
            print("Identical cheats with two different names were found.")
            print(f"Current Name: {cheatNameCurr}")
            print(f"New Name:     {cheatNameNew}")
            
            selection = input("Keep first or second one? [1, 2]")

            if selection == "1":
                return 1
            elif selection == "2":
                return 2
            else:
                pass # Ask again if input wasn't 1 or 2

    elif duplicateName and not duplicateCodes:
        while True:
            print("Two cheats with the same name but different codes were found.")
            print(f"Cheat name: {cheatNameCurr}")
            print(f"Current Codes:")
            for code in cheatCodesCurr:
                print(f"     {code}")
            print(f"New Codes:")
            for code in cheatCodesNew:
                print(f"     {code}")
            
            selection = input("Keep first or second one or keep both (3)? [1, 2, 3]")

            if selection == "1":
                return 1
            elif selection == "2":
                return 2
            elif selection == "3":
                return 3
            else:
                pass # Ask again if input wasn't 1, 2 or 3
    else:
        print("SHOULD NOT BE REACHED EVER!")
    

currCheatsPath = "./../../Cheats"
newCheatsPath = "./new_cheats"

currCheatsDir = os.listdir(currCheatsPath)
newCheatsDir = os.listdir(newCheatsPath)

for dir in newCheatsDir:
    cheats = os.listdir(f"{newCheatsPath}/{dir}/cheats")
    for cheat in cheats:
        print(f"/Cheats/{dir}/cheats/{cheat}")

        if not os.path.exists(f"{currCheatsPath}/{dir}/cheats/{cheat}"):
            copyCheat(f"{newCheatsPath}/{dir}/cheats/{cheat}", f"{currCheatsPath}/{dir}/cheats/{cheat}")
        else:
            mergeCheat(f"{newCheatsPath}/{dir}/cheats/{cheat}", f"{currCheatsPath}/{dir}/cheats/{cheat}")
