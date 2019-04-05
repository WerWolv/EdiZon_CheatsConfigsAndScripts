from gzip import zlib
import hashlib

import sys

def main():
    if len(sys.argv) == 2 and sys.argv[1] in options:
        print(sys.argv[1] + ": " + options[sys.argv[1]]['description'])
    elif len(sys.argv) > 2 and sys.argv[1] in options:
        args = sys.argv[2:]
        options[sys.argv[1]]['function'](args)
    else:
        for key in options.keys():
            print(key + ": " + options[key]['description'])

def zlib_decompress(args):
    startAddr = int(args[1], 0) if len(args) > 1 else None
    endAddr = int(args[2], 0) if len(args) > 2 else None

    inFile = open(args[0], 'rb').read()
    decompressedData = zlib.decompress(inFile[startAddr:endAddr])

    outFile = open(args[0] + ".decomp", 'wb')
    outFile.write(decompressedData)
    outFile.close()

def zlib_compress(args):
    compressionLevel = int(args[1], 0) if len(args) > 1 else None
    startAddr = int(args[2], 0) if len(args) > 2 else None
    endAddr = int(args[3], 0) if len(args) > 3 else None

    inFile = open(args[0], 'rb').read()
    compressedData = zlib.compress(inFile[startAddr:endAddr], compressionLevel)

    outFile = open(args[0] + ".comp", 'wb')
    outFile.write(compressedData)
    outFile.close()

def crc32(args):
    startAddr = int(args[1], 0) if len(args) > 1 else None
    endAddr = int(args[2], 0) if len(args) > 2 else None

    inFile = open(args[0], 'rb').read()
    print('CRC32 checksum: ' + hex(zlib.crc32(inFile[startAddr:endAddr]) % (1<<32)))

def md5(args):
    startAddr = int(args[1], 0) if len(args) > 1 else 9
    endAddr = int(args[2], 0) if len(args) > 2 else None

    inFile = open(args[0], 'rb').read()
    print('MD5 hash: 0x' + hashlib.md5(inFile[startAddr:endAddr]).hexdigest())

options = {
    'zlib_compress' : { 'function' : zlib_compress, 'description' : 'Compresses file with zlib. Args: < FilePath, [CompressionLevel], [StartAddress], [EndAddress] >' },
    'zlib_decompress' : { 'function' : zlib_decompress, 'description' : 'Decompresses zlib compressed file. Args: < FilePath, [StartAddress], [EndAddress] >' },
    'crc32' : { 'function' : crc32, 'description' : 'Calculates the CRC32 checksum of a file. Args: < FilePath, [StartAddress], [EndAddress] >' },
    'md5' : { 'function' : md5, 'description' : 'Calculates the MD5 Hash of a file. Args: < FilePath, [StartAddress], [EndAddress] >' }
}

if __name__ == '__main__':
    main()
