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