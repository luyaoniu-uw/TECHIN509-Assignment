from turtle import Turtle, Screen
from random import randint
from record_game import record_game_data  # 导入record_game_data函数

# 定义可选颜色列表
colors = ["red", "blue", "green", "yellow", "purple", "orange"]

# 创建屏幕
screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Race Game")

# 用户下注
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# 验证用户输入是否为有效颜色
if bet not in colors:
    print("Invalid input! Please enter a valid color.")
    exit()

# 创建乌龟并设置位置
all_turtles = []
start_y = -100
for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.goto(x=-230, y=start_y)
    start_y += 40
    all_turtles.append(turtle)

# 开始比赛
race_on = False
if bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        # 每只乌龟随机向前移动
        distance = randint(0, 10)
        turtle.forward(distance)

        # 检查是否有乌龟到达终点
        if turtle.xcor() > 230:
            race_on = False
            winning = turtle.pencolor()
            if winning == bet:
                print(f"You have won the bet on {winning} turtle! The {winning} is the winner!")
            else:
                print(f"You lose! {winning} turtle is the winner!")

            # 记录比赛数据
            record_game_data(bet, winning)
            break

# 关闭屏幕
screen.bye()