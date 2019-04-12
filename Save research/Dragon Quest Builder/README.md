## Save Struct ##

The save file `PRMDAT.BIN` is Zlib compressed.
When you uncompress it those following offsets have been found:

Offset | Size | Description
--- | --- | ---
0x45020 | 0x54 | Inventory Items (21 Items?)
0x4509C | 0x100 | Items Slot 1 (64 Items?)
0x4519C | 0x100 | Items Slot 2 (64 Items?)
0x4529C | 0x100 | Items Slot 3 (64 Items?)

## Items ##

All thoses `Items` offsets got each item values stored in `4 bytes`:

Offset | Size | Description
--- | --- | ---
0x00 | u8 | Item Id
0x01 | u8 | Unknown (Item Id on 2 bytes?)
0x02 | u8 | Item Count
0x03 | u8 | Unknown (Item Count on 2 bytes?)

## Editing ##

It's just a binary editing. After that you have to compress the file back with Zlib. That's all.

## Config & Script ##

- Currently, there are no config and script for this save file. Feel free to do one!

## TODO ##

Find other values offsets. Determine Items Id?
