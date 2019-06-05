## bin ##

import edizon, json

saveFileBuffer = edizon.getSaveFileBuffer()

zero_index = saveFileBuffer.find(b'\x00') # beginning index of the zero-padding at the end of the save file
skip_first_bytes = 3 # number of bytes to skip at the beginning of the save file

json_data = json.loads(saveFileBuffer[skip_first_bytes:zero_index].decode('utf8'))

def output_string():
	return saveFileBuffer[:skip_first_bytes] + bytes(json.dumps(json_data, separators=(',', ':')), 'utf8') + saveFileBuffer[zero_index + 1:]

def get_money_index():
	dollar_value = next(filter(lambda x: x["0x120"] == "Dollar", json_data['GTSWalletProfile']['0x13G']), None)

	if dollar_value is None:
		return -1

	return json_data['GTSWalletProfile']['0x13G'].index(dollar_value)

def get_addr_value(_str):
	if _str == "player_level":
		return int(json_data['GTSWalletProfile']['0x79'], 10)

	if _str == "player_money":
		index = get_money_index()

		if index < 0:
			return 0

		return int(json_data['GTSWalletProfile']['0x13G'][index]['0x43'], 10)

	return 0

def set_addr_value(_str, _newval):
	global json_data

	if _str == "player_level":
		json_data['GTSWalletProfile']['0x79'] = str(_newval)
		return

	if _str == "player_money":
		index = get_money_index()

		if index < 0:
			return

		json_data['GTSWalletProfile']['0x13G'][index]['0x43'] = str(_newval)
		return


def getValueFromSaveFile():
	_str_args = edizon.getStrArgs()
	return get_addr_value(_str_args[0])

def setValueInSaveFile(value):
	_str_args = edizon.getStrArgs()
	set_addr_value(_str_args[0], value)

def getModifiedSaveFile():
	return output_string()

