import pandas as pd

names = pd.read_csv("data/NationalNames.csv", usecols=["Name"])

with open("dictionary/names.txt", "a") as writer:
    for name in names.values.tolist():
        print(name[0])
        parts = name[0].split(" ")
        if len(parts) == 2:
            writer.write(parts[0] + " 1\n")
            writer.write(parts[1] + " 1\n")
        else:
            writer.write(parts[0] + " 1\n")
