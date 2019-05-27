#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Imports
import unicodedata as ud
import urllib.request
import os
import re
from bs4 import BeautifulSoup

# Variables
pathToCheats = 'https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/tree/master/Cheats/'
pathToReadme = 'https://raw.githubusercontent.com/WerWolv/EdiZon_CheatsConfigsAndScripts/master/Cheats/README.md'
savePathReadme = './Cheats/README.md' # Where to save the new Readme file

# Methods
latin_letters= {}
def is_latin(uchr):
    try: return latin_letters[uchr]
    except KeyError:
        return latin_letters.setdefault(uchr, 'LATIN' in ud.name(uchr))

def only_roman_chars(unistr):
    return all(is_latin(uchr)
               for uchr in unistr
               if uchr.isalpha()) # isalpha suggested by John Machin

def fixReadme():
    # Creating required databases from:
    #  - https://switchbrew.org/wiki/Title_list/Games
    #  - http://nswdb.com/xml.php
    #  - https://raw.githubusercontent.com/WerWolv/EdiZon_CheatsConfigsAndScripts/master/Cheats/README.md
    combinedDB = {}
    # SwitchBrew Database
    with urllib.request.urlopen("https://switchbrew.org/wiki/Title_list/Games") as fp:
        soup = BeautifulSoup(fp, "html.parser")
    listSwitchbrewGameList = []
    tables = soup.find_all('table',attrs={"class":"wikitable sortable"})
    for table in tables:
        table_body = table.find('tbody')
        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            listSwitchbrewGameList.append([ele for ele in cols])
    switchBrewDB = {}
    for entry in listSwitchbrewGameList:
        if len(entry)!= 0:
            switchBrewDB[entry[0]] = {'TitleID' : entry[0],'Description' : entry[1],'Region': entry[2], 'Origin' : 'SwitchBrew'}
            combinedDB[entry[0]] = switchBrewDB[entry[0]]
    
    # NSWDB Database
    with urllib.request.urlopen('http://nswdb.com/xml.php')as fp:
        soup = BeautifulSoup(fp, "html.parser")
        nswDB = {}
        for releases in soup.find_all('releases'):
            for release in releases.find_all('release'):
                titleID = release.find('titleid').text.strip()
                titleName = release.find('name').text.strip()
                titleRegion = release.find('region').text.strip()
                nswDB[titleID] = {'TitleID':titleID,'Description':titleName, 'Region': titleRegion, 'Origin':'NSWDB'}
                if not combinedDB.keys().__contains__(titleID):
                    combinedDB[titleID] = nswDB[titleID]
                elif switchBrewDB.keys().__contains__(titleID) and not only_roman_chars(switchBrewDB[titleID]['Description']):
                    combinedDB[titleID] = nswDB[titleID]
    
    # Old Readme Database
    readme = urllib.request.urlopen(pathToReadme)
    readmeText = readme.read().decode().replace('|Name|TitleID|Region','').replace('|--|--|--','')
    oldReadmeDatabase = re.findall(r'\|(.*)\|(.*)\|(.*)', readmeText)
    for entry in oldReadmeDatabase:
        titleID = re.match('\[(.*)\]', entry[1]).group(1)
        # Determinate whether the title is missing in the combined database
        if combinedDB.keys().__contains__(titleID):
            if not only_roman_chars(combinedDB[titleID]['Description']):
                combinedDB[titleID] = {'TitleID' : titleID,'Description' : entry[0],'Region': entry[2], 'Origin': 'Readme'}
        else:
            combinedDB[titleID] = {'TitleID' : titleID,'Description' : entry[0],'Region': entry[2], 'Origin': 'Readme'}
    
    # EdiZon Cheat Folder Database
    with urllib.request.urlopen(pathToCheats) as cheatDir:
        soup = BeautifulSoup(cheatDir, "html.parser")
    cheatDirFolders = []
    tables = soup.find_all('table',attrs={"class":"files"})
    for table in tables:
        table_body = table.find('tbody')
        rows = table_body.find_all('tr',attrs={"class":"js-navigation-item"})
        for row in rows:
            cols = row.find_all('td',attrs={"class":"content"})
            for ele in cols:
                if '/cheats' in ele.text.strip():
                    cheatDirFolders.append(ele.text.strip().replace('/cheats',''))
    
    # Creating new Readme Database
    newReadmeDatabase = {}
    for dir in cheatDirFolders:
        if combinedDB.keys().__contains__(dir):
            dataGame = combinedDB[dir]
            gameName = dataGame['Description']
            # Check if title name is in roman letters
            if not only_roman_chars(gameName):
                # Get english name
                if nswDB.keys().__contains__(dir):
                    gameName = (nswDB[dir]['Description'])
            titleID = ('[%s](%s/cheats)'% (dir,dir))
            if dataGame['Origin'] == 'Readme' and len(dataGame['Region'].split())==1:
                newReadmeDatabase[gameName] = {'Title':gameName,'TitleID':titleID, 'Region':dataGame['Region']}
            elif dataGame['Origin'] == 'NSWDB':
                region = '![%s](http://nswdb.com/images/%s.jpg)' % (dataGame['Region'],dataGame['Region'])
                newReadmeDatabase[dir] = {'Title':gameName,'TitleID':titleID, 'Region':region}
            else:
                region = '![WLD](http://nswdb.com/images/WLD.jpg)'
                newReadmeDatabase[dir] = {'Title':gameName,'TitleID':titleID, 'Region':region}
    
    # Creating Readme String
    readmeString = "# Atmosphère Cheats \n\n"
    currentLetter = ''
    for gameTitle in sorted(newReadmeDatabase.keys(),key=lambda x: newReadmeDatabase[x]['Title']):
        # Update Letter and create new table
        if newReadmeDatabase[gameTitle]['Title'][0] != currentLetter:
            currentLetter = newReadmeDatabase[gameTitle]['Title'][0]
            readmeString += '### %s \n' % (currentLetter)
            readmeString += '|Name|TitleID|Region\n'
            readmeString += '|--|--|--\n'
        readmeString += '|%s|%s|%s\n' % (newReadmeDatabase[gameTitle]['Title'],newReadmeDatabase[gameTitle]['TitleID'],newReadmeDatabase[gameTitle]['Region'])
    
    
    # Open Readme.md
    f = open(savePathReadme,'w+', encoding='utf-8')
    f.write(readmeString)
    f.close()
    
    print('#---------------------------------------------------------------------------#')
    print('Size SwitchBrew DB: %s' % (len(switchBrewDB.keys())))
    print('Size NSWDB: %s' % (len(nswDB.keys())))
    print('Size OldReadmeDB: %s' % (len(oldReadmeDatabase)))
    print('Size CheatDirDB: %s' % (len(cheatDirFolders)))
    print('Size combinedDB: %s' % (len(combinedDB.keys())))
    print('Size NewReadme DB: %s' % (len(newReadmeDatabase.keys())))
    for i in cheatDirFolders:
        if not combinedDB.keys().__contains__(i):
            print('Missing Entry for: ' + i)
    print('#---------------------------------------------------------------------------#')