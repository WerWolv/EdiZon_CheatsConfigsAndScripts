## Save Struct ##

The save file got a 0x10 bytes header and a byml file after that.
Header struct is:

Offset | Size | Description
--- | --- | ---
0x00 | u32 | CRC32 checkum from 0x04 to EndOfFile
0x04 | u32 | Version? (Always 0x01)
0x08 | u32 | Save file size
0x0C | u32 | Byml section size

## Data ##

To parse the byml, you have to use [byml-v2.py by leoetlino](https://github.com/leoetlino/byml-v2/tree/python3.5) to get an object with all the save value inside. This looks like:

```
{
    'AchievementSaveData': [{
        'GetTime': 1510358823,
        'IsGet': True,
        'Name': 'Scenario_Ending'
    }, {
        'GetTime': 1514860862,
        'IsGet': True,
        'Name': 'Scenario_WorldAll'
    }, {
        'GetTime': 1512769379,
        'IsGet': True,
        'Name': 'Shine_Gather_1'
    }, {
        'GetTime': 1512769388,
        'IsGet': True,
        'Name': 'Shine_Gather_2'
    }, {
        'GetTime': 1514860870,
        'IsGet': True,
        'Name': 'Shine_Gather_3'
    }

... and more
```

## Editing ##

After modified the byml object data, you have to convert back the object to the binary byml and then rewrite the sizes stored in the header. You don't need to recompute the save checksum since the game don't check it! (I haven't try to set it to 0x00000000)

## Config & Script ##

- Script: [smo.py](https://github.com/WerWolv/EdiZon_ConfigsAndScripts/blob/master/Scripts/smo.py)
- Config: [0100000000010000.json](https://github.com/WerWolv/EdiZon_ConfigsAndScripts/blob/master/Configs/0100000000010000.json)

## TODO ##

Right now the current script support edit of Coins, purchasable Items / Clothes / Caps / Stickers.
There are a lot of values who can be edited too, like the collectibles coins, stars, etc...
You can get the byml object content by uncomment [this line](https://github.com/WerWolv/EdiZon_ConfigsAndScripts/blob/master/Scripts/smo.py#L13) and then read it in `sd://EdiZon/EdiZon.log`.