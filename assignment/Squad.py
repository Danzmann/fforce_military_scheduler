import math
import random

class Squad:
    def __init__(self, time, numsquads):
        # Members of Squad, list of 2-item lists, 1st item member name,
        # 2nd is or not driver
        # Each squad has a stovewatch schedule
        self.members = []
        self.StoveWatch = []
        self.numsquads = numsquads  # stores the number of squads that exist
        self.ttime = time  # Stores the total time of the night shift for future ref
        self.time = time  # Time is relative to the squad
        self.medShiftTime = 0
        self.roundMedShiftTime = 0
        self.extraShiftHours = 0

    # When new squad is added, update time calculations
    # (new squad means splitting total time and recalculating everything)
    def updateTimeCalc(self,time):
        self.time = self.ttime
        self.time /= self.numsquads
        if len(self.members) == 0: # To avoid division by zero
            self.medShiftTime = self.time
        else:
            self.medShiftTime = self.time / (len(self.members))
        self.roundMedShiftTime = int(math.floor(self.medShiftTime))
        if self.roundMedShiftTime == 0:
            self.roundMedShiftTime = 1
        # Not evenly divided number of squads for the total shift hours:
        if self.time % self.numsquads != 0:
            self.extraShiftHours = self.ttime - math.floor(self.ttime / self.numsquads) * self.numsquads

    def AddMember(self, name, driver):
        self.members.append([name,driver])

    #  A new squad was added to the list in main, so
    #  the total number of squads need updating.
    def NewSquad(self):
        self.numsquads += 1

    def NumMembers(self):
        return len(self.members)

    def BuildSWatch(self):
        drivers = []  # drivers list for later reference

        #JUST FOR DRIVERS
        for b in self.members:
            if b[1] == 1:
                drivers.append(b)

                for c in range(0,self.roundMedShiftTime):
                    self.StoveWatch.append(b)


        #EVERYONE ELSE
        for b in self.members:
                if b not in drivers:  # Drivers were already added
                    if len(self.members) % self.time != 0:
                        # There is uneven number of soldier for shift hours
                        # Randomly chooses extra members for extra shift later
                        for c in range(0, int(self.roundMedShiftTime)):
                            self.StoveWatch.append(b)

                    else:
                        for c in range(0, int(self.medShiftTime)):
                            self.StoveWatch.append(b)

        if self.ttime % self.numsquads != 0:
            difference = math.floor(self.time - self.roundMedShiftTime*len(self.members))
        else:
            difference = self.time - self.roundMedShiftTime*len(self.members)

        # Will add random squad members to extra shifts
        random.seed()
        for c in range(0, int(difference)):
            # checks to not get a driver
            while True:
                randomMember = random.choice(self.members)
                if randomMember not in drivers:
                    break
            self.StoveWatch.append(randomMember)

    # If the number of shift hours cannot be divided equally among squads,
    # Main will randomly choose an instance (one squad) to activate this method on,
    # and fill the blank space of shifts
    def BuildSWatchExtra(self):

        for i in range(0, int(self.extraShiftHours)):
            while True:
                randomMember = random.choice(self.members)
                if randomMember[1] != 1:
                    break
            self.StoveWatch.append(randomMember)


    def BuildPatrol(self):
        pass


class Patrol:
    def AssignSquad(self, Squad):
        pass