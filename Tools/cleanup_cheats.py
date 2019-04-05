#!/usr/bin/env python3

"""cleanup_cheats.py by TehPsychedelic: Data cleansing to make cheat files compatible with atmosphère."""

import os
import re

baseFolder = '../Cheats'
fileExt = '.txt'
backupExt = '.bak'
maxSize =  64
patternCredits = re.compile(r'\[From (.*) by (.*) for (.*)\]$')
patternCheatNamea = re.compile(r'\[(.*)\]$')
patternCheatNameb = re.compile(r'([ ]*)\[(.*)\]([ ]*)$')
patternCheat1a = re.compile(r'([a-zA-Z0-9]{8})+([ ]{1}[a-zA-Z0-9]{8})*$') # Does not check max 3 (eg. 4 blocks is ok).
patternCheat1b = re.compile(r'(\s)*(\s*[a-zA-Z0-9]{8}\s*)+(\s+[a-zA-Z0-9]{8}\s*)*(\s)*$') # Does not check max 3 (eg. 4 blocks is ok). This version takes care of multiple spaces and/or trailing tabs.
patternCheat2 = re.compile(r'\[HEAP\+[a-zA-Z0-9]+\] ;\([a-zA-Z0-9]+\)$')
patternEmptyLinea = re.compile(r'$')
patternEmptyLineb = re.compile(r'[ ]+$')

def processLine(line):
    if patternCredits.match(line):
        return '[Credits ' + patternCredits.match(line).group(2) + ']\n' # Does not check if author length is 50ish characters or so.
    elif patternCheatNamea.match(line) and len(line) > maxSize:
        return line[:maxSize] # Does not check if last character is newline in which case needs to cut before closing ] then append ']\n'. Does not check if it cuts midway and needs to append ']\n'. Does not check if it's actually a cheat name (next line = cheat code).
    elif patternCheatNamea.match(line) and len(line) <= maxSize:
        return line
    elif patternCheatNameb.match(line) and len(line) > maxSize:
        return line.strip()[:maxSize] + '\n' # Does not check if last character is newline in which case needs to cut before closing ] then append ']\n'. Does not check if it cuts midway and needs to append ']\n'. Does not check if it's actually a cheat name (next line = cheat code).
    elif patternCheatNameb.match(line) and len(line) <= maxSize:
        return line.strip() + '\n'
    elif patternCheat1a.match(line):
        return line
    elif patternCheat1b.match(line):
        return re.sub('\s+', ' ', line).strip() + '\n'
    elif patternCheat2.match(line):
        return line
    elif patternEmptyLinea.match(line):
        return line # Respect empty line
    elif patternEmptyLineb.match(line):
        return '\n' # Respect empty line
    else:
        return ''

def processFile(filePath):
    print('Processing: ' + filePath)

    modifiedFlag = False
    oldFile = open(filePath,'r')
    newFile = open(filePath + backupExt, 'w')

    for line in oldFile:
        newLine = processLine(line)
        if newLine != line:
            modifiedFlag = True
        newFile.write(newLine)

    oldFile.close()
    newFile.close()

    if modifiedFlag:
        os.remove(filePath)
        os.rename(filePath + backupExt, filePath)
        print('\tModified!')
    else:
        os.remove(filePath + backupExt)

    fileName, fileExt = os.path.splitext(os.path.basename(filePath))
    if not fileName.islower():
        os.rename(filePath, filePath.replace(fileName, fileName.lower()))
        print('\tRenamed!')

def main():
    for root, dirs, files in os.walk(baseFolder):
        for file in files:
            if file.endswith(fileExt):
                 processFile(os.path.join(root, file))

if __name__ == "__main__":
    main()
