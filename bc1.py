import hashlib as hasher
import datetime as date

class Block:
    def __init__(self,index,timestamp,data ,previous_hash):
        self.index = index
        self.timestamp =timestamp
        self.data = data
        self.previous_hash =previous_hash
        self.hash =self.hash_block()

    def hash_block (self):
        encrypt=hasher.sha256()
        encrypt.update(str(self.index)+str(self.timestamp)+str(self.data)+str(self.previous_hash))
        return encrypt.hexdigest()
    
    @staticmethod
    def create_genesis_block():
        return Block(0,date.datetime.now(),"genesis block","0")
    
    @staticmethod
    def next_block(last_block):
        this_index = last_block.index+1
        this_timestamp = date.datetime.now()
        this_data = "this is data" +str(this_index)
        this_hash = last_block.hash
        return Block(this_index,this_timestamp,this_data,this_hash)

blockchain = [Block.create_genesis_block()]
previous_block = blockchain[0]
num_of_blocks =20

for i in range (0,20):
    block_to_add = Block.next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block =block_to_add

    print"block #{} has been added to blockchain!".format(block_to_add.index)
    print"Hash:{}\n".format(block_to_add.hash)
