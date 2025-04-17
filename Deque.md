## 데크(Double-ended Queue, Deque): 양쪽 끝에서삽입과 삭제를허용하는자료구조
• 데크는 스택과 큐 자료 구조를 혼합한 자료 구조

• 데큐는큐의양쪽끝에서삽입과삭제가모두발생할수 있는 큐로서 스택의 성질과 큐의 성질 모두 가지고 있는 자료구조

• 따라서 데크는 스택과 큐를 동시에 구현하는데 사용

![image](https://github.com/user-attachments/assets/88669542-1b54-40b3-ba88-0d36ae111f88)

## 코드
<pre>
  <code>
from collections import deque

dq = deque()  # 빈 deque를 생성합니다.
cardNum = 4  # 초기 카드 숫자를 설정합니다.

# cardNum 값을 기반으로 deque에 요소 추가
for i in range(1, cardNum + 1):  # 1부터 cardNum까지 반복
    dq.append(i)  # deque에 요소를 추가

# deque를 처리하는 로직
while cardNum >= 1:
    if len(dq) >= 2:  # deque 크기가 최소 2개인지 확인
        first = dq.popleft()  # 왼쪽 첫 번째 요소 제거
        second = dq.popleft()  # 또 다른 왼쪽 요소 제거
        dq.append(second)  # 제거한 두 번째 요소를 다시 append
    cardNum -= 1  # cardNum 값을 1씩 감소

print(dq)  # deque의 최종 상태를 출력
  </code>
</pre>

## 결과 화면
![image](https://github.com/user-attachments/assets/eca305ad-ee89-4943-8634-d2aec8ed1235)
