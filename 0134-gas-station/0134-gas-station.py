class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
            
        start_index = 0
        total_tank = 0
        
       
        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            
            
            if total_tank < 0:
                total_tank = 0
                start_index = i + 1
                
        return start_index