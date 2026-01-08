# ACM VIT Round 3 - Blockchain Task

This repository contains a Python implementation of a simple, immutable blockchain for the ACM 2026 Committee Selections.

## Implementation Details
- **Genesis Block:** Hardcoded with index 0 and a previous hash of "0".
- **Proof of Work:** Implements a mining loop where each block's SHA-256 hash must start with four leading zeros (`0000`).
- **Data Integrity:** Each block is linked to the previous one via its cryptographic hash, ensuring the chain is immutable.
- **Dynamic Entry:** The script dynamically accepts member details (Name, Reg No, Branch) for the subsequent blocks.
