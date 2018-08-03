# EdiZon Configs and Scripts

This is the official repository for EdiZon Editor Config and Editor Script files. They can be used by the [EdiZon save Editor
](https://github.com/thomasnet-mc/EdiZon) to modify every Nintendo Switch save file.
If you want yours to be added, please send them to @WerWolv98 or @thomasnet-mc or create a Pull Request.

Config files go into the `/EdiZon/editor` folder, Script files go into the `/EdiZon/editor/scripts` folder and libraries used by scripts go into the `/EdiZon/editor/scripts/lib` folder.

Before submitting a config file, please make sure it works correctly and run it through this site: https://jsonformatter.curiousconcept.com/ It will show you any syntax errors and formats the file nicely or you can use the python3 script inside the "Tools"-folder.

Before submitting a script file, please vetify that it works with EdiZon. Change some values, check in the game if they have changed. Create a backup before and after modification and compare them.

## All Editor Config files

| Game                            | Requirements            | Author    |
| ------------------------------- |:-----------------------:| --------:|
| [Super Mario Odyssey](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/0100000000010000.json)             | bin.lua                 | WerWolv  |
| [Hollow Knight](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/0100633007D48000.json)                   | json.lua & lib/json.lua | WerWolv  |
| [Octopath Traveler Prologue Demo](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/010096000B3EA000.json) | octp.lua                | shahmirn and SleepyPrince |
| [BOTW](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/01007EF00011E000.json)    | bin.lua | borntohonk |
| [Hyrule Warriors: Definitive Edition](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/0100AE00096EA000.json) | bin.lua | borntohonk and loganavatar |
| [Bayonetta 1](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/010076F0049A2000.json) | bin.lua | madhatter |
| [Bayonetta 2](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/01007960049A0000.json) | bin.lua | madhatter |
| [Mario + Rabbids : Kingdom Battle](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/010067300059A000.json) | json.lua | madhatter |
| [Mario Tennis Aces](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/0100BDE00862A000.json) | bin.lua | cubex |
| [I am Setsuna](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/0100849000BDA000.json) | setsuna.lua &  	lib/plc/md5.lua | JojoTheGoat |


## All Editor Script files
| Script                            | Requirements            | Author    |
| ------------------------------- |:-----------------------:| --------:|
| [Binary](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Scripts/bin.lua) | None                 | WerWolv  |
| [JSON](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Scripts/json.lua) | [lib/json.lua](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Scripts/lib/json.lua) | WerWolv  |
| [Octopath Traveler (UE4 GVAS)](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Scripts/octp.lua) | None | shahmirn and SleepyPrince |
| [I am Setsuna](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Scripts/setsuna.lua) | [lib/md5.lua](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Scripts/lib/md5.lua) | JojoTheGoat |
