import time
import hashlib

class Block:
    def __init__(self, index, previous_hash, timestamp, data):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}"
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = []
        self.add_block(Block(0, "0", time.time(), "Genesis Block"))  # Block pertama

    def add_block(self, block):
        self.chain.append(block)

    def print_chain(self):
        for block in self.chain:
            print(f"Index: {block.index}, Hash: {block.hash}, Previous Hash: {block.previous_hash}, Data: {block.data}")


# Menggunakan kelas Blockchain
if __name__ == "__main__":
    my_blockchain = Blockchain()
    
    # Menambahkan blok baru
    my_blockchain.add_block(Block(1, my_blockchain.chain[-1].hash, time.time(), "Transaksi 1"))
    my_blockchain.add_block(Block(2, my_blockchain.chain[-1].hash, time.time(), "Transaksi 2"))
    my_blockchain.add_block(Block(3, my_blockchain.chain[-1].hash, time.time(), "Transaksi 3"))
    
    
    # Mencetak isi blockchain
    my_blockchain.print_chain()
