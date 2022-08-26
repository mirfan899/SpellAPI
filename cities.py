import pandas as pd

names = pd.read_csv("data/uscities.csv", usecols=["city"])

with open("data/cities.txt", "a") as writer:
    for name in names.values.tolist():
        print(name[0])
        parts = name[0].split(" ")
        if len(parts) == 3:
            writer.write(parts[0] + " 1\n")
            writer.write(parts[1] + " 1\n")
            writer.write(parts[2] + " 1\n")
        elif len(parts) == 2:
            writer.write(parts[0] + " 1\n")
            writer.write(parts[1] + " 1\n")
        elif len(parts) == 1:
            writer.write(parts[0] + " 1\n")
