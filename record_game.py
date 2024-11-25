import pandas as pd


def record_game_data(user_color, winning_color, file_name="game_data.csv"):
    """Records the game data (user input color and winning color) to a CSV file

    Args:
        user_color (str): color of user choice
        winning_color (str): color of winning turtle
        file_name (str, optional): csv file name, default to "game_data.csv".
    """

    game_data = pd.DataFrame([{"User Color": user_color, "Winning Color": winning_color}])

    try:
        existing_data = pd.read_csv(file_name)
        updated_data = pd.concat([existing_data, game_data], ignore_index=True)
    except FileNotFoundError:
        updated_data = game_data

    updated_data.to_csv(file_name, index=False)