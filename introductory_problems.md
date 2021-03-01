
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

### [Increasing Array](https://cses.fi/problemset/task/1094/)
```python
n = int(input())
array = list(map(int, input().split()))

count = 0
for i in range(1, n):
    if array[i] < array[i - 1]:
        count += array[i - 1] - array[i]
        array[i] = array[i-1]
print(count)
```

### [Permutations](https://cses.fi/problemset/task/1070/)
```python
n = int(input())

if 1 < n < 4:
    print("NO SOLUTION")
else:
    a = [i * 2 if i <= n // 2 else (i - n // 2) * 2 - 1 for i in range(1, n + 1)]
    print(*a)
```

### [Number Spiral](https://cses.fi/problemset/result/1716950/)
```python
n = int(input())
 
 
def squared_start_behind(i): return (i - 1) * (i - 1) + 1
def squared_start(i): return i * i
def seq_increasing(f, i, j): return f(i) + j - 1
def seq_decreasing(f, i, j): return f(i) - j + 1
 
 
def get_spiral_value(x, y):
    if x <= y:
        return seq_increasing(squared_start_behind, y, x) if y % 2 == 0 else seq_decreasing(squared_start, y, x)
    else:
        return seq_decreasing(squared_start, x, y) if x % 2 == 0 else seq_increasing(squared_start_behind, x, y)
 
 
for _ in range(n):
    x, y = map(int, input().split())
    print(get_spiral_value(x, y))
```
