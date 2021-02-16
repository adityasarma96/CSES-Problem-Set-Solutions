
## Introductory Problems

### [Weird Algorithm](https://cses.fi/problemset/task/1068)

```python
n = int(input())
sequence = [n]
while n != 1:
    n = n // 2 if n % 2 == 0 else n * 3 + 1
    sequence.append(n)
print(*sequence)
```

### [Missing Number](https://cses.fi/problemset/task/1083)

```python
n = int(input())
numbers = list(map(int,input().split()))
print(n*(n+1)//2 - sum(numbers))
```

### [Missing Number](https://cses.fi/problemset/task/1083)

```python
n = int(input())
numbers = list(map(int,input().split()))
print(n*(n+1)//2 - sum(numbers))
```

### [Repetitions](https://cses.fi/problemset/task/1069)
```python
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

```
