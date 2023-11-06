# --- Import packages ---
from psychopy.hardware import keyboard
import psychopy.iohub as io
import sys  # to get file system encoding
import os  # handy system and path functions
from numpy.random import random, randint, normal, shuffle, choice as randchoice
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
from psychopy.tools import environmenttools
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'


class Experiment():
    def __init__(self, directory) -> None:
        # Ensure that relative paths start from the same directory as this script
        # Store info about the experiment session
        psychopyVersion = '2023.1.3'
        expName = 'Race Game'  # from the Builder filename that created this script
        expInfo = {
            'participant': data.getDateStr(format="%y%m%d%H"),
            'treatment': ['test', '62135', '35216', '48', '21']
        }
        # --- Show participant info dialog --
        dlg = gui.DlgFromDict(dictionary=expInfo,
                              sortKeys=False, title=expName)
        if dlg.OK == False:
            core.quit()  # user pressed cancel
        expInfo['date'] = data.getDateStr(
            format="%Y-%m-%d-%H%M")  # add a simple timestamp
        expInfo['expName'] = expName
        expInfo['psychopyVersion'] = psychopyVersion

        self.treatment = expInfo['treatment']
        # Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
        self.filename = directory + os.sep + \
            u'data/%s_%s_%s_%s' % (expInfo['participant'], 'EP'+expInfo['treatment'],
                                   expName, expInfo['date'])

        # An ExperimentHandler isn't essential but helps with data saving
        self.thisExp = data.ExperimentHandler(name=expName, version='',
                                              extraInfo=expInfo, runtimeInfo=None,
                                              originPath='C:\\Users\\lytt\\Desktop\\yuping\\text.py',
                                              savePickle=True, saveWideText=True,
                                              dataFileName=self.filename)

        self.total_reward = 0
        # save a log file for detail verbose info
        self.logFile = logging.LogFile(self.filename+'.log', level=logging.EXP)
        # this outputs to the screen, not a file
        logging.console.setLevel(logging.WARNING)

        self.endExpNow = False  # flag for 'escape' or other condition => quit the exp
        self.frameTolerance = 0.001  # how close to onset before 'same' frame

        # Start Code - component code to be run after the window creation

        # --- Setup the Window ---
        win_height = 1024
        win_width = 768
        zh_tw_font = 'LiHei Pro'
        #zh_tw_font = 'Microsoft JhengHei'
        self.win = visual.Window(
            size=[win_height, win_width], fullscr=True, screen=0,
            winType='pyglet', allowStencil=True,
            monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height')
        self.win.mouseVisible = False
        # store frame rate of monitor if we can measure it
        expInfo['frameRate'] = self.win.getActualFrameRate()
        if expInfo['frameRate'] != None:
            frameDur = 1.0 / round(expInfo['frameRate'])
        else:
            frameDur = 1.0 / 60.0  # could not measure, so guess
        # --- Setup input devices ---
        ioConfig = {}

        # Setup iohub keyboard
        ioConfig['Keyboard'] = dict(use_keymap='psychopy')

        ioSession = '1'
        if 'session' in expInfo:
            ioSession = str(expInfo['session'])
        ioServer = io.launchHubServer(window=self.win, **ioConfig)
        eyetracker = None

        # create a default keyboard (e.g. to check for escape)
        self.defaultKeyboard = keyboard.Keyboard(backend='iohub')

        # Create some handy timers
        self.globalClock = core.Clock()  # to track the time since experiment started
        # to track time remaining of each (possibly non-slip) routine
        self.routineTimer = core.Clock()

        # --- Initialize components for Routine "new_round" ---
        self.text_test_stage = visual.TextStim(win=self.win, name='text_test_stage',
                                               text='本階段為測試階段\n\n本階段不會計算報酬',
                                               font=zh_tw_font,
                                               units='pix', pos=(0, 0), height=60.0, wrapWidth=1920.0, ori=0.0,
                                               color='white', colorSpace='rgb', opacity=None,
                                               languageStyle='LTR',
                                               depth=0.0)
        self.text_waitTrigger = visual.TextStim(win=self.win, name='text_waitTrigger',
                                                text='+',
                                                font='Open Sans',
                                                pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
                                                color='white', colorSpace='rgb', opacity=None,
                                                languageStyle='LTR',
                                                depth=0.0)
        self.text_waitSec = visual.TextStim(win=self.win, name='text_waitTen',
                                            text='+',
                                            font='Open Sans',
                                            pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
                                            color='yellow', colorSpace='rgb', opacity=None,
                                            languageStyle='LTR',
                                            depth=0.0)

        self.key_choice = keyboard.Keyboard()

        self.text_new_round = visual.TextStim(win=self.win, name='text_new_round',
                                              text='新回合開始，目標數字 6',
                                              font=zh_tw_font,
                                              units='height', pos=(0, 0.32), height=0.08, wrapWidth=1920, ori=0.0, bold=True,
                                              color='white', colorSpace='rgb', opacity=None, anchorHoriz='center',
                                              languageStyle='LTR',
                                              depth=-1.0)

        self.text_current_num = visual.TextStim(win=self.win, name='text_current_num',
                                                text='當前數字 \n0',
                                                font=zh_tw_font,
                                                units='height', pos=(-0.28, 0.04), height=0.08, wrapWidth=1920.0, ori=0.0,
                                                color='white', colorSpace='rgb', opacity=None, bold=True,
                                                languageStyle='LTR',
                                                depth=-2.0)

        self.text_target_num = visual.TextStim(win=self.win, name='text_target_num',
                                               text='目標數字 \n6',
                                               font=zh_tw_font,
                                               units='height', pos=(0.28, 0.04), height=0.08, wrapWidth=1920.0, ori=0.0,
                                               color='white', colorSpace='rgb', opacity=None, bold=True,
                                               languageStyle='LTR',
                                               depth=-3.0)

        self.text_subject_turn = visual.TextStim(win=self.win, name='text_subject_turn',
                                                 text='現在輪到「您」做選擇',
                                                 font=zh_tw_font,
                                                 units='height', pos=(0, 0.35), height=0.08, wrapWidth=1920.0, ori=0.0,
                                                 color='white', colorSpace='rgb', opacity=None, bold=True,
                                                 languageStyle='LTR',
                                                 depth=-1.0)

        self.text_computer_turn = visual.TextStim(win=self.win, name='text_computer_turn',
                                                  text='現在輪到「電腦」做選擇',
                                                  font=zh_tw_font,
                                                  units='height', pos=(0, 0.35), height=0.08, wrapWidth=1920.0, ori=0.0,
                                                  color='white', colorSpace='rgb', opacity=None, bold=True,
                                                  languageStyle='LTR',
                                                  depth=-1.0)

        self.text_round_end = visual.TextStim(win=self.win, name='text_round_end',
                                              text='回合結束',
                                              font=zh_tw_font,
                                              units='height', pos=(0, 0.35), height=0.08, wrapWidth=1920.0, ori=0.0,
                                              color='white', colorSpace='rgb', opacity=None, bold=True,
                                              languageStyle='LTR',
                                              depth=-1.0)

        self.text_subject_win = visual.TextStim(win=self.win, name='text_subject_win',
                                                text='本回合由您獲勝',
                                                font=zh_tw_font,
                                                units='height', pos=(0, -0.23), height=0.08, wrapWidth=1920.0, ori=0.0,
                                                color='white', colorSpace='rgb', opacity=None, bold=True,
                                                languageStyle='LTR',
                                                depth=-1.0)

        self.text_computer_win = visual.TextStim(win=self.win, name='text_computer_win',
                                                 text='本回合由電腦獲勝',
                                                 font=zh_tw_font,
                                                 units='height', pos=(0, -0.23), height=0.08, wrapWidth=1920.0, ori=0.0,
                                                 color='white', colorSpace='rgb', opacity=None, bold=True,
                                                 languageStyle='LTR',
                                                 depth=-1.0)

        self.text_computer_option = visual.TextStim(win=self.win, name='text_computer_option',
                                                    text='電腦的選擇', bold=True,
                                                    font=zh_tw_font,
                                                    units='height', pos=(-0.18, -0.23), height=0.08, wrapWidth=1920.0, ori=0.0,
                                                    color='white', colorSpace='rgb', opacity=None,
                                                    languageStyle='LTR',
                                                    depth=-4.0)

        self.text_subject_option = visual.TextStim(win=self.win, name='text_subject_option',
                                                   text='您的選擇', bold=True,
                                                   font=zh_tw_font,
                                                   units='height', pos=(-0.18, -0.23), height=0.08, wrapWidth=1920.0, ori=0.0,
                                                   color='white', colorSpace='rgb', opacity=None,
                                                   languageStyle='LTR',
                                                   depth=-4.0)

        self.choice1_box = visual.TextBox2(
            self.win, text='1', placeholder='Type here...', font=zh_tw_font,
            pos=(0.10, -0.24), units='height', letterHeight=0.07,
            size=(0.1, 0.1), borderWidth=0.0,
            color="#000000", colorSpace='rgb',
            opacity=None,
            bold=True, italic=False,
            lineSpacing=1.0, speechPoint=None,
            padding=0.0, alignment='center',
            anchor='center', overflow='visible',
            fillColor="#BFBFBF", borderColor=None,
            flipHoriz=False, flipVert=False, languageStyle='LTR',
            editable=False,
            name='choice1_box',
            depth=-5, autoLog=True,
        )
        self.choice2_box = visual.TextBox2(
            self.win, text='2', placeholder='Type here...', font=zh_tw_font,
            pos=(0.215, -0.24), units='height', letterHeight=0.07,
            size=(0.1, 0.1), borderWidth=0.0,
            color="#000000", colorSpace='rgb',
            opacity=None,
            bold=True, italic=False,
            lineSpacing=1.0, speechPoint=None,
            padding=0.0, alignment='center',
            anchor='center', overflow='visible',
            fillColor="#BFBFBF", borderColor=None,
            flipHoriz=False, flipVert=False, languageStyle='LTR',
            editable=False,
            name='choice2_box',
            depth=-6, autoLog=True,
        )
        self.choice3_box = visual.TextBox2(
            self.win, text='3', placeholder='Type here...', font=zh_tw_font,
            pos=(0.33, -0.24), units='height', letterHeight=0.070,
            size=(0.1, 0.1), borderWidth=0.0,
            color="#000000", colorSpace='rgb',
            opacity=None,
            bold=True, italic=False,
            lineSpacing=1.0, speechPoint=None,
            padding=0.0, alignment='center',
            anchor='center', overflow='visible',
            fillColor="#BFBFBF", borderColor=None,
            flipHoriz=False, flipVert=False, languageStyle='LTR',
            editable=False,
            name='choice2_box',
            depth=-6, autoLog=True,
        )
        self.choice4_box = visual.TextBox2(
            self.win, text='4', placeholder='Type here...', font=zh_tw_font,
            pos=(0.445, -0.24), units='height', letterHeight=0.07,
            size=(0.1, 0.1), borderWidth=0.0,
            color="#000000", colorSpace='rgb',
            opacity=None,
            bold=True, italic=False,
            lineSpacing=1.0, speechPoint=None,
            padding=0.0, alignment='center',
            anchor='center', overflow='visible',
            fillColor="#BFBFBF", borderColor=None,
            flipHoriz=False, flipVert=False, languageStyle='LTR',
            editable=False,
            name='choice2_box',
            depth=-6, autoLog=True,
        )
        self.choice_boxes = [self.choice1_box,
                             self.choice2_box, self.choice3_box, self.choice4_box]

        self.text_fixation = visual.TextStim(win=self.win, name='text_fixation',
                                             text='+',
                                             font='Open Sans',
                                             pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
                                             color='white', colorSpace='rgb', opacity=None,
                                             languageStyle='LTR',
                                             depth=0.0
                                             )
        self.text_reward = visual.TextStim(win=self.win, name='text_reward',
                                           text='',
                                           font=zh_tw_font,
                                           pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0,
                                           color='white', colorSpace='rgb', opacity=None,
                                           languageStyle='LTR',
                                           depth=0.0
                                           )

    def end_exp(self):
        # --- End experiment ---
        # Flip one final time so any remaining win.callOnFlip()
        # and win.timeOnFlip() tasks get executed before quitting
        self.win.flip()

        # these shouldn't be strictly necessary (should auto-save)
        self.thisExp.saveAsWideText(self.filename+'.csv', delim='auto')
        self.thisExp.saveAsPickle(self.filename)
        logging.flush()
        self.thisExp.abort()  # or data files will save again on exit
        self.win.close()
        core.quit()
