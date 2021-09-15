import math

class Pair:
    def __init__(self, HC_member1, HC_member2):
        self.HCmember1 = HC_member1
        self.HCmember2 = HC_member2
        self.distance = self.compute_distance()
    
    def __lt__(self, p2):
        return self.distance < p2.get_distance()

    def compute_distance(self):
        x = 0
        for i in range(len(self.HCmember1)):
            x += (self.HCmember1[i] - self.HCmember2[i])**2
        return math.sqrt(x)

    def get_distance(self):
        return self.distance
        
    def get_hc_member1(self):
        return self.HCmember1

    def get_hc_member2(self):
        return self.HCmember2