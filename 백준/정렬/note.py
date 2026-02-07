array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# 선택 정렬
for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

# 삽입 정렬
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j - 1], array[j] = array[j], array[j - 1]
        else:
            break
# 퀵 정렬
# 1
def quick_sort1(array, start, end):
    if start >= end: # 원소가 한개인 경우 종료
        return
    pivot = start
    left = start + 1
    right = end
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을때까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을때까지 반복
        while(right >= start and array[right >= array[pivot]]):
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort1(array, start, right - 1)
    quick_sort1(array, right + 1, end)