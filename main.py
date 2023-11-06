from Game import Game
from routines.Experiment import Experiment
from routines.reward_page import reward_page
from routines.test_stage import test_stage_page
from routines.fMRI_trigger import waitTrigger_page
from routines.waitSec import waitSec
import os

_thisDir = os.path.dirname(os.path.abspath(__file__))
print(_thisDir)
os.chdir(_thisDir)
exp = Experiment(_thisDir)
Game7_3_test = Game(exp, target_num=7, step=3,
                    isPlayerFirst=False, test_mode=True)  # When test_mode is True, isPlayerFirst will be ignored.
Game5_2_test = Game(exp, target_num=5, step=2,
                    isPlayerFirst=False, test_mode=True)  # When test_mode is True, isPlayerFirst will be ignored.
Game6_2 = Game(exp, target_num=6, step=2, isPlayerFirst=False)
Game21_2 = Game(exp, target_num=21, step=2, isPlayerFirst=False)
Game35_4 = Game(exp, target_num=35, step=4, isPlayerFirst=False)
Game48_3 = Game(exp, target_num=48, step=3, isPlayerFirst=False)
Game21_2 = Game(exp, target_num=21, step=2, isPlayerFirst=False)

# EPI
Treatment_0 = [Game7_3_test, Game5_2_test]
Treatment_1 = [Game6_2, Game6_2, Game6_2, Game21_2,
               Game21_2, Game21_2, Game35_4, Game35_4, Game35_4]
Treatment_2 = [Game35_4, Game35_4, Game35_4, Game21_2,
               Game21_2, Game21_2, Game6_2, Game6_2, Game6_2]
Treatment_3 = [Game48_3, Game48_3, Game48_3]
Treatment_4 = [Game21_2, Game21_2, Game21_2]

if exp.treatment == 'test':
    test_stage_page(exp)
    for trial, Game in enumerate(Treatment_0):
        Game.play(trial+1)
elif exp.treatment == '62135':
    waitTrigger_page(exp)
    waitSec(exp)
    for trial, Game in enumerate(Treatment_1):
        Game.play(trial+1)
elif exp.treatment == '35216':
    waitTrigger_page(exp)
    waitSec(exp)
    for trial, Game in enumerate(Treatment_2):
        Game.play(trial+1)
elif exp.treatment == '48':
    waitTrigger_page(exp)
    waitSec(exp)
    for trial, Game in enumerate(Treatment_3):
        Game.play(trial+1)
elif exp.treatment == '21':
    waitTrigger_page(exp)
    waitSec(exp)
    for trial, Game in enumerate(Treatment_4):
        Game.play(trial+1)

reward_page(exp)
