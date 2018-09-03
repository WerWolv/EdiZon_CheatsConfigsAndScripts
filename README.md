# EdiZon Configs and Scripts

This is the official repository for EdiZon Editor Config and Editor Script files. They can be used by the [EdiZon save Editor
](https://github.com/thomasnet-mc/EdiZon) to modify every Nintendo Switch save file.
If you want yours to be added, please send them to @WerWolv98 or @thomasnet-mc or create a Pull Request.

Config files go into the `/EdiZon/editor` folder, Script files go into the `/EdiZon/editor/scripts` folder and libraries used by scripts go into the `/EdiZon/editor/scripts/lib` folder.

Before submitting a config file, please make sure it works correctly and run it through this site: https://jsonformatter.curiousconcept.com/ It will show you any syntax errors and formats the file nicely.

Before submitting a script file, please vetify that it works with EdiZon. Change some values, check in the game if they have changed. Create a backup before and after modification and compare them.

## Editor Config files

| Game                            | Requirements            | Author    |
| ------------------------------- |:-----------------------:| ---------:|
| [Super Mario Odyssey](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/0100000000010000.json)             | bin.lua                 | WerWolv  |
| [Hollow Knight](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/0100633007D48000.json)                   | json.lua & lib/json.lua | WerWolv  |
| [Octopath Traveler](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/0100E66006406000.json) | octp.lua      | shahmirn and SleepyPrince |
| [BOTW](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/01007EF00011E000.json)    | bin.lua | borntohonk |
| [Hyrule Warriors: Definitive Edition](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/0100AE00096EA000.json) | bin.lua | borntohonk and loganavatar |
| [Bayonetta 1](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/010076F0049A2000.json) | bin.lua | madhatter |
| [Bayonetta 2](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/01007960049A0000.json) | bin.lua | madhatter |
| [Mario Tennis Aces](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/0100BDE00862A000.json) | bin.lua | cubex |
| [I am Setsuna](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/0100849000BDA000.json) | setsuna.lua & lib/md5.lua | JojoTheGoat |
| [Puyo Puyo Tetris](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/010053D0001BE000.json) | puyopuyo.lua & lib/checksum.lua | JojoTheGoat |
| [Super Bomberman R](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/01007AD00013E000.json) | bin.lua | JojoTheGoat |


## Editor Script files
| Script                            | Requirements            | Author    |
| --------------------------------- |:-----------------------:| ---------:|
| [Binary](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Scripts/bin.lua) | None                 | WerWolv  |
| [JSON](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Scripts/json.lua) | [lib/json.lua](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Scripts/lib/json.lua) | WerWolv  |
| [Octopath Traveler (UE4 GVAS)](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Scripts/octp.lua) | None | shahmirn and SleepyPrince |
| [I am Setsuna](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Scripts/setsuna.lua) | [lib/md5.lua](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Scripts/lib/md5.lua) | JojoTheGoat |
| [Puyo Puyo Tetris](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Scripts/puyopuyo.lua) | [lib/checksum.lua](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Scripts/lib/checksum.lua) | JojoTheGoat |


## Pending Editor Config files
| Game                            | Requirements            | Author    |
| ------------------------------- |:-----------------------:| ---------:|
| [Xenoblade Chronicles 2](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Pending/Configs/0100E95004038000.json)             | bin.lua                 | madhatter  |
| [Adventure Time](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Pending/Configs/0100C4E004406000.json)             | json.lua & lib/json.lua         | madhatter  |
| [Fire Emblem Warriors](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Pending/Configs/0100F15003E64000.json)             | bin.lua         | CrisFTW & Brawl345  |
| [I am Setsuna](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Pending/Configs/0100849000BDA000.json) | setsuna.lua & lib/md5.lua | mrLewisFC |
| [Lost Sphear](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Pending/Configs/010077B0038B2000.json) | lostsphear.lua & lib/md5.lua | mrLewisFC |
| [Party Planet](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Pending/Configs/01004F10066B0000.json)             | bin.lua         | trueicecold  |
| [Golf Story](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Pending/Configs/0100779004172000.json)             | bin.lua         | trueicecold  |

## Pending Editor Script files

| Game                            | Requirements            | Author    |
| ------------------------------- |:-----------------------:| ---------:|
| [Lost Sphear](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Pending/Scripts/lostsphear.lua) | [lib/md5.lua](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Scripts/lib/md5.lua) | mrLewisFC |
