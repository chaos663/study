#코드 구현력 기르기
# k번째 약수
import sys
sys.stdin = open("input.txt", "rt")
N,K = map(int,input().split(" "))
# 텍스트 파일에 옆으로 나열되어있는 거는 map으로 읽고, 띄어쓰기로 구분해놨으니까 split(" ")을 써야한다.
# 인풋용 텍스트 파일 만들어서 불러와서 사용 !
print(N,K)
# 함수로 만든 것
def K_div(N,K):
    cnt = 0
    for i in range(1,N+1):
        if N%i == 0 :
            cnt+=1
        if cnt==K :
            print(i)
            break
    else :
        print(-1)

K_div(N,K)

# 강의 자료 답안
cnt = 0
for i in range(1,N+1):
    if N%i == 0 :
        cnt+=1
        # 약수가 True면, cnt를 1증가시킨다.
    if cnt==K :
         print(i)
         # 이 때, K번 째로 작은 약수를 출력하고 for문을 정지시킨다.
         break
else :
    print(-1)


