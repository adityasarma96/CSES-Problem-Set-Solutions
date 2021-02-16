string = input()
max_rep = 1
count = 1
for i in range(1, len(string)):
    if string[i] == string[i - 1]:
        count += 1
        max_rep = max(count, max_rep)
    else:
        count = 1
print(max_rep)
