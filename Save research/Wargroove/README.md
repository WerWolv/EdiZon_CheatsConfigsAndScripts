## Save Struct ##

The save file are `aiTurnStateX` where `X` is a number between 0 and 9 (Slot?).

Save struct is:

Offset | Size | Description
--- | --- | ---
0x00 | u64 | savedata uncompressed size
0x08 |   | Zlib compressed savedata

Then you have to uncompress the data with Zlib.

## Data ##

The uncompressed savedata is unknown but data looks like serialized.

## Editing ##

You need to write a deserializer/serializer for the data, then compress the data back and finally write the uncompressed size as the struct above said.

## Config & Script ##

- Currently, there are no config and script for this save file. Feel free to do one!

## TODO ##

Everything.
