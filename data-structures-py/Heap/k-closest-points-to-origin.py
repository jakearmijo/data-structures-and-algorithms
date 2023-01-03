from collections import heapq

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
        points_track = []
        for n in points:
            distance = (n[0]**2) + (n[1]**2)
            points_track.append([distance, n])

        points_track.sort()

        result = []

        for i in points_track:
            result.append(i[1])
            if len(result) == k:
                return result
