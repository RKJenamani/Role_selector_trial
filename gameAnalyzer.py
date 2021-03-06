import enum

class gameAnalyzer():
    class staticPlays(enum.Enum):
        FreeHomeKick = 0
        FreeAwayKick = 1
        IndirectHomeKick = 2
        IndirectAwayKick = 3
        HomePenalty = 4
        AwayPenalty = 5

    def __init__(self, tasklist, state, play=None):
        # tasklist -> list of available tactics
        # state -> belief state
        # play -> static play, if it is None means we have decide it dynamically
        self.tasklist = tasklist
        self.state = state
        self.play = play
        self.home_yellow = state.isteamyellow

    def availableBots():
        # return list of available bots using state
        bots = []
        for i in xrange(len(state.homePos)):
            if state.homeDetected[i]:
                bots.append(i)

        return bots

    def targetPoints(tasks):
        # input -> list of tasks(Tactics)
        # ouput -> a dict, keyword -> tasks name, value -> their target point

        #assuming class names for tactics are TBallHandler , TMarker etc.
        task_dict = {'Defender':TDefender,'BallHandler':TBallHandler,'Marker':TMarker,'Supporter':TSupporter,'Attacker':TAttacker,'Distractor':TDistractor,'Clearer':TClearer}
        required_task_dict = {}
        for i in xrange(len(tasks)):
            obj = task_dict[tasks[i]]()
            required_task_dict[tasks[i]] = obj.getTargetPos(state)

        return required_task_dict

    def staticPlays():
        curPlay = -1
        for play in staticPlays:
            if play.value == self.play:
                curPlay = play.value
                break
        if curPlay > -1:
            if curPlay == 0:
                # FreeHomeKick
                requiredTasks = ['BallHandler','Clearer','Marker','Marker','Defender']  # add more task here
                tasks = self.intersection(requiredTasks, self.tasklist)
                # task is dict, keyword -> tasks name, value -> their target point
                tasks = self.targetPoints(tasks)
                bots = self.availableBots()
                return tasks, bots

        else:
            print("this static play is not available!!")

