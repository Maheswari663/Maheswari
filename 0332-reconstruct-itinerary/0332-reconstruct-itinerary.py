class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)
            
        itinerary = []
        
        def dfs(airport):
            while adj[airport]:
                next_destination = adj[airport].pop()
                dfs(next_destination)
            itinerary.append(airport)
            
        dfs("JFK")
        return itinerary[::-1]