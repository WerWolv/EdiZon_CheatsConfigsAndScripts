## Save Struct ##

The save file `userdata.dat` got a 0x48 bytes header, a 0x48 bytes subheader and the data.
Header struct is:

Offset | Size | Description
--- | --- | ---
0x00 | u32 | Magic "SUTC"
0x04 | u32 | Version? (Always 0x00)
0x08 | u32 | Save file size
0x0C | 0x2C | Always 0x00
0x38 | u32 | CRC32 checkum from 0x48 to EndOfFile

SubHeader struct is:

Offset | Size | Description
--- | --- | ---
0x00 | u32 | Magic "SUTC"
0x04 | u32 | Version? (Always 0x01)
0x08 | 0x40 | Unknown

Data struct is unknown.

## Data ##

Data in `userdata.dat` can be found with some files comparison. I used an existing PC Editor to found some offsets. But some of them was false, so I have found correct ones by deduction! You can find all the list of offsets in the Config file.

## Editing ##

It's just a binary editing. After that the new CRC32 is computed and written in the header. That's all.

## Config & Script ##

- Script: [mk8.py](https://github.com/WerWolv/EdiZon_ConfigsAndScripts/blob/master/Scripts/mk8.py)
- Config: [0100152000022000.json](https://github.com/WerWolv/EdiZon_ConfigsAndScripts/blob/master/Configs/0100152000022000.json)

## TODO ##

Right now the current script support edit of stats. The games seems to create more files to unlock tracks or karts. So maybe some other edits can be add