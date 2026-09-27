class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorter = [(pos, sp) for pos, sp in zip(position, speed)]
        sorter.sort(key=lambda x:x[0], reverse=True)

        pos = [i[0] for i in sorter]
        spe = [i[1] for i in sorter]


        fleetCount = len(pos)
        prevTime = None
        # 8 7 6 5 4 3
        for index in range(len(pos)):
            currTimeToTarget = (target - pos[index])/spe[index]
            if prevTime:
                if prevTime >= currTimeToTarget:
                    fleetCount -= 1
                prevTime = max(currTimeToTarget, prevTime)
            else:
                prevTime = currTimeToTarget
        return fleetCount
                

