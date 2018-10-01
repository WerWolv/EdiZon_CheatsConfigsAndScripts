#!/usr/bin/env python3
"""
This is a little helper script, that I (Luro02)
wrote to help making the config files more consistent
and usable.
[DEPRECATED] Please use npm install & npm test instead
"""
import sys
import json
import pathlib
import argparse


def formatJSON(filepath: pathlib.Path):
	""" prettyfies a give JSON file
	Arguments:
		filepath: path object to the file ; pathlib.Path('../example.json')
	Returns:
		dict: the json-file as a dict
	"""
	with open(filepath, 'rb') as fd:
		try:
			data = json.load(fd)
		except json.decoder.JSONDecodeError:
			return False

	with open(filepath, 'w', encoding='utf-8') as fd:
		json.dump(data, fd, sort_keys=False, indent=4)

	return data



if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="formats a json-file")
	parser.add_argument(
		'-a',
		'--all',
		action='store_true',
		required=False,
		help='if this argument is used all json files in "../Configs/" will be formatted'
	)
	parser.add_argument(
		'-i',
		'--input',
		required=False,
		help='specify the file you want to format.'
	)
	args = parser.parse_args()
	if not args.all and not args.input:
		parser.parse_args('-h')
	if args.all:
		files = sorted(pathlib.Path("../Configs/").glob('*.json'))
	else:
		files = [pathlib.Path(args.input)]

	for i in files:
		if not formatJSON(i):
			print(f"Failed to parse: {i.as_posix()!r}, because it's an invalid JSON")

	print("Done.")
