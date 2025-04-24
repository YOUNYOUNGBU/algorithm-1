# 스택으로 수열 만들기 실습
## 코드
<pre>
<code>
    def push(item):
    global top
    stack.append(item)
    top += 1 #top = top + 1

    def pop():
    global top
    if len(stack) != 0:
        #item = stack.pop(-1)
        item = stack.pop(top)
        top -= 1 #top = top - 1
        return item

stack = []     
top = -1 # -1, 0 , 1, 2, 1
if __name__ == "__main__":
    push("apple") #apple 삽입
    push("orange") #orange 삽입
    push("cherry") #cherry 삽입
    print("apple, orange, cherry를 push후=\t", end = "") 
    print(stack, "\t <- top") #['apple', 'orange', 'cherry'] 출력
    print("TOP 항목 = " , end = '') 
    topvalue = pop() #cherry 삭제
    print("topvalue=", topvalue)
    push("pear") #pear 추가
    print("pear추가후 top=", end = "")
    topval2 = pop() #pear 삭제
    print("topval2=" , topval2)
</code>
</pre>

1. 스택으로 수열만들기 과제 방법 1
## 코드
<pre>
    <code>
        def stack_sequence(target_sequence):
    stack = []
    operations = []
    current = 1

    for num in target_sequence:
        # 스택에 num이 들어올 때까지 push 수행
        while current <= num:
            stack.append(current)
            operations.append("+")  # push 연산
            current = current + 1
        
        # 스택 최상단이 num과 같으면 pop 수행
        if stack[-1] == num:
            stack.pop()
            operations.append("-")  # pop 연산
        else:
            # 스택으로 해당 수열을 만들 수 없는 경우
            return "NO"

    return "\n".join(operations)
    </code>
</pre>

target = [4,3,6,8,7,5,2,1]  # 목표 수열
result = stack_sequence(target)

print(result)

2. 스택으로 수열만들기 방법 2
## 코드
<pre>
    <code>
        target = [4, 3, 6, 8, 7, 5, 2, 1] # 목표 수열

def stack_sequence(target_sequence): # 스택 수열을 생성하고 출력하는 함수
    stack = []  # 스택 리스트
    operations = []  # 연산 기록을 저장할 리스트
    current = 1  # 현재 숫자 1부터 시작

    for num in target_sequence:
        if num >= current:  # 목표 숫자가 현재 숫자보다 크거나 같은 경우
            while num >= current:  # 현재 숫자가 목표 숫자에 도달할 때까지 반복
                stack.append(current)  # 현재 숫자를 스택에 추가
                current += 1  # 숫자를 하나 증가
                operations.append("+")  # "-" 넣기

            stack.pop()  # 목표 숫자에 도달했으므로 스택에서 제거(pop)
            operations.append("-")  # pop("-") 연산을 기록
        else: # 스택의 마지막 값이 목표 숫자보다 큰 경우
            if stack[-1] > num:  
                print("NO")  # 수열 생성이 불가능하므로 "NO" 출력
                return # 함수 종료
            stack.pop()  # 스택에서 숫자 제거(pop)
            operations.append("-")  # "-" 넣기
    
    return operations  # 연산 기록 반환

result = stack_sequence(target)

if result:  # 결과가 존재할 경우
    print("\n".join(result))  # 결과를 줄바꿈하여 출력
</code>
</pre>


느낀점: 파이썬은 공부를 많이 안해서 마지막 코드에 ";"를 안붙인다거나 if문이나 for문을 사용할 때 중괄호를 넣지 않는다는 점이 자바랑 많이 달라서 헷갈렸다.
막히는 부분이 많아서 챗GPT의 힘을 빌렸지만 조금 만 더 공부하면 혼자 짤 수 있을 것같다.
요즘 챗GPT의 도움을 많이 받는다. 식당을 갈 때나 드라마에서 내가 좋아하는 부분을 다시 보고 싶을 때 물어보면 GPT가 다알려준다.
엄청 신기하다.



