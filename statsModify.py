import json
from urllib.parse import urlparse

with open("data.json") as f:
    data = json.load(f)

x = {}

for i in data:
    w = i["id"]
    v = i["views"]

    if (w == None) or (w == "null"):
        w = "Direct"
    else:
        w = urlparse(w).netloc

    if ("localhost" in w) or ("127.0.0.1" in w):
        w = "localhost"

    if w in x:
        x[w] += v
    else:
        x[w] = v


# sort the dictionary by value
x = dict(sorted(x.items(), key=lambda item: item[1], reverse=True))


t = "Website,Views\n"

for i in x:
    print(i, x[i])

    t += i + "," + str(x[i]) + "\n"

with open("stats.csv", "w") as f:
    f.write(t)
