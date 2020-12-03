# Python-bitcoinlib project

To run the program you need:

* Download chosen program code.
* Download [python](https://www.python.org/downloads/).
* Install python-bitcoinlib library: `pip install python-bitcoinlib`
* To perform code calculation, you must have access to the Bitcoin full node
* When connected to Bitcoin full node, compile program code using `python nameoffile.py`


## What does each program do?
* 1uzduotis.py - program that calculates transaction fee of any given Bitcoin transaction (by providing its hash`$ python 1uzduotis.py [tx_hash]`)
* default transaction hash - 0627052b6f28912f2703066a912ea577f2ce4da4caa5a5fbd8a57286c345c2f2
![Capture](https://user-images.githubusercontent.com/57493215/101085145-b19bd800-35b7-11eb-99eb-c224edf32a68.PNG)
* 2uzduotis.py - program that checks if the block hash is correct by comparing manually calculated hash with the one that is given in a block. The block is specified by providing its blockheight `$ python 2uzduotis.py [block_height]`.
* default blockheight - 277316
![Capture](https://user-images.githubusercontent.com/57493215/101085078-916c1900-35b7-11eb-9b69-1f76695f4d3a.PNG)
