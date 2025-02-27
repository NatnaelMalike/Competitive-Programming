class UndergroundSystem:

    def __init__(self):
        self.check_in = {}
        self.travel_records = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_in.pop(id)
        travel_t = t - start_time
        route = (start_station, stationName)
        if route not in self.travel_records:
            self.travel_records[route] = [0, 0]
        self.travel_records[route][0] += travel_t
        self.travel_records[route][1] += 1

        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = (startStation, endStation)
        return self.travel_records[route][0] / self.travel_records[route][1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)