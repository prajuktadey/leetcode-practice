class SeatManager:
    def __init__(self, n: int):
        self.hq = []
        self.current = 0

    def reserve(self) -> int:
        if self.hq:
            return heapq.heappop(self.hq)
        self.current += 1
        return self.current

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.hq, seatNumber)
