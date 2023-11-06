from psychopy import core, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import re


def win_page(exp, winner, current_num, target_num):

    win = exp.win
    thisExp = exp.thisExp
    routineTimer = exp.routineTimer
    defaultKeyboard = exp.defaultKeyboard

    duration = 4.0000
    text_round_end = exp.text_round_end
    text_current_num = exp.text_current_num
    text_target_num = exp.text_target_num
    if winner == 'computer':
        text_winner = exp.text_computer_win
    else:
        text_winner = exp.text_subject_win

    current_num_text_part = re.split(r'\d+', text_current_num.text)[0]
    target_num_text_part = re.split(r'\d+', text_target_num.text)[0]

    text_current_num.text = current_num_text_part + str(current_num)
    text_target_num.text = target_num_text_part + str(target_num)

    frameTolerance = 0.001
    endExpNow = False

    # --- Prepare to start Routine "computer_choice" ---
    continueRoutine = True
    # keep track of which components have finished
    computer_choiceComponents = [text_round_end,
                                 text_current_num, text_target_num, text_winner]

    for thisComponent in computer_choiceComponents:
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

    # --- Run Routine "computer_choice" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < duration:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        # number of completed frames (so 0 is the first frame)
        frameN = frameN + 1
        # update/draw components on each frame

        # *text_round_end* updates

        # if text_round_end is starting this frame...
        if text_round_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_round_end.frameNStart = frameN  # exact frame index
            text_round_end.tStart = t  # local t and not account for scr refresh
            text_round_end.tStartRefresh = tThisFlipGlobal  # on global time
            # time at next scr refresh
            win.timeOnFlip(text_round_end, 'tStartRefresh')
            # add timestamp to datafile
            # thisExp.timestampOnFlip(win, 'text_round_end.started')
            # update status
            text_round_end.status = STARTED
            text_round_end.setAutoDraw(True)

        # if text_round_end is active this frame...
        if text_round_end.status == STARTED:
            # update params
            pass

        # if text_round_end is stopping this frame...
        if text_round_end.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_round_end.tStartRefresh + duration-frameTolerance:
                # keep track of stop time/frame for later
                text_round_end.tStop = t  # not accounting for scr refresh
                text_round_end.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                # thisExp.timestampOnFlip(win, 'text_round_end.stopped')
                # update status
                text_round_end.status = FINISHED
                text_round_end.setAutoDraw(False)

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

        # *text_winner* updates

        # if text_winner is starting this frame...
        if text_winner.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_winner.frameNStart = frameN  # exact frame index
            text_winner.tStart = t  # local t and not account for scr refresh
            text_winner.tStartRefresh = tThisFlipGlobal  # on global time
            # time at next scr refresh
            win.timeOnFlip(text_winner, 'tStartRefresh')
            # update status
            text_winner.status = STARTED
            text_winner.setAutoDraw(True)

        # if text_winner is active this frame...
        if text_winner.status == STARTED:
            # update params
            pass

        # if text_winner is stopping this frame...
        if text_winner.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_winner.tStartRefresh + duration-frameTolerance:
                # keep track of stop time/frame for later
                text_winner.tStop = t  # not accounting for scr refresh
                text_winner.frameNStop = frameN  # exact frame index
                # update status
                text_winner.status = FINISHED
                text_winner.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in computer_choiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # --- Ending Routine "computer_choice" ---
    for thisComponent in computer_choiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
            stoptime = win.getFutureFlipTime(clock=None)
            thisComponent.tStopRefresh = stoptime

    thisExp.addData(f'win_page.start',
                    text_round_end.tStartRefresh)
    thisExp.addData(f'win_page.stop',
                    text_round_end.tStopRefresh)

    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-duration)
