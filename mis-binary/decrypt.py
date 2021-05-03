import pandas as pd
from Crypto.Util.number import long_to_bytes

df = pd.read_csv("binary.csv")
bits = "".join(map(str, df['0'].tolist()))
bits = int(bits, 2)
print("bits = ", bits)
print(long_to_bytes(bits))