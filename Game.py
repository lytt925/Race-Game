from routines.Experiment import Experiment
from routines.new_round import new_round
from routines.play import move
from routines.win_page import win_page
from routines.fixation import fixation


class Game():
    def __init__(self, exp, target_num, step, isPlayerFirst=False, test_mode=False):
        self.exp = exp
        self.target_num = target_num
        self.current_num = 0
        self.step = step
        self.isPlayerFirst = isPlayerFirst
        self.currentPlayer = None
        self.winner = None
        self.win_count = 0
        self.test_mode = test_mode

    def reset_game(self):
        self.current_num = 0
        self.currentPlayer = None
        self.winner = None

    def play(self, trial):
        self.exp.thisExp.addData('Trial', trial)
        self.exp.thisExp.addData('Game', self.target_num)

        fixation(self.exp, duration_list=[4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8])
        new_round(self.exp, self.target_num)

        self.exp.thisExp.nextEntry()
        if self.isPlayerFirst or self.test_mode:
            self.currentPlayer = 'subject'
        else:
            self.currentPlayer = 'computer'

        step = 0
        while self.current_num < self.target_num:
            self.exp.thisExp.addData(f'Trial', trial)
            self.exp.thisExp.addData('Game', self.target_num)
            step += 1
            self.exp.thisExp.addData('step', step)
            fixation(self.exp)
            add_num = move(
                self.exp, self.currentPlayer, self.current_num, self.target_num, self.step)
            self.current_num += add_num
            self.exp.thisExp.nextEntry()
            if self.current_num == self.target_num:
                self.winner = self.currentPlayer
                break
            else:
                if not self.test_mode:
                    self.currentPlayer = 'computer' if self.currentPlayer == 'subject' else 'subject'
                else:
                    self.currentPlayer = 'subject'

        self.exp.thisExp.addData('Trial', trial)
        self.exp.thisExp.addData('Game', self.target_num)
        if self.winner == 'subject':
            self.exp.total_reward += 20
        win_page(self.exp, self.winner,  self.current_num, self.target_num)
        self.exp.thisExp.addData('accumulated_reward', self.exp.total_reward)
        self.exp.thisExp.nextEntry()
        self.reset_game()
