from bitcoin.rpc import RawProxy
import sys

if (len(sys.argv) > 1):
        txid = sys.argv[1]
else:
        txid = "0627052b6f28912f2703066a912ea577f2ce4da4caa5a5fbd8a57286c345c2f2"

p = RawProxy()


decoded_tx = p.decoderawtransaction(p.getrawtransaction(txid))

out_value = 0

for output in decoded_tx['vout']:
        out_value = out_value + output['value']

inp_value = 0

for output in decoded_tx['vin']:
        inp_txid = output['txid']
        index = output['vout']
        inp_decoded_tx = p.decoderawtransaction(p.getrawtransaction(inp_txid))
        inp_value += inp_decoded_tx['vout'][index]['value']

print("Transaction fee: ", inp_value - out_value)