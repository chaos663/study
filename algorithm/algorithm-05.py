#대표값 구하기
import sys
import random as r
# K번 째 큰 수 구하기 !!
sys.stdin = open("input.txt", "rt")

# 풀어보자!!
# N명의 학생수를 입력받고
N = int(input())
# 각 학생의 수학점수를 또 입력받고
M = list(map(int,input().split()))
avr = round(sum(M)/N)
# 반올림 함수인 round()를 써서 반올림
# 내장함수 enumerate()는 예를들면, for idx, x in enumerate(M)이라고 하면 idx 에는 인덱스번호를 x에는 리스트의 요소값을 대응 시켜주는 함수
min = 999999999999999
# min 초기값을 엄청 큰 숫자로 잡아서 비교해서 최소값을 구해준다.
for idx, x in enumerate(M):
    # 절대값을 구하는 함수 abs()를 써서 거리(차이값)를 구해준다.
    tmp = abs(x-avr)

    if tmp < min :
        # 여기서 참이되니까 아래 코드를 수행해서 min 에 tmp가 들어가고 차이가 1보다 적어야만 참을 이룰 것이다.
        min = tmp
        # 점수인 x를 score에 넣어주고 !!
        score = x
        # 그 점수의 인덱스번호도 저장한다. index는 1부터 시작하니까 +1을 해줬다.
        res = idx + 1
    elif tmp == min :
        # 이 조건문을 쓰는 이유는 이제 평균으로부터 거리가 같은 것들을 비교하는데 , 같은 것들 중에서 score가 큰 것을 반환시켜야한다.
        if x > score:
            # 그래서 점수 x가 전 정답인 score보다 높으면 x는 현재의 score가 되고
            score = x
            # 인덱스 번호도 위와 같이 증가 된다.
            res = idx + 1
print(avr)
print(res)
'''파이썬에서 round() 함수는 round_half_up 방식이 아닌 round_half_even 방식이다. 만약 a = 4.500 이걸 반올림한다고 하면 4가 나온다.
 정확하게 중간잉 있으면 짝수로 근사값을 표현한다. 4가 짝수니까 4가 뜨는 것... 그래서 이 코드에서 round()를 사용해서 반올림을 하면 논리적 오류가 생긴다.
그래서 a를 반올림하려고 한다면, a = a+0.5를 더하면 정수의 1의 자리가 1증가하는 효과
a = int(a) 하면 소수점 날아가고 정수만 출력이 된다.'''