class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area1 = abs((C - A) * (D - B))
        area2 = abs(((G - E) * (H - F)))
        total_area = area1 + area2

        if C <= E or A >= G or F >= D or H <= B:
            return total_area
        else:
            x = max(A, E) - min(G, C)
            y = max(F, B) - min(H, D)
            over_lap = abs(x * y)
            total_area = total_area - over_lap
            return total_area
