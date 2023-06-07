# Holds events at certain times

class Timeslot:

    def __init__(self):
        self.times = [False] * 24



    def getFreeTimes(self):
        freeTimes =[]
        for time in range(len(self.times)):
            if self.times[time] is False:
                freeTimes.append(time)
        return freeTimes

    def getTakenTime(self):
        takenTimes = []
        for time in range(len(self.times)):
            if self.times[time] is True:
                takenTimes.append(time)
        return takenTimes


    def takeTimeSlot(self, time : int) -> bool:
        if time <= 24:
            if self.times[time] is False:
                self.times[time] = True
                return True
        return False




