
import heapq


def min_connection_price(cables):
    
    heapq.heapify(cables)

    total_cost = 0

    while len(cables) > 1:

        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        current_cost = first + second

        total_cost += current_cost

        heapq.heappush(cables, current_cost)
    
    return total_cost
