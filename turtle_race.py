# code credit: https://www.geeksforgeeks.org/turtle-race-game-using-python-turtle-graphics-library/

import random
from turtle import Turtle, Screen
from record_game import record_game_data  # 导入 record_game_data 函数

Race = False

# 创建游戏屏幕
s = Screen()
s.setup(width=500, height=400)

# 获取用户输入的投注
bet = s.textinput(title="Make your Bet", prompt="Which turtle will win? Enter Color: ")
X = -230
Y = -100
colors = ["red", "orange", "yellow", "blue", "violet"]

# 验证用户输入的颜色是否有效
if bet not in colors:
    print("Invalid color entered. Please choose a valid color from the list.")
    Race = False  # 结束比赛，防止继续
else:
    Race = True  # 如果输入有效，继续比赛

turtles = []
for i in range(0, 5):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(x=X, y=-100 + 50 * i)
    turtles.append(t)

while Race:
    # 每一轮比赛
    for turtle in turtles:
        # 检查是否有乌龟到达终点
        if turtle.xcor() >= 230:
            Race = False
            winning = turtle.pencolor()  # 获胜的乌龟颜色
            if winning == bet:  # 判断用户是否赢得了投注
                print(f"You have Won the bet on {winning} turtle! The {winning} is the winner")
            else:
                print(f"You lose! {winning} turtle is the winner")
            
            # 调用 record_game_data 函数记录比赛数据
            record_game_data(bet, winning)

        # 每次乌龟随机前进的距离
        distance = random.randint(0, 10)
        turtle.forward(distance)

# 点击屏幕关闭
s.exitonclick()
