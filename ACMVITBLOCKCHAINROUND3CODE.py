import hashlib # Standard library for SHA-256

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0 # This is the "counter" we change to find a valid hash
        self.hash = "" 

    def calculate_hash(self):
        """Creates a SHA-256 hash of the block's contents."""
        # We combine all block information into one long string
        block_content = str(self.index) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        
        # .encode() turns the string into bytes, .hexdigest() turns the result into a readable hex string
        return hashlib.sha256(block_content.encode()).hexdigest()

    def mine_block(self, difficulty_prefix="0000"):
        """The 'Mining' process: finds a hash that starts with four zeros."""
        print(f"Mining Block {self.index}...")
        while True:
            self.hash = self.calculate_hash()
            if self.hash.startswith(difficulty_prefix):
                print(f"Success! Block {self.index} Mined. Nonce: {self.nonce} Hash: {self.hash}")
                break
            self.nonce += 1 # If hash is invalid, increment nonce and try again

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """Requirement: Hardcoded first block."""
        genesis = Block(0, "Genesis Block", "0")
        genesis.mine_block()
        self.chain.append(genesis)

    def add_new_block(self, name, reg_no, branch):
        """Adds a new block with user-provided data."""
        data = f"Name: {name} | Reg: {reg_no} | Branch: {branch}"
        prev_hash = self.chain[-1].hash # Get the hash of the last block in the list
        
        new_block = Block(len(self.chain), data, prev_hash)
        new_block.mine_block()
        self.chain.append(new_block)

# --- Main Execution ---
my_blockchain = Blockchain()

for i in range(1, 3):
    print(f"\n--- Entry for Committee Member {i} ---")
    u_name = input("Enter Name: ")
    u_reg = input("Enter Reg No: ")
    u_branch = input("Enter Branch: ")
    my_blockchain.add_new_block(u_name, u_reg, u_branch)

# Display final results
print("\n" + "="*50 + "\nFINAL BLOCKCHAIN RECORD\n" + "="*50)
for b in my_blockchain.chain:
    print(f"Index: {b.index} | Data: {b.data}")
    print(f"Prev Hash: {b.previous_hash}")
    print(f"Current Hash: {b.hash}\n" + "-"*30)
