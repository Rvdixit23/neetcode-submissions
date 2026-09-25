class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()
        for a in asteroids:
            stack.append(a)
            while len(stack) > 1 and stack[-2] > 0 and stack[-1] < 0:
                a2 = stack.pop()
                a1 = stack.pop()
                result = self.collisionCompute(a1, a2)
                if result:
                    stack.extend(result)
        return list(stack)

    def collisionCompute(self, a1, a2):
        aa1 = abs(a1)
        aa2 = abs(a2)
        if aa1 > aa2:
            return [a1]
        elif aa2 > aa1:
            return [a2]
        elif aa2 == aa1:
            return []
    
        
        