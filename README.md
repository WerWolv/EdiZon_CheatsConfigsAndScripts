# EdiZon Configs and Scripts

This is the official repository for EdiZon Editor Config and Editor Script files. They can be used by the [EdiZon save Editor
](https://github.com/thomasnet-mc/EdiZon) to modify every Nintendo Switch save file.
If you want yours to be added, please send them to @WerWolv98 or create a Pull Request.

Config files go into the `/EdiZon/editor` folder, Script files go into the `/EdiZon/editor/scripts` folder and libraries used by scripts go into the `/EdiZon/editor/scripts/lib` folder.

Before submitting a config file, please make sure it works correctly and run it through the test suite with `npm test`. The test suite requires a [Node.js](https://nodejs.org/) environment can be installed via `npm install`.

Before submitting a script file, please verify that it works with EdiZon. Change some values, check in the game if they have changed. Create a backup before and after modification and compare them.

## Editor Config files

| Game                            | Requirements            | Author    | Beta     |
|:-------------------------------:|:-----------------------:|:---------:|:--------:|
| [Super Mario Odyssey](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/0100000000010000.json)             | bin.lua                 | WerWolv  | No |
| [Hollow Knight](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/0100633007D48000.json)                   | json.lua & lib/json.lua | WerWolv  | No |
| [Octopath Traveler](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/0100E66006406000.json) | octp.lua      | shahmirn, SleepyPrince & @x43x61x69 | No |
| [BOTW](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/01007EF00011E000.json)    | bin.lua | borntohonk & macia10 | Yes |
| [Hyrule Warriors: Definitive Edition](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/0100AE00096EA000.json) | bin.lua | borntohonk and loganavatar | No |
| [Bayonetta 1](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/010076F0049A2000.json) | bin.lua | madhatter | No |
| [Bayonetta 2](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/01007960049A0000.json) | bin.lua | madhatter | No |
| [Mario Tennis Aces](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/0100BDE00862A000.json) | bin.lua | cubex | No |
| [I am Setsuna](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/0100849000BDA000.json) | setsuna.lua & lib/md5.lua | JojoTheGoat & mrLewisFC | Yes |
| [Puyo Puyo Tetris](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/010053D0001BE000.json) | puyopuyo.lua & lib/checksum.lua | JojoTheGoat | No |
| [Super Bomberman R](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/01007AD00013E000.json) | bin.lua | JojoTheGoat | No |
| [Xenoblade Chronicles 2](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/0100E95004038000.json)             | bin.lua                 | madhatter  | Yes |
| [Adventure Time](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/0100C4E004406000.json)             | json.lua & lib/json.lua         | madhatter  | No |
| [Fire Emblem Warriors](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/0100F15003E64000.json)             | bin.lua         | CrisFTW & Brawl345  | No |
| [Lost Sphear](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/010077B0038B2000.json) | lostsphear.lua & lib/md5.lua | mrLewisFC | Yes |
| [Party Planet](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/01004F10066B0000.json)             | bin.lua         | trueicecold  | Yes |
| [Golf Story](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/0100779004172000.json)             | bin.lua         | trueicecold  | Yes |
| [God Wars](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/0100F3D00B032000.json)             | bin.lua         | mrLewisFC | Yes |
| [The Lost Child](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/01008A000A404000.json)             | bin.lua         | mrLewisFC | Yes |
| [Mega Man 11](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/0100B0C0086B0000.json)             | bin.lua         | jonyluke | Yes |
| [Yooka Laylee](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/0100F110029C8000.json)             | json.lua         | WerWolv | Yes |010036B0034E4000
| [Yooka Laylee](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Configs/010036B0034E4000.json)             | bin.lua         | WerWolv | Yes |

## Editor Script files
| Script                            | Requirements            | Author    | Beta   |
|:---------------------------------:|:-----------------------:|:---------:|:------:|
| [Binary](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Scripts/bin.lua) | None                 | WerWolv  | No |
| [JSON](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Scripts/json.lua) | [lib/json.lua](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Scripts/lib/json.lua) | WerWolv  | No |
| [Octopath Traveler (UE4 GVAS)](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Scripts/octp.lua) | None | shahmirn and SleepyPrince | No |
| [I am Setsuna](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Scripts/setsuna.lua) | [lib/md5.lua](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Scripts/lib/md5.lua) | JojoTheGoat | No |
| [Puyo Puyo Tetris](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Scripts/puyopuyo.lua) | [lib/checksum.lua](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Scripts/lib/checksum.lua) | JojoTheGoat | No |
| [Lost Sphear](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Scripts/lostsphear.lua) | [lib/md5.lua](https://github.com/WerWolv98/EdiZon_ConfigsAndScripts/blob/master/Scripts/lib/md5.lua) | mrLewisFC | Yes |
