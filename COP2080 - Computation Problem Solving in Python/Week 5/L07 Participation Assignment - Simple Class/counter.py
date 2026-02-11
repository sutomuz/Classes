class Counter:
    def __init__(self):
        self._strokes = ""     # track clicks as string of "|"
        self.__limit = 0

    def setLimit(self, maximum):
        self.__limit = maximum

    def getValue(self):
        return self._strokes

    def click(self):
        if len(self._strokes) >= self.__limit:
            print("Limit Exceeded")
        else:
            self._strokes = self._strokes + "|"

    def reset(self):
        self._strokes = ""
