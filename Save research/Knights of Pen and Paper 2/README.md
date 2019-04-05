## Research

The majority of the save file is zlib compressed. The compressed section goes from 0x04 to 0x30E0 which decompresses into a 4MB save file.

### Integer Key-Values
`[KEY_STRING_LENGTH][KEY_STRING][DATA]`

### String Key-Values
`[KEY_STRING_LENGTH][KEY_STRING][VALUE_STRING_SIZE][VALUE_STRING]`

### String List
`[KEY_STRING_LENGTH][KEY_STRING][??LIST_LENGTH??][LIST_STRINGS]`
`LIST_STRINGS` is separated by the `|` (Pipe) symbol.