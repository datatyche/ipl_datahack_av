"""
Main application
"""
import logging
import pandas as pd

# logging
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

# read input
ball_by_ball = pd.read_csv('resources/train/ball_by_ball_data.csv')
key_teams = pd.read_csv('resources/train/key_teams.csv')
match_data = pd.read_csv('resources/train/match_data.csv')
player_roasters = pd.read_csv('resources/train/player_rosters.csv')

# batsmen stats
print(ball_by_ball)






