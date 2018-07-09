saveFileBuffer = edizon.getSaveFileBuffer()
cachedOffset = {}

function getStrArgsAsString()
	strArgs = edizon.getStrArgs()
	return ((strArgs[1] or '')..'_'..(strArgs[3] or '')..'_'..(strArgs[4] or ''))
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
	start = 1
	
	r = tonumber(strArgs[4], 10)
	
	--[[if cachedOffset[((strArgs[1] or '')..'_'..(strArgs[3] or '')..'_'..(r-1))] ~= nil then
		start = cachedOffset[((strArgs[1] or '')..'_'..(strArgs[3] or '')..'_'..(r-1))]+2
		r = r - 1
	end]]--
	
	if searchString ~= nil and searchString ~= '' then
		searchTable = { searchString:byte(1, -1) }
		searchSize = searchString:len()
		
		for i = start, #saveFileBuffer do
			if i - 1 + searchSize > #saveFileBuffer then
				break
			end
			found = false
			for j = 1, searchSize do
				c = saveFileBuffer[i + j -1]
				if c ~= searchTable[j] then
					break
				end
				found = j == searchSize
			end
			if found then
				r = r - 1
				if ( r <= 0 ) then
					offset = i - 1
					break
				end
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
	cachedOffset = {}
	return saveFileBuffer
end