class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = [[(val[0]**2 + val[1]**2), val[0], val[1]] for val in points]
        dists = self.boundMergeSort(dists, 0, len(dists) - 1, k)
        return [[val[1], val[2]] for val in dists[:k]]
    
    def boundMergeSort(self, dists, s, e, k):
        if e - s < 1:
            return dists
        for i in range(s, e):
            if dists[i][0] < dists[e][0]:
                tmp = dists[s]
                dists[s] = dists[i]
                dists[i] = tmp
                s += 1
        tmp = dists[s]
        dists[s] = dists[e]
        dists[e] = tmp

        dists = self.boundMergeSort(dists, 0, s - 1, k)
        if s + 1 < k:
            dists = self.boundMergeSort(dists, s + 1, e, k)
        return dists

        