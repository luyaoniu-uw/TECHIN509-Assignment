import random
from turtle import Turtle, Screen
import record_game  # 載入 record_game 模組

Race = False

s = Screen()
s.setup(width=500, height=400)
bet = s.textinput(title="Make your Bet", prompt="Which turtle which win? Enter Color: ")
X = -230
Y = -100
colors = ["red", "orange", "yellow", "blue", "violet"]

turtles = []
for i in range(0, 5):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(x=X, y=-100 + 50 * i)
    turtles.append(t)

if bet:
    Race = True

while Race:
    for turtle in turtles:
        if turtle.xcor() >= 230:  # 檢查是否有烏龜過終點
            Race = False
            winning = turtle.pencolor()  # 獲勝烏龜的顏色
            if winning == bet:
                print(f"You have Won the bet on {winning} turtle! The {winning} is the winner.")
            else:
                print(f"You lose! {winning} turtle is the winner.")
            
            # 記錄比賽結果
            record_game.record_game_data(bet, winning)

        # 隨機移動每個烏龜
        distance = random.randint(0, 10)
        turtle.forward(distance)

s.exitonclick()
