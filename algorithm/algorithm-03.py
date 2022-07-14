import sys
import random as r
# K번 째 큰 수 구하기 !!
sys.stdin = open("input.txt", "rt")
''' 
문제) 현수는 1부터 100사이의 자연수가 적힌 N장의 카드를 가지고 있습니다.
 같은 숫자의 카드가 여러장 있을 수 있습니다. 현수는 이 중 3장을 뽑아 각 카드에 적힌 수를 합한 값을 기록하려 고 합니다. 
 3장을 뽑을 수 있는 모든 경우를 기록합니다. 기록한 값 중 K번째로 큰 수를 출력 하는 프로그램을 작성하세요.
만약 큰 수부터 만들어진 수가 25 25 23 23 22 20 19......이고 K값이 3이라면 K번째 큰 값 은 22입니다.'''
'''
1부터 100사이의 자연수 N 장의 카드
카드의 번호는 중복가능
이 중 3장을 뽑아서 리스트에 담는다
리스트의 요소를 sum()으로 합해서 프린트한다.
3장을 뽑을 수 있는 모든 경우를 또 하나의 리스트에 기록한다.
그리고 리스트 안에서 k번째 수를 출력한다.
'''

# 풀이

N,K = map(int,input().split())
a = list(map(int,input().split()))
# 중복을 제거하는 내장 함수 set()을 써서 자료구조를 만들면 중복되지않게 array륾 만들어준다.!
res = set()
# 3중 for문을 사용한다. j는 i뒤편부터 for문, m은 j뒷편부터 for>> 중복을 방지하기 위해서 3중 for문을 사용한 것!
for i in range(N):
    for j in range(i+1, N):
        for m in range(j+1,N) :
            res.add(a[i]+a[j]+a[m])
res = list(res)
# 내림차순으로 만들어주기위해서 set 자료형을 list로 만들어줬다.
res.sort(reverse=True)
print(res[K-1])
print("합의 ",K,"번째로 큰 수 는 ",res[K-1],"입니다.")