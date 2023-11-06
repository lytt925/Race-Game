from psychopy import core, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import re


def new_round(exp, target_num, duration=4.000000):

    text_new_round = exp.text_new_round
    text_current_num = exp.text_current_num
    text_target_num = exp.text_target_num

    current_num_text_part = re.split(r'\d+', text_current_num.text)[0]
    target_num_text_part = re.split(r'\d+', text_target_num.text)[0]
    newround_num_text_part = re.split(r'\d+', text_new_round.text)[0]

    text_current_num.text = current_num_text_part + str(0)
    text_target_num.text = target_num_text_part + str(target_num)
    text_new_round.text = newround_num_text_part + str(target_num)

    win = exp.win
    thisExp = exp.thisExp
    routineTimer = exp.routineTimer
    defaultKeyboard = exp.defaultKeyboard

    frameTolerance = 0.001
    endExpNow = False

    # --- Prepare to start Routine "new_round" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    new_roundComponents = [text_new_round, text_current_num, text_target_num]
    for thisComponent in new_roundComponents:
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

    # --- Run Routine "new_round" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < duration:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        # number of completed frames (so 0 is the first frame)
        frameN = frameN + 1
        # update/draw components on each frame

        # *text_new_round* updates

        # if text_new_round is starting this frame...
        if text_new_round.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_new_round.frameNStart = frameN  # exact frame index
            text_new_round.tStart = t  # local t and not account for scr refresh
            text_new_round.tStartRefresh = tThisFlipGlobal  # on global time
            # time at next scr refresh
            win.timeOnFlip(text_new_round, 'tStartRefresh')
            # add timestamp to datafile
            # thisExp.timestampOnFlip(win, 'text_new_round.started')
            # update status
            text_new_round.status = STARTED
            text_new_round.setAutoDraw(True)

        # if text_new_round is active this frame...
        if text_new_round.status == STARTED:
            # update params
            pass

        # if text_new_round is stopping this frame...
        if text_new_round.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_new_round.tStartRefresh + duration-frameTolerance:
                # keep track of stop time/frame for later
                text_new_round.tStop = t  # not accounting for scr refresh
                text_new_round.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_new_round.stopped')
                # update status
                text_new_round.status = FINISHED
                text_new_round.setAutoDraw(False)

        # *text_current_num* updates

        # if text_current_num is starting this frame...
        if text_current_num.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_current_num.frameNStart = frameN  # exact frame index
            text_current_num.tStart = t  # local t and not account for scr refresh
            text_current_num.tStartRefresh = tThisFlipGlobal  # on global time
            # time at next scr refresh
            win.timeOnFlip(text_current_num, 'tStartRefresh')
            # update status
            text_current_num.status = STARTED
            text_current_num.setAutoDraw(True)

        # if text_current_num is active this frame...
        if text_current_num.status == STARTED:
            # update params
            pass

        # if text_current_num is stopping this frame...
        if text_current_num.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_current_num.tStartRefresh + duration-frameTolerance:
                # keep track of stop time/frame for later
                text_current_num.tStop = t  # not accounting for scr refresh
                text_current_num.frameNStop = frameN  # exact frame index
                # update status
                text_current_num.status = FINISHED
                text_current_num.setAutoDraw(False)

        # *text_target_num* updates

        # if text_target_num is starting this frame...
        if text_target_num.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_target_num.frameNStart = frameN  # exact frame index
            text_target_num.tStart = t  # local t and not account for scr refresh
            text_target_num.tStartRefresh = tThisFlipGlobal  # on global time
            # time at next scr refresh
            win.timeOnFlip(text_target_num, 'tStartRefresh')
            # update status
            text_target_num.status = STARTED
            text_target_num.setAutoDraw(True)

        # if text_target_num is active this frame...
        if text_target_num.status == STARTED:
            # update params
            pass

        # if text_target_num is stopping this frame...
        if text_target_num.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_target_num.tStartRefresh + duration-frameTolerance:
                # keep track of stop time/frame for later
                text_target_num.tStop = t  # not accounting for scr refresh
                text_target_num.frameNStop = frameN  # exact frame index
                # update status
                text_target_num.status = FINISHED
                text_target_num.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in new_roundComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # --- Ending Routine "new_round" ---
    for thisComponent in new_roundComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
            stoptime = win.getFutureFlipTime(clock=None)
            thisComponent.tStopRefresh = stoptime

    thisExp.addData('new_round.start', text_new_round.tStartRefresh)
    thisExp.addData('new_round.stop', text_new_round.tStopRefresh)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-duration)
