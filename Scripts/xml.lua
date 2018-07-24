local xml2lua = require("lib.xml2lua")
local handler = require("lib.T2")
local LuaToXml2 = require("lib.LuaToXml2")

function convertToTable(s)
	t = {}
	for i = 1, #s do
		t[i] = string.byte(s:sub(i, i))
	end
	return t
end

local parser = xml2lua.parser(handler)
local saveString = edizon.getSaveFileString()
saveString = saveString:sub(4)
parser:parse(saveString)
saveGame = handler.root
	
function getValueFromSaveFile()
	strArgs = edizon.getStrArgs()
	
	item = saveGame;
	
	for i, tag in pairs(strArgs) do
		if type(item) ~= "table" then break end
	
		item = item[tag]
	end
	
	return item
end

function setValueInSaveFile(value)
	local items = saveGame
	strArgs = edizon.getStrArgs()
	
	local ref = items
	
	for i, arg in ipairs(strArgs) do
		if i == #strArgs then
			ref[arg] = value
		else 
			ref = ref[arg]
		end
	end
end

function getModifiedSaveFile()
	convertedTable = {}
	--This is currently broken, somehow makes something invalid in the xml
	local xml = LuaToXml2.TableToXML(saveGame)
	convertedTable = convertToTable(xml)
	return convertedTable
end