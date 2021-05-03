with open("output.txt", "r") as f:
    num = int(f.read())
print(num.to_bytes(64, "big"))