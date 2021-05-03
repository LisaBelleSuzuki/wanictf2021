def decrypt(plaintext: str, a: int, b: int) -> str:
    originaltext = ""
    for x in plaintext:
        if "A" <= x <= "Z":
            x = ord(x) - ord("A")
            for i in range(8):
                cur = x + 26 * i
                cur -= b
                if (cur % a != 0):
                    continue
                cur //= a
                cur += ord("A")
                cur = chr(cur)
                break
        else:
            cur = x
        originaltext += cur
    return originaltext



if __name__ == "__main__":
    cyphertext = "HLIM{OCLSAQCZASPYFZASRILLCVMC}"
    # FLAG -> HLIM
    # a == 5
    # b == 8
    print(decrypt(cyphertext, a=5, b=8))
