## Save Struct ##

The save file `savegame` start with 0x03 unknown bytes and then a JSON file.

At the end of the save file is some zero padding.

## Editing ##

It's just a JSON editing.

You need to put the 0x03 unknown bytes back after editing.

The zero padding at the end of the file seems to be required as well, or else the game rejects the save.

That's all.

## Config & Script ##

- Script: [GearClubUnlimited.py](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Scripts/GearClubUnlimited.py)
- Config: [010065E003FD8000.json](https://github.com/WerWolv/EdiZon_CheatsConfigsAndScripts/blob/master/Configs/010065E003FD8000.json)

## TODO ##

Currently support for PLAYER ONE LEVEL and PLAYER ONE CASH is ready, but there are some caveats.

Editing Cash value too high will result in save being rejected (you'll have to either restore a backup, or make the value small again).

Script improvements and additional support may be added later on.

JSON file looks like:

```JSON
{
         "0x40":"1",
         "0x325":"12835",
         "0x335":"12921",
         "0x41":"Z4Roadster",
         "0x330":"12895",
         "0x331":"2147483647",
         "0x332":"12900",
         "0x333":"12904",
         "0x336":"2147483647",
         "0x329":"100",
         "0x337":"1#1&True&0.063&0.0312&6&1#",
         "0x326":[
            {
               "0x322":"446",
               "0x323":"12839"
            },
            {
               "0x322":"453",
               "0x323":"12841"
            },
...
```

So each field name have to be search because names are probably hardcoded by the game! But values can be find easily by comparison.
