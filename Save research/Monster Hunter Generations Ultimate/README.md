TitleID: 0100770008DD8000
Save file name(s): system (there's also system_backup, but either the old 'system' file will be copied and renamed to system_backup (and the original, not renamed, file that the renamed-as-system_backup file is a copy of will be edited), or the system_backup file will be untouched, so whether this file even gets used depends on the implementation)
Save file type: bin
Offsets of each character: These offsets are relative to the end of the Switch save header (0x34 in the file), so add 0x34 to the values at these offsets to get the offset in relation to the start of the file. The offset for Character 1 is at **0x34** in the save (byte swapped), character 2 is at **0x38**, and Character 3 is at **0x3C**. I suggest that this editor only support the first slot initially, however, for ease of creation of this config; it can be improved on later if need be.

**Note: All offsets listed after this note ignore the 0x34 byte header at the beginning of the file, so you'll need to add 0x34 to each offset mentioned after this to get the offset relative to the beginning of the file. Also, each item is 19 BITS - the 12 low bits are the item ID while the high 7 are the item quantity. Finally, there's an unused 0x0000 at the beginning of each character's Item Box data that should be skipped over when reading the bits.**

Character 1 Money Offset = **[0x34] + 0x24** and **[0x34] + 0x280F** <-Both need to be the same value; the 1st is the value displayed on the Character Select screen, while the 2nd is the actual value
Character 1 Item Box Offset = **[0x34] + 0x0268** ; Length is 43700 bits, or 5462.5 bytes + 2 bytes (the 0x0000 that needs to be skipped)

This one is pretty difficult to implement, but it will probably end up relying on the bin.lua script to some degree for the item box.

I got a lot of this info from [here](https://github.com/mineminemine/MHXXSaveEditor/wiki/MHXX-'system'-file-structure), so props to @mineminemine / ukee from GBAtemp for documenting the 3DS version of MHXX's save format. Credits also go to the entities credited [here](https://github.com/mineminemine/MHXXSaveEditor#credits).