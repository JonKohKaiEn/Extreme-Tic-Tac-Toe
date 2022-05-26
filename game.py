from ultimate_ttt.play_utils import play, play_trials
from bots import RandomBot, SimpleMCTSBot, MCTSBot

play_trials([MCTSBot, SimpleMCTSBot])