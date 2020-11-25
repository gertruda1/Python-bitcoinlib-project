from bitcoin.rpc import RawProxy
import struct
import sys
import hashlib

def little_endian_int(num):
        return struct.pack('<I', num).encode('hex')

def little_endian_str(value):
    bin = value.decode('hex')
    hex = bin[::-1].encode('hex_codec')
    return hex

if (len(sys.argv) > 1):
        blockheight = sys.argv[1]
else:
        blockheight = 277316


p = RawProxy()

block = p.getblock(p.getblockhash(blockheight))

version = little_endian_str(block['versionHex'])
prev_hash = little_endian_str(block['previousblockhash'])
merkle = little_endian_str(block['merkleroot'])
time = little_endian_int(block['time'])
bits = little_endian_str(block['bits'])
nonce = little_endian_int(block['nonce'])


header_hex = version + prev_hash + merkle + time + bits + nonce


header_bin = header_hex.decode('hex')

hash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
hash = hash[::-1].encode('hex_codec')

if (hash == block['hash']):
        print("Hash is correct")
else:
        print("Hash is incorrect")
