class MyQueue:

    # NOTE:
    # - Visualize and compare each step for one queue vs two stacks.
    # - Use `self` to access attributes in a Python class

    def __init__(self):
        self.main = []  # for storing elements
        self.aux = []  # for shuffling elements

    def push(self, x: int) -> None:
        self.main.append(x)

    def pop(self) -> int:
        # "All the calls to pop and peek are valid."
        # Shuffle from `main` to `aux` to get the bottom item
        while len(self.main) > 1:
            val = self.main.pop(-1)
            self.aux.append(val)
        popped = self.main.pop(-1)

        # Shuffle back to `main` to restore
        while len(self.aux) > 0:
            val = self.aux.pop(-1)
            self.main.append(val)
        return popped

    def peek(self) -> int:
        # "All the calls to pop and peek are valid."
        # Shuffle from `main` to `aux` to get the bottom item
        while len(self.main) > 1:
            val = self.main.pop(-1)
            self.aux.append(val)
        result = self.main[-1]

        # Shuffle back to `main` to restore
        while len(self.aux) > 0:
            val = self.aux.pop(-1)
            self.main.append(val)
        return result

    def empty(self) -> bool:
        return True if not self.main else False
