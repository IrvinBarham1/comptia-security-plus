import hashlib, time

class Block:
    def __init__(self, index, data, prev_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        to_hash = f"{self.index}{self.timestamp}{self.data}{self.prev_hash}".encode()
        return hashlib.sha256(to_hash).hexdigest()

def build_chain(n=3):
    chain = [Block(0, "Genesis Block", "0")]
    for i in range(1, n):
        chain.append(Block(i, f"Block {i} data", chain[-1].hash))
    return chain

def validate_chain(chain):
    for i , block in enumerate(chain):
        if block.hash != block.calc_hash():
            return False
        if i > 0 and block.prev_hash != chain[i-1].hash:
            return False
    return True

def main():
    chain = build_chain(4)
    for block in chain:
        print(f"Block {block.index}: {block.hash} (prev: {block.prev_hash[:8]}...)")

    print("\nChain valid? : ", validate_chain(chain))

    # Tamper with block 2
    chain[2].data = "Tampered!"
    print("\nAfter tampering, chain valid? : ", validate_chain(chain))

if __name__ == "__main__":
    main()
