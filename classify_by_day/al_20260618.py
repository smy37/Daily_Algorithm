class IntervalContainer:
    def __init__(self):
        self.starts = []
        self.ends = []
        self.results = [0]

    def add_interval(self, interval):
        start, end = sorted(interval)
        count = 0

        # Count the number of start points that are less than the end of the new interval
        start_count = sum(1 for s in self.starts if s < end)

        # Count the number of end points that are greater than the start of the new interval
        end_count = sum(1 for e in self.ends if e > start)

        # The number of intersections is the minimum of start_count and end_count
        count = min(start_count, end_count)

        # Insert the start and end points in the sorted order
        self.starts.append(start)
        self.starts.sort()
        self.ends.append(end)
        self.ends.sort()

        # Update the results list
        self.results.append(self.results[-1] + count)

# Test the IntervalContainer class
container = IntervalContainer()
intervals = [[1, 7], [6, 14], [3, 8], [18, 3]]

for interval in intervals:
    container.add_interval(interval)

print(container.results)
