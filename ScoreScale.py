import math as m
import pandas as pd
import sys

# Special CSV mode.
if len(sys.argv) > 5 and sys.argv[1] == "--csv":
    fname = sys.argv[2]
    df = pd.read_csv(fname)
    assert("score" in list(df.columns))
    assert(sys.argv[3] == "--factor")
    scale = float(sys.argv[4])

    df["score"] = m.ceil(2*df["score"]*scale) / 2

    df.to_csv(fname)

scale = input("Enter the scale factor: ")
scaleF = float(scale)
print("begin: ")
while True:
    x = input("Score: ")
    xFloat = float(x)
    print(m.ceil(2*xFloat*scaleF)/2)
