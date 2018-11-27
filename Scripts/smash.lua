-- bin --

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
		if strArgs[1] == "53FF60" then
			for i = 0, valueSize - 1 do
				value = value | (saveFileBuffer[indirectAddress + i + 1 + 160] << i * 8)
			end
		end

		if strArgs[1] == "426C70" then
			for i = 0, valueSize - 1 do
				value = value | (saveFileBuffer[indirectAddress + i + 1 + 7] << i * 8)
			end
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
	j = 0
	if indirectAddress ~= 0 then
		if strArgs[1] == "53FF60" then
			for i = 0, address - indirectAddress - 1, 4 do
				if j == 0 or j == 4 or j == 8 then
					saveFileBuffer[indirectAddress+i+1] = value
				end

				if j == 12 then
					j = 0
				else
					j = j+4
				end
			end
		end

		if strArgs[1] == "426C70" then
			for i = 0, address - indirectAddress - 1 do
				if saveFileBuffer[indirectAddress + i] ~= 0 and saveFileBuffer[indirectAddress + i] < 255 then
					saveFileBuffer[indirectAddress + i + 1] = value
				end
			end
		end

	else	
		for i = 0, valueSize - 1 do
			saveFileBuffer[offset + address + i + 1] = (value & (0xFF << i * 8)) >> (i * 8)
		end
	end
end

function getModifiedSaveFile()
	return saveFileBuffer
end

function getModifiedSaveFile()
	return saveFileBuffer
end
