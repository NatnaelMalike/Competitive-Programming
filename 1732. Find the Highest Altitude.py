class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur_altitude = 0
        highest_point = cur_altitude
        
        for altitude_gain in gain:
            cur_altitude += altitude_gain
            highest_point = max(highest_point, cur_altitude)
        
        return highest_point