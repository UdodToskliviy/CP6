def __min(arr):
    _min = 0
    for i in range(len(arr)):
        if i == 0:
            _min =arr[i]
        else:
            if arr[i] < _min:
                _min = arr[i]
    return _min

def DiffDelta(n, _min, delta):
    if n - _min == delta:
        return 1
    return 0



arr = []



print("Введите длину массива")
lenght = int(input())
print("Введите поочерёдно " + str(lenght) + " элементов массива")
for i in range(lenght):
    arr.append(int(input()))



print("Введите delta")
delta = int(input())

_min = __min(arr)

ans = 0
for i in range(len(arr)):
    ans += DiffDelta(arr[i], _min, delta)

print(ans)
