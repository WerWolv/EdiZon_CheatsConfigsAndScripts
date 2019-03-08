# EdiZon Configs and Scripts & Atmosphère Cheats

This is the official repository for EdiZon Editor Config, Editor Script files and Atmosphère Cheats. The configs and scripts can be used by the [EdiZon save Editor
](https://github.com/WerWolv/EdiZon) to modify every Nintendo Switch save file. 
The Atmosphère cheat files get loaded by Atmosphère's `dmnt:cht` cheat module.

If you want yours to be added, please send them to @WerWolv#1337 on Discord or create a Pull Request.

Config files go into the `/EdiZon/editor` folder, Script files go into the `/EdiZon/editor/scripts` folder, libraries used by scripts go into the `/EdiZon/editor/scripts/lib` folder and cheats go into the respective `/atmosphere/titles/<titleID>/cheats` folders.
Before submitting a config file, please make sure it works correctly and run it through the test suite with `npm test`. The test suite requires a [Node.js](https://nodejs.org/) environment can be installed via `npm install`.


## Save file analyzing
You can use the [save_util.py Python script](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Tools/save_util.py) to analyze your save file. It supports following options:
```python
options = {
    'zlib_compress' : { 'function' : zlib_compress, 'description' : 'Compresses file with zlib. Args: < FilePath, [CompressionLevel], [StartAddress], [EndAddress] >' },
    'zlib_decompress' : { 'function' : zlib_decompress, 'description' : 'Decompresses zlib compressed file. Args: < FilePath, [StartAddress], [EndAddress] >' },
    'crc32' : { 'function' : crc32, 'description' : 'Calculates the CRC32 checksum of a file. Args: < FilePath, [StartAddress], [EndAddress] >' },
    'md5' : { 'function' : md5, 'description' : 'Calculates the MD5 Hash of a file. Args: < FilePath, [StartAddress], [EndAddress] >' }
}
```
Feel free to add more common functions and PR them!

If you want to read up on how the save files of some games are structured, check out the [Save research](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/tree/master/Save%20research) folder. 
You can PR your own research there if you have some but don't want to build a config/script yourself.

## Editor Config files [![Build Status](https://travis-ci.com/WerWolv/EdiZon_CheatsConfigsAndScripts.svg?branch=master)](https://travis-ci.com/WerWolv/EdiZon_CheatsConfigsAndScripts)

| Game                            | Requirements            | Author    | Beta     |
|:-------------------------------:|:-----------------------:|:---------:|:--------:|
| [Super Mario Odyssey](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Configs/0100000000010000.json)             | smo.py, lib/byml.py & lib/python3.5/sortedcontainers/| Ac_K & WerWolv  | No |
| [Hollow Knight](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Configs/0100633007D48000.json)                   | json.lua & lib/json.lua | WerWolv  | No |
| [Octopath Traveler](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Configs/0100E66006406000.json) | octp.lua      | shahmirn, SleepyPrince & @x43x61x69 | No |
| [BOTW](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Configs/01007EF00011E000.json)    | bin.lua | borntohonk & macia10 | No |
| [Hyrule Warriors: Definitive Edition](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Configs/0100AE00096EA000.json) | bin.lua | borntohonk and loganavatar | No |
| [Bayonetta 1](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Configs/010076F0049A2000.json) | bin.lua | madhatter | No |
| [Bayonetta 2](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Configs/01007960049A0000.json) | bin.lua | madhatter | No |
| [Mario Tennis Aces](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Configs/0100BDE00862A000.json) | bin.lua | cubex | No |
| [I am Setsuna](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Configs/0100849000BDA000.json) | setsuna.lua & lib/md5.lua | Jojo & mrLewisFC | Yes |
| [Puyo Puyo Tetris](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Configs/010053D0001BE000.json) | puyopuyo.lua & lib/checksum.lua | Jojo | No |
| [Super Bomberman R](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Configs/01007AD00013E000.json) | bin.lua | Jojo | No |
| [Adventure Time](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Configs/0100C4E004406000.json)             | json.lua & lib/json.lua         | madhatter  | No |
| [Fire Emblem Warriors](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Configs/0100F15003E64000.json)             | bin.lua         | CrisFTW & Brawl345  | No |
| [Lost Sphear](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Configs/010077B0038B2000.json) | lostsphear.lua & lib/md5.lua | mrLewisFC | Yes |
| [Party Planet](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Configs/01004F10066B0000.json)             | bin.lua         | trueicecold  | Yes |
| [Golf Story](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Configs/0100779004172000.json)             | bin.lua         | trueicecold  | No |
| [God Wars](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Configs/0100F3D00B032000.json)             | bin.lua         | mrLewisFC | Yes |
| [The Lost Child](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Configs/01008A000A404000.json)             | bin.lua         | mrLewisFC | Yes |
| [Mega Man 11](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Configs/0100B0C0086B0000.json)             | bin.lua         | jonyluke | Yes |
| [Yooka Laylee](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Configs/0100F110029C8000.json)             | json.lua         | WerWolv | No |010036B0034E4000
| [Super Mario Party](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Configs/010036B0034E4000.json)             | bin.lua         | WerWolv | No |
| [Disgaea 1: Complete](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Configs/01004B100AF18000.json)             | bin.lua         | findonovan95 | Yes |
| [Dark Souls Remastered](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Configs/01004AB00A260000.json)             | darksouls.lua         | Jojo | Yes |
| [Super Smash Bros. Ultimate](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Configs/01006A800016E000.json)             | smash.lua         | mrLewisFC | Yes |
| [Donkey Kong: Tropical Freeze](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Configs/0100C1F0051B6000.json)           | dktf.lua          | kindofblues | Yes |
| [New Super Mario Bros. U Deluxe](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Configs/0100EA80032EA000.json)           | nsmbud.lua          | DNA | No |
| [Stardew Valley](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Configs/0100E65002BB8000.json)           | xml.py          | echo000 & WerWolv | Yes |
| [Xenoblade Chronicles 2](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Configs/0100E95004038000.json)           | bin.lua          | madhatter & macia10 | Yes |
| [Xenoblade Chronicles 2 Torna Golden Country Stand Alone](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Configs/0100C9F009F7A000.json)           | torna.py          | macia10 | Yes |
| [Celeste](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Configs/01002B30028F6000.json)           | xml.py          | WerWolv | Yes |
| [Mario Kart 8](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Configs/0100152000022000.json)           | mk8.py          | Ac_K | No |
| [Kirby Star Allies](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Configs/01007E3006DDA000.json)           | kirbysa.py          | Ac_K | No |

## Editor Script files
| Script                            | Requirements            | Author    | Beta   |
|:---------------------------------:|:-----------------------:|:---------:|:------:|
| [Binary (Lua)](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Scripts/bin.lua) | None                 | WerWolv  | No |
| [Binary (Python)](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Scripts/bin.py) | None  | WerWolv | Yes |
| [JSON](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Scripts/json.lua) | [lib/json.lua](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Scripts/lib/json.lua) | WerWolv  | No |
| [XML](https://github.com/WerWolv/EdiZon_ConfigsAndScripts/blob/master/Scripts/xmls.py) | [lib/python3.5/xmltodict.py](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Scripts/lib/python3.5/xmltodict.py)  | WerWolv | Yes |
| [Octopath Traveler (UE4 GVAS)](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Scripts/octp.lua) | None | shahmirn and SleepyPrince | No |
| [I am Setsuna](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Scripts/setsuna.lua) | [lib/md5.lua](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Scripts/lib/md5.lua) | Jojo | No |
| [Puyo Puyo Tetris](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Scripts/puyopuyo.lua) | [lib/checksum.lua](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Scripts/lib/checksum.lua) | Jojo | No |
| [Lost Sphear](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Scripts/lostsphear.lua) | [lib/md5.lua](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Scripts/lib/md5.lua) | mrLewisFC | Yes |
| [Dark Souls Remastered](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Scripts/darksouls.lua) | [lib/md5.lua](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Scripts/lib/md5.lua) | Jojo | Yes |
| [Super Smash Bros. Ultimate](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Scripts/smash.lua) | None | mrLewisFC | Yes |
| [Donkey Kong: Tropical Freeze](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Scripts/dktf.lua) | [lib/checksum.lua](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Scripts/lib/checksum.lua)  | kindofblues | Yes |
| [New Super Mario Bros. U Deluxe](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Scripts/nsmbud.lua) | [lib/checksum.lua](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Scripts/lib/checksum.lua)  | DNA | Yes |
| [Torna](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Scripts/torna.py) | None  | macia10 | Yes |
| [Mario Kart 8](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Scripts/mk8.py) | None  | Ac_K | No |
| [Kirby Star Allies](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Scripts/kirbysa.py) | None  | Ac_K | No |
| [Super Mario Odyssey](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Scripts/smo.py) | [lib/byml.py](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Scripts/lib/byml.py) & lib/python3.5/sortedcontainers/  | Ac_K & WerWolv | No |

## Atmosphère Cheats

A list of all available cheats can be found [here](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Cheats/README.md).

