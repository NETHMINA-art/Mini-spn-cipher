

plaintext = input("Enter 4-bit plaintext: ")
key = input("Enter 4-bit key: ")


if (
    len(plaintext) != 4
    or len(key) != 4
    or not all(bit in "01" for bit in plaintext)
    or not all(bit in "01" for bit in key)
):
    print("Error: Please enter exactly 4 binary bits.")

else:
    
    rotated_key = key[1:] + key[0]

    
    xor_result = ""

    for p, k in zip(plaintext, rotated_key):
        xor_result += str(int(p) ^ int(k))

    print("\n--- XOR Operation ---")
    print("Plaintext    :", plaintext)
    print("Original Key :", key)
    print("Rotated Key  :", rotated_key)
    print("XOR Result   :", xor_result)