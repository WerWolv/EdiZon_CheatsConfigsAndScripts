-- New Super Mario Bros U Deluxe (modified bin) --
-- by DNA

checksum = require("lib.checksum")

saveFileBuffer = edizon.getSaveFileBuffer()


function getValueFromSaveFile()
	strArgs = edizon.getStrArgs()
	intArgs = edizon.getIntArgs()
	indirectAddress = tonumber(strArgs[1], 16)
	address = tonumber(strArgs[2], 16)
	addressSize = intArgs[1]
	valueSize = intArgs[2]
	
	offset = 0
	value = 0
		
	if indirectAddress ~= 0 then
		for i = 0, addressSize - 1 do
			offset = offset | (saveFileBuffer[indirectAddress + i + 1] << i * 8)
		end
	end
		
	for i = 0, valueSize - 1 do
		value = value | (saveFileBuffer[offset + address + i + 1] << i * 8)
	end
	
	return value
end

function setValueInSaveFile(value)
	strArgs = edizon.getStrArgs()
	intArgs = edizon.getIntArgs()
	indirectAddress = tonumber(strArgs[1], 16)
	address = tonumber(strArgs[2], 16)
	dummy = strArgs[3]
	
	addressSize = intArgs[1]
	valueSize = intArgs[2]
	
	offset = 0
	
	if indirectAddress ~= 0 then
		for i = 0, addressSize - 1 do
			offset = offset | (saveFileBuffer[indirectAddress + i + 1] << (i * 8))
		end
	end
	
	if dummy == "Lives" then
		for i = 0, 4 do
			saveFileBuffer[offset + address + i + 1] = value
		end
	else
		for i = 0, valueSize - 1 do
			saveFileBuffer[offset + address + i + 1] = (value & (0xFF << i * 8)) >> (i * 8)
		end
	end

end


function setChecksum()
	gameFileBuffer = {}
	
	struct_start = 0x10
	struct_size = 0x207
	
	
	for num_struct = 0,2 do 
	address = 1
	
		for i = 1 + struct_start + num_struct * struct_size + num_struct, 1 + struct_start + struct_size * (num_struct + 1) - 4 + num_struct do
			gameFileBuffer[address] = saveFileBuffer[i]
			address = address + 1
		end
		
			crc = checksum.crc32(string.char(table.unpack(gameFileBuffer)))
   
		for i = 0, 3 do                                           
			saveFileBuffer[i + 1 + struct_start + struct_size * (num_struct + 1) - 3 + num_struct] = (crc & (0xFF000000 >> (i * 8))) >> (24 - i * 8)
		end
	end 
	
end

function getModifiedSaveFile()
	setChecksum()
	return saveFileBuffer
end