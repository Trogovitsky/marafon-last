h = input().strip()
if not h:
    print("ERROR")
    exit()

p = h.split()

if len(p) % 2 != 0:
    print("ERROR")
    exit()

s = []
for i in range(0, len(p), 2):
    n = p[i]
    ht = p[i + 1]

    if not n or n.isdigit():
        print("ERROR")
        exit()

    try:
        he = int(ht)
    except ValueError:
        print("ERROR")
        exit()
    if not (50 <= he <= 250):
        print("ERROR")
        exit()

    s.append((-he, n, he))

s.sort()

sorted_list = [f"{name} {height}" for (_, name, height) in s]
print(" ".join(sorted_list))
