n = int(input())
phoneBook = {}
for _ in range(n):
    key, value = input().split()
    phoneBook[key] = value

while True:
    try:
        name = input().strip()
        if name == "":
            break
        if name in phoneBook:
            print(name + '=' + phoneBook[name])
        else:
            print('Not found')
    except:
        break
