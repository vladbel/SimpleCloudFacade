class Counter():
    _counter = None

    def __init__(self):
        self._counter = 0

    def get_value(self):
        self._counter += 1
        return self._counter
