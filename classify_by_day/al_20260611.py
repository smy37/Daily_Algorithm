class MyCalendarTwo:

    def __init__(self):
        self.books = []
        self.overlaps = []

    def book(self, startTime: int, endTime: int) -> bool:
        for s, e in self.overlaps:
            if s < endTime and e > startTime:
                return False

        for s, e in self.books:
            if s < endTime and e > startTime:
                self.overlaps.append([max(s, startTime), min(e, endTime)])
        self.books.append([startTime, endTime])
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)