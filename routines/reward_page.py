from psychopy import core, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import random


def reward_page(exp, duration=5):

    win = exp.win
    thisExp = exp.thisExp
    routineTimer = exp.routineTimer
    defaultKeyboard = exp.defaultKeyboard
    text_reward = exp.text_reward
    text_reward.text = f"你在本段落獲得 {exp.total_reward} 法幣 \n本畫面將在 {duration} 秒後結束。"
    thisExp.addData('accumulated_reward', exp.total_reward)

    frameTolerance = 0.001
    endExpNow = False

    # --- Prepare to start Routine "reward" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    rewardComponents = [text_reward]
    for thisComponent in rewardComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1

    # --- Run Routine "reward" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < duration:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        # number of completed frames (so 0 is the first frame)
        frameN = frameN + 1
        # update/draw components on each frame

        # *text_reward* updates

        # if text_reward is starting this frame...
        if text_reward.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_reward.frameNStart = frameN  # exact frame index
            text_reward.tStart = t  # local t and not account for scr refresh
            text_reward.tStartRefresh = tThisFlipGlobal  # on global time
            # time at next scr refresh
            win.timeOnFlip(text_reward, 'tStartRefresh')
            # add timestamp to datafile
            # thisExp.timestampOnFlip(win, 'text_reward.started')
            # update status
            text_reward.status = STARTED
            text_reward.setAutoDraw(True)

        # if text_reward is active this frame...
        if text_reward.status == STARTED:
            # update params
            pass

        # if text_reward is stopping this frame...
        if text_reward.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_reward.tStartRefresh + duration-frameTolerance:
                # keep track of stop time/frame for later
                text_reward.tStop = t  # not accounting for scr refresh
                text_reward.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                # thisExp.timestampOnFlip(win, 'text_reward.stopped')
                # update status
                text_reward.status = FINISHED
                text_reward.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rewardComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # --- Ending Routine "reward" ---
    for thisComponent in rewardComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
            stoptime = win.getFutureFlipTime(clock=None)
            thisComponent.tStopRefresh = stoptime

    # --- Save timestamp
    thisExp.addData(f'reward.start', text_reward.tStartRefresh)
    thisExp.addData(f'reward.stop', text_reward.tStopRefresh)

    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-duration)
