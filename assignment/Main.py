import Squad


Patrols = []


def AddSquad(time,Squads):

    print("Enter squad members name, one by one, exit to finish:")
    Squads.append(Squad.Squad(time, len(Squads)+1))
    cond = 1

    while cond:
        member = input("Squad member: ")
        if member == "exit":
            cond = 0
            continue
        driver = input("Is it a driver? (y/n): ")
        if driver.lower() == "y":
            Squads[len(Squads) - 1].AddMember(member, 1)
        elif driver.lower() == "n":
            Squads[len(Squads) - 1].AddMember(member, 0)
        else:
            print("invalid")
    for a in Squads:
        a.updateTimeCalc(time/len(Squads))


def countAll():
    count = 0
    for i in Squads:
        count += i.NumMembers()
        return count

def TotalTime(stime, etime):
    count = 0
    while stime != etime:
        if stime == 24:
            stime = 0
        count += 1
        stime += 1
    return count


def showSchedule(Squads, stime, ttime):
    # currtime will show the time of current shift (start time + i)
    currtime = stime
    currSquad = 0
    currSquadMember = 0
    # Cycles though the entire timeframe and shows each StoveWatch soldier
    for i in range(0, ttime):
        # Resets clock after 24 hours to another day
        if currtime == 24:
            currtime = 0

        # When one Squad is done, another will begin
        if (len(Squads[currSquad].StoveWatch)) == currSquadMember:
            currSquad += 1
            currSquadMember = 0

        print(str(currtime) + ":00 " + str(Squads[currSquad].StoveWatch[currSquadMember][0]))
        currSquadMember += 1
        currtime += 1


def main():
    Squads = []

    #Temporary terminal inputs:
    Squads = []

    stime = int(input("Enter the start time of the night routine: "))
    etime = int(input("Enter the end time of the night routine: "))
    ttime = TotalTime(stime,etime)

    while True:
        AddSquad(ttime,Squads)
        cond = input("exit to quit, other input to add another Squad: ")
        if cond.lower() == "y":
            for a in Squads:
                a.NewSquad()
            continue
        if cond.lower() == "n":
            break

    for a in Squads:
        a.BuildSWatch()

    showSchedule(Squads, stime, ttime)



if __name__ == "__main__":
    main()

#    patrols = input("How many patrols are there? ")

#    for a in patrols:
 #       Patrols.append(Squad.Patrol())
