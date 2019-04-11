## Save Struct ##

The save file `savegame` start with 0x03 unknown bytes and then a JSON file.

## Editing ##

It's just a JSON editing. You need to put the 0x03 unknown bytes back after editing. That's all.

## Config & Script ##

- Currently, there are no config and script for this save file. Feel free to do one!

## TODO ##

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
