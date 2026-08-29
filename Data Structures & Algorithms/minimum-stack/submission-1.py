class MinStack:

    def __init__(self):
        self.arr = []
        self.ms = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        val = min(val, self.ms[-1] if self.ms else val)
        self.ms.append(val)

    def pop(self) -> None:
        val = self.arr.pop()
        self.ms.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.ms[-1]
