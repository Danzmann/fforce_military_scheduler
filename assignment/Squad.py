import math
import random


class Squad:
    def __init__(self, time, numsquads):
        # Members of Squad, list of 2-item lists, 1st item member name,
        # 2nd is or not driver
        # Each squad has a stovewatch schedule
        # Each squad has a patrol schedule which is a list of lists with a variable
        # length according to the number of soldiers assigned to each patrol
        self.members = []
        self.StoveWatch = []
        self.patrol = []
        self.numsquads = numsquads  # stores the number of squads that exist
        self.ttime = time  # Stores the total time of the night shift for future ref
        self.time = time  # Time is relative to the squad
        self.medShiftTime = 0  # The time of each squadron member's shift
        self.roundMedShiftTime = 0  # ^^^ Rounded down
        self.extraShiftHours = 0  # In case not evenly divisible total time frame
        # for the total number of squads, extra shifts are added

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
        self.members.append([name, driver])

    #  A new squad was added to the list in main, so
    #  the total number of squads need updating.

    def BuildSWatch(self):
        drivers = []  # drivers list for later reference

        # JUST FOR DRIVERS
        for b in self.members:
            if b[1] == 1:
                drivers.append(b)

                for c in range(0,self.roundMedShiftTime):
                    self.StoveWatch.append(b)

        # EVERYONE ELSE
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
                if randomMember[1] != 1: # Not driver
                    break
            self.StoveWatch.append(randomMember)


    def CountMembersInPatrol(self, someone):
        count = 0
        for a in self.patrol:
            for b in a:
                if someone == b:
                    count += 1
        return count

    def BuildPatrol(self):

        currentPatrol = []

        numPatrolMember = self.time/len(self.members)

        for a in range(0, int(self.time)):
            for b in self.members:
                if b[1] == 1 and self.StoveWatch[a] != b and self.CountMembersInPatrol(b) \
                        < numPatrolMember*self.roundMedShiftTime:
                    currentPatrol.append(b)
                    break
            for b in self.members:
                if b[1] == 0 and self.StoveWatch[a] != b and self.CountMembersInPatrol(b) \
                        < numPatrolMember*self.roundMedShiftTime:
                    currentPatrol.append(b)
                    break

            self.patrol.append(currentPatrol)
            currentPatrol = []
        #self.PatrolOptimization(numPatrolMember)

# Not yet implemented
    def PatrolOptimization(self,numPatrolMember):

        # Checks who is driving alone (driver)
        problematic = []

        # Checks who has been underused (non-driver)
        underused = []

        for a in self.members:
            if self.CountMembersInPatrol(a) < numPatrolMember*self.roundMedShiftTime:
                for i in range(0, int(self.roundMedShiftTime)):
                    underused.append(a)

        index2 = 0
        for a in self.patrol:
            if len(a) == 1:
                # Uses a[0] to get rid of the [[item]] to just [item] and adds
                # index of it within patrol for future reference
                problematic.append([a[0], index2])
            index2 += 1

        current = 0
        if len(problematic) > 0:
            for a in problematic:
                index = 0
                for b in self.patrol:
                    break
                    index += 1
