import builtins

class array:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"({self.data})"

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, index):
        return self.data[index]

    def tolist(self):
        return self.data.copy()

    def __add__(self, other):
        if isinstance(other, array):
            return array([a + b for a, b in zip(self.data, other.data)])
        else:
            return array([a + other for a in self.data])
    def __sub__(self, other):
        if isinstance(other, array):
            return array([a - b for a, b in zip(self.data, other.data)])
        else:
            return array([a - other for a in self.data])
    def __mul__(self, other):
        if isinstance(other, array):
            return array([a * b for a, b in zip(self.data, other.data)])
        else:
            return array([a * other for a in self.data])
    def __truediv__(self, other):
        if isinstance(other, array):
            return array([a / b for a, b in zip(self.data, other.data)])
        else:
            return array([a / other for a in self.data])

    def __pow__(self, other):
        if isinstance(other, array):
            return array([a ** b for a, b in zip(self.data, other.data)])
        else:
            return array([a ** other for a in self.data])

    def __neg__(self):
        return array([-a for a in self.data])
    
    def __radd__(self, other):
        return self.__add__(other)
    def __rsub__(self, other):
        return array([other - a for a in self.data])
    def __rmul__(self, other):
        return self.__mul__(other)
    def __rtruediv__(self, other):
        return array([other / a for a in self.data])
    
    def zeros(shape):
        if isinstance(shape, int):
            shape = (shape,)
        return array([0.0] * shape[0])

    def ones(shape):
        if isinstance(shape, int):
            shape = (shape,)
        return array([1.0] * shape[0])

    def mean(self, arr):
        if not isinstance(arr, array):
            raise TypeError("Input must be an instance of array")
        return sum(arr.data) / len(arr.data) if arr.data else 0.0

    def std(self, arr):
        if not isinstance(arr, array):
            raise TypeError("Input must be an instance of array")
        mean_value = self.mean(arr)
        variance = sum((x - mean_value) ** 2 for x in arr.data) / len(arr.data) if arr.data else 0.0
        return variance ** 0.5

    def median(self, arr):
        if not isinstance(arr, array):
            raise TypeError("Input must be an instance of array")
        sorted_data = sorted(arr.data)
        n = len(sorted_data)
        if n == 0:
            return 0.0
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2.0
        else:
            return sorted_data[mid]

    def var(self, arr):
        if not isinstance(arr, array):
            raise TypeError("Input must be an instance of array")
        mean_value = self.mean(arr)
        return sum((x - mean_value) ** 2 for x in arr.data) / len(arr.data) if arr.data else 0.0

    def min(self, arr):
        if not isinstance(arr, array):
            raise TypeError("Input must be an instance of array")
        return builtins.min(arr.data)

    def max(self, arr):
        if not isinstance(arr, array):
            raise TypeError("Input must be an instance of array")
        return builtins.max(arr.data)

def linspace(start, stop, num=50):
    if num < 0:
        raise ValueError("num must be non-negative")
    if num == 0:
        return array([])
    if num == 1:
        return array([start])
    step = (stop - start) / (num - 1)
    return array([
        start + i * step
        for i in range(num)
    ])
def arange(start, stop=None, step=1):
    if stop is None:
        start, stop = 0, start
    if step == 0:
        raise ValueError("step must not be zero")
    result = []
    value = start
    if step > 0:
        while value < stop:
            result.append(value)
            value += step
    else:
        while value > stop:
            result.append(value)
            value += step
    return array(result)