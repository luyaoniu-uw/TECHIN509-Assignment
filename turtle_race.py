import random
from turtle import Turtle, Screen
import record_game  # 載入 record_game 模組

Race = False

s = Screen()
s.setup(width=500, height=400)

# 讓用戶輸入選擇的顏色
bet = s.textinput(title="Make your Bet", prompt="Which turtle will win? Enter Color: ")
X = -230
Y = -100
colors = ["red", "orange", "yellow", "blue", "violet"]

# 檢查用戶輸入的顏色是否在預設顏色列表中
if bet not in colors:
    print(f"Invalid bet! The color '{bet}' is not in the list of available colors.")
    bet = None  # 如果顏色無效，將 bet 設為 None，防止比賽開始
else:
    Race = True

# 設置烏龜
turtles = []
for i in range(0, 5):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(x=X, y=-100 + 50 * i)
    turtles.append(t)

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
