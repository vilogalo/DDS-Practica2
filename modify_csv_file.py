with open("epa-http.csv", "r") as f:
    data = f.readlines()

for n,x in enumerate(data):
    if len(x.split(" ")) < 7:
        data[n] = f"{data[n][0:-1]} -\n"

with open("epa-http.csv", "w") as f:
    f.writelines(data)
