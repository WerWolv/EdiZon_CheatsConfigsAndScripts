-- Yoshi's Crafted World (modified bin) --
-- by DNA


checksum = require("lib.checksum")

struct_start = 0x0
quick_struct_start = 0xC40
struct_size = 0x208
offset_pipes = 0x21
offset_no_crash = 0x51
offset_unlock_nabbit = 0x4D
saveFileBuffer = edizon.getSaveFileBuffer()
	


function getValueFromSaveFile()
	strArgs = edizon.getStrArgs()
	intArgs = edizon.getIntArgs()
	slot = tonumber(strArgs[1], 16)
	offset = tonumber(strArgs[2], 16)
	addressSize = intArgs[1]
	valueSize = intArgs[2]
	
	value = 0
	

	
		
	for i = 0, valueSize - 1 do
		value = value | (saveFileBuffer[struct_start + offset + i + 1 + slot * struct_size] << i * 8)
	end
	
	
	return value
end



function setValueInSaveFile(value)
	strArgs = edizon.getStrArgs()
	intArgs = edizon.getIntArgs()
	slot = tonumber(strArgs[1], 16)
	offset = tonumber(strArgs[2], 16)
	dummy = strArgs[3]
	
	addressSize = intArgs[1]
	valueSize = intArgs[2]
	
	

	if dummy == "coins" then
		for i = 0, valueSize - 1 do
			saveFileBuffer[offset + i + 1] = (value & (0xFF << i * 8)) >> (i * 8)
			saveFileBuffer[offset + i + 1 + 0x50] = (value & (0xFF << i * 8)) >> (i * 8)
		end
	else
		for i = 0, valueSize - 1 do
			saveFileBuffer[struct_start + offset + i + 1 + slot * struct_size] = (value & (0xFF << i * 8)) >> (i * 8)
		end
	end
	
end



function setChecksum()
	gameFileBuffer = {}
	
	
	
	for num_struct = 0,5 do 
	address = 1
	
		for i = 1 + struct_start + num_struct * struct_size,  struct_start + (struct_size * (num_struct + 1)) - 4 do
			gameFileBuffer[address] = saveFileBuffer[i]			
			address = address + 1
		end
		
			crc = checksum.crc32(string.char(table.unpack(gameFileBuffer)))
   
		for i = 0, 3 do                                           
			saveFileBuffer[i + struct_start + struct_size * (num_struct + 1) - 3 ] = (crc & (0xFF000000 >> (i * 8))) >> (24 - i * 8)
		end
	end 
	
end

function getModifiedSaveFile()
	--copyquickslot()
	--setChecksum()
	return saveFileBuffer
end