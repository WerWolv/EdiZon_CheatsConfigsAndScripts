-- octp --

saveFileBuffer = edizon.getSaveFileBuffer()
cachedOffset = {}

function getStrArgsAsString()
	strArgs = edizon.getStrArgs()
	return ((strArgs[1] or '')..(strArgs[2] or '')..(strArgs[3] or ''))
end

function getOffset()
	strArgs = edizon.getStrArgs()
	intArgs = edizon.getIntArgs()
	strArgsAsString = getStrArgsAsString()

	if cachedOffset[strArgsAsString] ~= nil then
		return cachedOffset[strArgsAsString]
	end

	indirectAddress = tonumber(strArgs[1], 16)
	searchString = strArgs[3]

	addressSize = intArgs[1]

	offset = 0

	if searchString ~= nil and searchString ~= '' then
		searchTable = { searchString:byte(1, -1) }
		searchSize = searchString:len()

		for i = 1, #saveFileBuffer do
			if i - 1 + searchSize > #saveFileBuffer then
				break
			end
			found = false
			for j = 1, searchSize do
				c = saveFileBuffer[i + j -1]
				if c ~= searchTable[j] then
					break
				end
				found = j == 10
			end
			if found then
				offset = i - 1
				break
			end
		end
	elseif indirectAddress ~= 0 then
		for i = 0, addressSize - 1 do
			offset = offset | (saveFileBuffer[indirectAddress + i + 1] << i * 8)
		end
	end

	cachedOffset[strArgsAsString] = offset
	return offset
end

function getValueFromSaveFile()
	strArgs = edizon.getStrArgs()
	intArgs = edizon.getIntArgs()

	address = tonumber(strArgs[2], 16)
	valueSize = intArgs[2]

	offset = getOffset()
	value = 0

	for i = 0, valueSize - 1 do
		value = value | (saveFileBuffer[offset + address + i + 1] << i * 8)
	end

	return value
end

function setValueInSaveFile(value)
	strArgs = edizon.getStrArgs()
	intArgs = edizon.getIntArgs()
	address = tonumber(strArgs[2], 16)
	valueSize = intArgs[2]

	offset = getOffset()

	for i = 0, valueSize - 1 do
		saveFileBuffer[offset + address + i + 1] = (value & (0xFF << i * 8)) >> (i * 8)
	end
end

function getModifiedSaveFile()
	strArgsAsString = getStrArgsAsString()
	cachedOffset[strArgsAsString] = nil
	return saveFileBuffer
end
