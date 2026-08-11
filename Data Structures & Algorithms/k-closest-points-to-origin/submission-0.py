class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest_dist = [math.inf] * k
        closest_pt = [None] * k
        furthest = math.inf
        furthestidx = 0

        def get_furthest_idx():
            newfurthest = -math.inf
            newfurthestidx = 0
            for i in range(len(closest_dist)):
                if closest_dist[i] > newfurthest:
                    newfurthest = closest_dist[i]
                    newfurthestidx = i
            return newfurthest, newfurthestidx

        for x, y in points:
            d = x**2 + y**2
            if d < furthest:
                closest_pt[furthestidx] = [x, y]
                closest_dist[furthestidx] = d
                furthest, furthestidx = get_furthest_idx()

        return closest_pt
