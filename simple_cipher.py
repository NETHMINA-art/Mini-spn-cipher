

SBOX = [
    0xE, 0x4, 0xD, 0x1,
    0x2, 0xF, 0xB, 0x8,
    0x3, 0xA, 0x6, 0xC,
    0x5, 0x9, 0x0, 0x7
]


INV_SBOX = [0] * 16

for i, value in enumerate(SBOX):
    INV_SBOX[value] = i



def rotate_left_4bit(value):
    return ((value << 1) & 0b1111) | (value >> 3)



def permute(value):
    bits = f"{value:04b}"
    result = bits[1] + bits[3] + bits[0] + bits[2]
    return int(result, 2)


def inverse_permute(value):
    bits = f"{value:04b}"
    result = bits[2] + bits[0] + bits[3] + bits[1]
    return int(result, 2)



def encrypt(plaintext, key):

    rotated_key = rotate_left_4bit(key)

    xor_result = plaintext ^ rotated_key

    permuted_result = permute(xor_result)

    ciphertext = SBOX[permuted_result]

    return ciphertext



def decrypt(ciphertext, key):

    rotated_key = rotate_left_4bit(key)

    inverse_sbox_result = INV_SBOX[ciphertext]

    inverse_perm_result = inverse_permute(inverse_sbox_result)

    plaintext = inverse_perm_result ^ rotated_key

    return plaintext



if __name__ == "__main__":

    plaintext = int("1011", 2)
    key = int("0110", 2)

    ciphertext = encrypt(plaintext, key)
    recovered = decrypt(ciphertext, key)

    print("=== Simplified 4-bit Cipher ===")

    print("Plaintext  :", f"{plaintext:04b}")
    print("Key        :", f"{key:04b}")
    print("Ciphertext :", f"{ciphertext:04b}")
    print("Recovered  :", f"{recovered:04b}")

    if recovered == plaintext:
        print("Verification: PASS")
    else:
        print("Verification: FAIL")