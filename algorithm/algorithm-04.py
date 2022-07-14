#최솟값 구하기
import sys
import random as r
# K번 째 큰 수 구하기 !!
sys.stdin = open("input.txt", "rt")

arr = [5, 3, 7, 9, 2, 5, 2, 6]

arrMin = float('inf')
# 무한대 값으로 변수 초기화(첫 인덱스를 무조건 참으로 만들기 위해서)

#방법1
for i in range(len(arr)):
    if arr[i] < arrMin :
        # i가 0 이면 arr[0]은 5이니까 참이다
        arrMin = arr[i]
print("최솟값은",arrMin,"입니다.")


arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin = float('inf')
# 방법 2
for x in arr:
    if x < arrMin :
        arrMin = x
print("최솟값은", arrMin, "입니다.")
