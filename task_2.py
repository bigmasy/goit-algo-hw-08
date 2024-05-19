import heapq

def merge_k_lists(lists):
    min_heap = []

    for i, list in enumerate(lists):
        if list:
            heapq.heappush(min_heap, (list[0], i, 0))

    merged_list = []

    while min_heap:
        value, list_index, element_index = heapq.heappop(min_heap)
        merged_list.append(value)
        
        if element_index + 1 < len(lists[list_index]):
            next_tuple = (lists[list_index][element_index + 1], list_index, element_index + 1)
            heapq.heappush(min_heap, next_tuple)

    return merged_list

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
