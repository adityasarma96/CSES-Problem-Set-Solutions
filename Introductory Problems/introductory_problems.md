# CSES PROBLEM SET 

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
