-- Rune Factory 4 Special (modified from "dktf" and "bin" which this is common Little Endian) --
-- IMPORTANT: 
--   Save file is always 0x022480 (140416) bytes in size, where the first 4 bytes are
--   the CRC32 of [0x04 .. 0x02239F (140192) ]
--   Mainly for JP(Asia) version, not sure if NA or PAL version could work normally or not.

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
	addressSize = intArgs[1]
	valueSize = intArgs[2]
	
	offset = 0
	
	if indirectAddress ~= 0 then
		for i = 0, addressSize - 1 do
			offset = offset | (saveFileBuffer[indirectAddress + i + 1] << (i * 8))
		end
	end
		
	for i = 0, valueSize - 1 do
		saveFileBuffer[offset + address + i + 1] = (value & (0xFF << i * 8)) >> (i * 8)
	end
end

function setChecksum()
	gameFileBuffer = {}
	-- 140192 with  first 4 is crc32, so 140188 --
	for i = 1, 140188 do
		gameFileBuffer[i] = saveFileBuffer[i + 4]
	end
	crc = checksum.crc32(string.char(table.unpack(gameFileBuffer)))
	for i = 0,3 do
	saveFileBuffer[4 - i] = (crc & (0xFF000000 >> (i * 8))) >> (24 - i * 8)
	end
end

function getModifiedSaveFile()
	setChecksum()
	return saveFileBuffer
end

