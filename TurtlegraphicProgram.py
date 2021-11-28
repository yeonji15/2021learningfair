import turtle

print("1. 원 2. 별 3. 스파이럴 4. 정다각형")
n = int(input("터틀 그래픽으로 그리고 싶은 도형의 번호를 선택하세요: "))
c = input("원하는 색을 영어로 입력하세요: ")

t = turtle.Turtle()
t.color(c)
t.shape("turtle")
t.shapesize(2, 2)

if n==1:
    t.circle(150)
    
elif n==2:
    i = 0
    while i < 5:
        t.forward(300)
        t.right(144)
        i = i + 1
        
elif n==3:
    t.speed(0)
    length = 10
    while length < 500:
        t.forward(length)
        t.right(89)
        length += 5
        
elif n==4:
    s = int(turtle.textinput("정다각형", "몇 각형을 원하시나요?"))
    for i in range(s):
        t.forward(150)
        t.left(360/s)
        
else:
    print("잘못 입력하셨습니다.")

