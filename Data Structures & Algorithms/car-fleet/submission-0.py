class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        road= list(zip(position, speed)) 
        road.sort(key=lambda x: x[0])
        road = [(target - pos) / sp for pos, sp in road]

        for i in range(len(road)-2, -1, -1):
            if road[i+1] > road[i]:
                road[i] = road[i+1]
        
        return len(set(road))





        

        