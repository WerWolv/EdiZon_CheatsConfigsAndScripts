-- pmtok --

json = require("lib.json")
checksum = require("lib.checksum")


saveFileStringHash = edizon.getSaveFileString()
saveFileStringHash = saveFileStringHash:gsub('{%s*}', '{"edizon":true}')
oldHash = saveFileStringHash:sub(saveFileStringHash:len()-7)
saveFileString = saveFileStringHash:gsub(oldHash,"")
saveFileBuffer = json.decode(saveFileString)

function getValueFromSaveFile()
	strArgs = edizon.getStrArgs()
	intArgs = edizon.getIntArgs()

	item = saveFileBuffer
	
	for i, tag in pairs(strArgs) do
		if type(item) ~= "table" then break end
	
		if string.sub(tag, 1, 1) == "\\" then
			tag = tonumber(tag:sub(2)) + 1
			
			if tag == nil then return 0 end
		end
	
		item = item[tag]
	end
	if intArgs[1] == 0 then -- Generic
		return item
	elseif intArgs[1] == 1 then -- Boolean
		return item and 1 or 0
	elseif intArgs[1] == 2 then -- Item Slot
		if type(item) ~= "table" then return "-2:INVALID_SLOT" end
		return (item["type"]~=nil and item["type"] or "-1") .. ":" .. (item["itemId"]~=nil and item["itemId"] or "")
	end
end

function getStringFromSaveFile()
	return getValueFromSaveFile()
end

function string:split(sep)
   local sep, fields = sep or ":", {}
   local pattern = string.format("([^%s]*)", sep)
   self:gsub(pattern, function(c) fields[#fields+1] = c end)
   return fields
end

function validateSlot()
	print("not yet implemented!")
end

function setValueInSaveFile(value)
	local items = saveFileBuffer
	strArgs = edizon.getStrArgs()
	intArgs = edizon.getIntArgs()
	
	local ref = items
		
	for i, tag in ipairs(strArgs) do
		
		if string.sub(tag, 1, 1) == "\\" then
			tag = tonumber(tag:sub(2)) + 1
		end
		if i == #strArgs then
			if intArgs[1] == 0 then -- Generic
				ref[tag] = value
			elseif intArgs[1] == 1 then -- Boolean
				ref[tag] = (value == 1)
			elseif intArgs[1] == 2 then -- Item Slot
				local splits = value:split(":")
				local typ = splits[1]~=nil and splits[1] or "-1"
				local itemId = splits[2]~=nil and splits[2] or ""
				typ = tonumber(typ)
				if typ == -1 then -- EMPTY Slot
					itemId = ""
				end
				ref[tag]["type"] = typ
				ref[tag]["itemId"] = itemId
			end
		else 
			ref = ref[tag]
		end
		
	end
end

function setStringInSaveFile(value)
	setValueInSaveFile(value)
end

local ITEM_LOOKUP_TABLE = {
  ["0:HAMMER"] = "Hammer",
  ["0:SILVER_HAMMER"] = "Shiny Hammer",
  ["0:SUPER_HAMMER"] = "Flashy Hammer",
  ["0:GREAT_HAMMER"] = "Legendary Hammer",
  ["0:GOLDEN_HAMMER"] = "Gold Hammer",
  ["0:THROW_HAMMER"] = "Hurlhammer",
  ["0:SUPER_THROW_HAMMER"] = "Flashy Hurlhammer",
  ["0:FIRE_HAMMER"] = "Fire Hammer",
  ["0:ICE_HAMMER"] = "Ice Hammer",
  ["1:BOOTS"] = "Boots",
  ["1:SILVER_BOOTS"] = "Shiny Boots",
  ["1:SUPER_BOOTS"] = "Flashy Boots",
  ["1:GREAT_BOOTS"] = "Legendary Boots",
  ["1:GOLD_BOOTS"] = "Gold Boots",
  ["1:IRON_BOOTS"] = "Iron Boots",
  ["1:STEEL_BOOTS"] = "Shiny Iron Boots",
  ["1:SUPER_IRON_BOOTS"] = "Flashy Iron Boots",
  ["1:SUPER_STEEL_BOOTS"] = "Legendary Iron Boots",
  ["4:KINOKO"] = "Mushroom",
  ["4:SUPER_KINOKO"] = "Shiny Mushroom",
  ["4:GREAT_KINOKO"] = "Flashy Mushroom",
  ["4:HEEL_KINOKO"] = "1-Up Mushroom",
  ["4:FIRE_FLOWER"] = "Fire Flower",
  ["4:SUPER_FIRE_FLOWER"] = "Shiny Fire Flower",
  ["4:ICE_FLOWER"] = "Ice Flower",
  ["4:SUPER_ICE_FLOWER"] = "Shiny Ice Flower",
  ["4:TAIL"] = "Tail",
  ["4:SUPER_TAIL"] = "Shiny Tail",
  ["4:POW_BLOCK"] = "POW Block",
  ["2:PSV_Battle_DAMAGE1"] = "Guard Plus",
  ["2:PSV_Battle_DAMAGE2"] = "Silver Guard Plus",
  ["2:PSV_Battle_DAMAGE3"] = "Gold Guard Plus",
  ["2:PSV_Puzzle_TIME1"] = "Time Plus",
  ["2:PSV_Puzzle_TIME2"] = "Silver Time Plus",
  ["2:PSV_Puzzle_TIME3"] = "Gold Time Plus",
  ["2:PSV_Sub_PaperVacuum"] = "Confetti Vacuum",
  ["2:PSV_Sub_FlowerShower"] = "Petal Bag",
  ["2:PSV_Sub_MembersCard1"] = "Membership Card",
  ["2:PSV_Sub_MembersCard2"] = "Silver Membership Card",
  ["2:PSV_Sub_MembersCard3"] = "Gold Membership Card",
  ["2:PSV_Battle_HP1"] = "Heart Plus",
  ["2:PSV_Battle_HP2"] = "Silver Heart Plus",
  ["2:PSV_Battle_HP3"] = "Gold Heart Plus",
  ["2:PSV_Sub_KinopioAlarm"] = "Toad Alert",
  ["2:PSV_Sub_TreasureAlarm"] = "Treasure Alert",
  ["2:PSV_Sub_HideBlockAlarm"] = "Hidden Block Alert",
  ["4:IC_KINOPIO_RS"] = "Toad Radar",
  ["4:IC_WHISTLE"] = "Boot Whistle",
  ["2:PSV_Sub_BattleParty"] = "Ally Tambourine",
  ["4:IC_LATENCY"] = "Lamination Suit",
  ["2:PSV_Sub_Pedometer"] = "Coin Step Counter",
  ["2:PSV_Sub_MarioSound"] = "Retro Soundbox",
  ["4:IC_SECRET_BLOCK_RS"] = "Hidden Block Unhider",
  ["-1:"] = "Nothing"
}

item_slot = 1
key_item_slot = 1

local dummy_equipped = {
	slot_type = "hammer",
	slot = 1,
	item_slot = -1
}

local DUMMY_TYPES = {
	hammer = {
		max_slot = 4,
		item_type = 0
	},
	boots = {
		max_slot = 4,
		item_type = 1
	},
	amulet = {
		max_slot = 6,
		item_type = 2
	}
}

function getDummyValue()
	local items = saveFileBuffer
	if items["Pouch"]==nil 
		or items["Pouch"]["equipment"]==nil 
		or items["Pouch"]["equipment"]["bag"]==nil 
		or items["Pouch"]["equipment"]["hammer"]==nil
		or items["Pouch"]["equipment"]["boots"]==nil
		or items["Pouch"]["equipment"]["amulet"]==nil
		or items["Pouch"]["key_item"]==nil then
			return 0
		end
	strArgs = edizon.getStrArgs()
	intArgs = edizon.getIntArgs()

	if strArgs[1] == "bag" then
		local item = items["Pouch"]["equipment"]["bag"][tostring(item_slot - 1)]
		local keyitem = items["Pouch"]["key_item"][tostring(key_item_slot - 1)]

		if strArgs[2] == "item_slot" then
			return item_slot
		elseif strArgs[2] == "item_descriptor" then
			return item["type"] .. ":" .. item["itemId"]
		elseif strArgs[2] == "item_damage" then
			return item["usedEndurance"]
		elseif strArgs[2] == "item_durability" then
			return item["usedBreakRate"]
		elseif strArgs[2] == "item_count" then
			return item["stackCount"]
		elseif strArgs[2] == "key_item_slot" then
			return key_item_slot
		elseif strArgs[2] == "key_item_name" then
			return keyitem["id"]
		elseif strArgs[2] == "key_item_hidden" then
			return keyitem["removed"] and 1 or 0
		end
	elseif strArgs[1] == "equipped" then
		local dummy_nil = (dummy_equipped.item_slot == 0)

		if dummy_equipped.item_slot < 0 then
			dummy_equipped.item_slot = items["Pouch"]["equipment"][dummy_equipped.slot_type][dummy_equipped.slot] + 1
		end

		local dummy_item = items["Pouch"]["equipment"]["bag"][tostring(dummy_equipped.item_slot - 1)] or {type=-1,itemId=""}

		if dummy_equipped[strArgs[2]]~=nil then
			return dummy_equipped[strArgs[2]]
		elseif strArgs[2] == "item_name" then
			if dummy_nil then return "None" end
			local id = dummy_item["type"]..":"..dummy_item["itemId"]
			return ITEM_LOOKUP_TABLE[id]
		elseif strArgs[2] == "valid" then
			if dummy_nil then return 1 end
			return dummy_item["type"]==DUMMY_TYPES[dummy_equipped.slot_type]["item_type"] and 1 or 0
		end
	end
end


function getDummyString()
	return getDummyValue()
end

function setDummyValue(value)
	local items = saveFileBuffer
	if items["Pouch"]==nil 
		or items["Pouch"]["equipment"]==nil 
		or items["Pouch"]["equipment"]["bag"]==nil
		or items["Pouch"]["equipment"]["hammer"]==nil
		or items["Pouch"]["equipment"]["boots"]==nil
		or items["Pouch"]["equipment"]["amulet"]==nil 
		or items["Pouch"]["key_item"]==nil then
			return 0
		end
	strArgs = edizon.getStrArgs()
	intArgs = edizon.getIntArgs()
		
	if strArgs[1] == "bag" then
		local item = items["Pouch"]["equipment"]["bag"][tostring(item_slot - 1)]
		local keyitem = items["Pouch"]["key_item"][tostring(key_item_slot - 1)]
		if strArgs[2] == "item_slot" then
			item_slot = value
		elseif strArgs[2] == "item_descriptor" then
			local splits = value:split(":")
			local typ = splits[1]~=nil and splits[1] or "-1"
			local itemId = splits[2]~=nil and splits[2] or ""
			typ = tonumber(typ)
			if typ == -1 then -- EMPTY Slot
				itemId = ""
			end
			item["type"] = typ
			item["itemId"] = itemId
		elseif strArgs[2] == "item_damage" then
			item["usedEndurance"] = value
		elseif strArgs[2] == "item_durability" then
			item["usedBreakRate"] = value
		elseif strArgs[2] == "item_count" then
			item["stackCount"] = value
		elseif strArgs[2] == "key_item_slot" then
			key_item_slot = value
		elseif strArgs[2] == "key_item_name" then
			keyitem["id"] = value
		elseif strArgs[2] == "key_item_hidden" then
			keyitem["removed"] = (value==1)
		end
	elseif strArgs[1] == "equipped" then
		if strArgs[2] == "slot_type" and DUMMY_TYPES[value]~=nil then
			dummy_equipped.slot_type = value
			dummy_equipped.slot = 1
			dummy_equipped.item_slot = items["Pouch"]["equipment"][value][1] + 1
		elseif strArgs[2] == "slot" then
			if value <= DUMMY_TYPES[dummy_equipped.slot_type]["max_slot"] then
				dummy_equipped.slot = value
				dummy_equipped.item_slot = items["Pouch"]["equipment"][dummy_equipped.slot_type][value] + 1
			end
		elseif strArgs[2] == "item_slot" then
			dummy_equipped.item_slot = value
			local dummy_item = items["Pouch"]["bag"][tostring(value - 1)]
			if (dummy_item~=nil and dummy_item["type"]==DUMMY_TYPES[dummy_equipped.slot_type]["item_type"]) or dummy_equipped.item_slot == 0 then
				items["Pouch"]["equipment"][dummy_equipped.slot_type][dummy_equipped.slot] = dummy_equipped.item_slot - 1
			end
		end
	else
		print("Unknown Dummy Hierarchy! '" .. strArgs[1] .. "'")
	end
end

function setDummyString(value)
	setDummyValue(value)
end

local function convertToTable(s)
	t = {}
	
	for i = 1, #s do
		t[i] = string.byte(s:sub(i, i))
	end
	
	return t
end

function getModifiedSaveFile()
	encoded = json.encode(saveFileBuffer)
	
	encoded = encoded:gsub('{"edizon":true}', '{}')

	crc = checksum.crc32(encoded)

	encoded = encoded .. string.format("%08x",crc)
	
	convertedTable = {}
	convertedTable = convertToTable(encoded)
				
	return convertedTable
end