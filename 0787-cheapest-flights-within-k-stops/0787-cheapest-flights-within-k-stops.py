class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))
            
        prices = [float('inf')] * n
        prices[src] = 0
        
        queue = collections.deque([(src, 0)])
        stops = 0
        
        while queue and stops <= k:
            size = len(queue)
            next_prices = list(prices)
            
            for _ in range(size):
                curr, curr_price = queue.popleft()
                
                for neighbor, weight in adj[curr]:
                    if curr_price + weight < next_prices[neighbor]:
                        next_prices[neighbor] = curr_price + weight
                        queue.append((neighbor, next_prices[neighbor]))
                        
            prices = next_prices
            stops += 1
            
        return prices[dst] if prices[dst] != float('inf') else -1