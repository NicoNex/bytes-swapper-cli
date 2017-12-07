#! /usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys
import os


def getBytes (filename):
	return bytearray(open(filename, "rb").read())


def bytesSwapper (filename):
	bytes_array = getBytes(filename)
	
	for x in range(0, len(bytes_array) - 2, 2):
		tmp = bytes_array[x]
		bytes_array[x] = bytes_array[x + 1]
		bytes_array[x + 1] = tmp

	return bytes_array


def scrambleFile (bytes_array, filename):
	with open(filename, "wb") as file:
		file.write(bytes_array)


def createParser ():
	parser = argparse.ArgumentParser(description="A tool that swaps the bytes of a file")
	parser.add_argument("inputFile", help="Path to the file", nargs="*")
	parser.add_argument("-o", "--output", help="Output directory")

	return parser


if __name__ == "__main__":
	parser = createParser()
	parser = parser.parse_args(sys.argv[1:])
	
	for file in parser.inputFile:
		if os.path.exists(file):
			bytes_array = bytesSwapper(file)
			
			if parser.output:
				filename = file.split("/")[-1]
				if os.path.exists(parser.output):
					scrambleFile(bytes_array, parser.output+filename)

			else:
				scrambleFile(bytes_array, file)

		else:
			print("File %s not found" % file)
