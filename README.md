Mini SPN Cipher

A simplified 4-bit block cipher written in Python, built to learn how a Substitution-Permutation Network (SPN) works. It has a single round, a 4-bit key, and a 4-bit block.

Educational project only. A 4-bit key has just 16 possible values, so this cipher is trivially breakable. Do not use it to protect real data.

How it works

Encryption takes a 4-bit plaintext and a 4-bit key and runs three steps:

Key rotation: the key is rotated left by 1 bit.
XOR (key mixing): the plaintext is XORed with the rotated key.
Permutation: the 4 bits are shuffled (bit order 1, 3, 0, 2).
Substitution: the result goes through a 4-bit S-box lookup.

Decryption runs the same steps in reverse: inverse S-box, inverse permutation, XOR with the rotated key.

plaintext --XOR--> permute --> S-box --> ciphertext
            ^
     rotate_left(key)
S-box
In	0	1	2	3	4	5	6	7	8	9	A	B	C	D	E	F
Out	E	4	D	1	2	F	B	8	3	A	6	C	5	9	0	7
Files
File	Description
simple_cipher.py	Full encrypt and decrypt implementation with a built-in self-test
xor_operation.py	Interactive demo of the key rotation and XOR step
Usage

Requires Python 3.6 or newer. No external libraries needed.

Run the cipher
bash
python simple_cipher.py

Example output:

=== Simplified 4-bit Cipher ===
Plaintext  : 1011
Key        : 0110
Ciphertext : 1001
Recovered  : 1011
Verification: PASS
Try the XOR step
bash
python xor_operation.py
Enter 4-bit plaintext: 1011
Enter 4-bit key: 0110

--- XOR Operation ---
Plaintext    : 1011
Original Key : 0110
Rotated Key  : 1100
XOR Result   : 0111
Use it in your own code
python
from simple_cipher import encrypt, decrypt

ciphertext = encrypt(0b1011, 0b0110)
plaintext = decrypt(ciphertext, 0b0110)
What I learned
How confusion (S-box) and diffusion (permutation) work together in an SPN
Why key mixing with XOR is reversible
How to build an inverse S-box and inverse permutation for decryption
Possible improvements
Add multiple rounds with a proper key schedule
Extend to an 8-bit or 16-bit block
Analyse the S-box (differential and linear cryptanalysis)
Add unit tests that check every plaintext and key combination
License

MIT
