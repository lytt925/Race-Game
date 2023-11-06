from psychopy import core, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
from routines.Experiment import Experiment
import re
import random


def move(exp, mover, current_num, target_num, step):

    # common settings
    text_current_num = exp.text_current_num
    text_target_num = exp.text_target_num
    if target_num - current_num < step:
        step = target_num - current_num

    # for participant:
    if mover == 'subject':
        missed = False
        key_choice = exp.key_choice
        key_list = [str(i+1) for i in range(step)]
        key_choice.keys = []
        key_choice.rt = []
        _key_choice_allKeys = []

        # screen objects
        choice_duration = 2.0000
        text_turn = exp.text_subject_turn
        text_option = exp.text_subject_option
        turnComponents = [key_choice, text_turn,
                          text_current_num, text_target_num, text_option]
    # for computer
    else:
        # screen objects
        turn_duration = 2.0000
        choice_duration = 2.0000
        text_turn = exp.text_computer_turn
        text_option = exp.text_computer_option
        turnComponents = [text_turn, text_current_num,
                          text_target_num, text_option]

    choice_boxes = exp.choice_boxes[:step]
    for box in choice_boxes:
        box.color = '#000000'
    win = exp.win
    thisExp = exp.thisExp
    routineTimer = exp.routineTimer
    defaultKeyboard = exp.defaultKeyboard

    current_num_text_part = re.split(r'\d+', text_current_num.text)[0]
    text_current_num.text = current_num_text_part + str(current_num)

    target_num_text_part = re.split(r'\d+', text_target_num.text)[0]
    text_target_num.text = target_num_text_part + str(target_num)

    frameTolerance = 0.001
    endExpNow = False

    # --- Prepare to start Routine "subject_turn" ---
    continueRoutine = True
    # update component parameters for each repeat

    # keep track of which components have finished
    turnComponents += choice_boxes
    for thisComponent in turnComponents:
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

    # --- Run Routine "subject_turn" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        # number of completed frames (so 0 is the first frame)
        frameN = frameN + 1
        # update/draw components on each frame

        # *key_choice* updates
        waitOnFlip = False

        if mover == 'subject':
            # if key_choice is starting this frame...
            if key_choice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_choice.frameNStart = frameN  # exact frame index
                key_choice.tStart = t  # local t and not account for scr refresh
                key_choice.tStartRefresh = tThisFlipGlobal  # on global time
                # time at next scr refresh
                win.timeOnFlip(key_choice, 'tStartRefresh')
                # add timestamp to datafile
                # thisExp.timestampOnFlip(win, 'key_choice.started')
                # update status
                key_choice.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                # t=0 on next screen flip
                win.callOnFlip(key_choice.clock.reset)
                # clear events on next screen flip
                win.callOnFlip(key_choice.clearEvents, eventType='keyboard')
            if key_choice.status == STARTED and not waitOnFlip:
                theseKeys = key_choice.getKeys(
                    keyList=key_list, waitRelease=False)
                if t >= 60:
                    missed = True
                    key_choice.keys = str(random.randint(1, step))
                    continueRoutine = False
                _key_choice_allKeys.extend(theseKeys)
                if len(_key_choice_allKeys):
                    # just the last key pressed
                    key_choice.keys = _key_choice_allKeys[-1].name
                    key_choice.rt = _key_choice_allKeys[-1].rt
                    key_choice.duration = _key_choice_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False

        # *text_turn* updates

        # if text_turn is starting this frame...
        if text_turn.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_turn.frameNStart = frameN  # exact frame index
            text_turn.tStart = t  # local t and not account for scr refresh
            text_turn.tStartRefresh = tThisFlipGlobal  # on global time
            # time at next scr refresh
            win.timeOnFlip(text_turn, 'tStartRefresh')
            # add timestamp to datafile
            # thisExp.timestampOnFlip(win, 'text_turn.started')
            # update status
            text_turn.status = STARTED
            text_turn.setAutoDraw(True)

        # if text_turn is active this frame...
        if text_turn.status == STARTED:
            # update params
            pass

        # if text_computer_turn is stopping this frame...
        if text_turn.status == STARTED and mover == 'computer':
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_turn.tStartRefresh + turn_duration-frameTolerance:
                # keep track of stop time/frame for later
                text_turn.tStop = t  # not accounting for scr refresh
                text_turn.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                # thisExp.timestampOnFlip(win, 'text_turn.stopped')
                # update status
                text_turn.status = FINISHED
                text_turn.setAutoDraw(False)
                continueRoutine = False

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

        # *text_option* updates

        # if text_option is starting this frame...
        if text_option.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_option.frameNStart = frameN  # exact frame index
            text_option.tStart = t  # local t and not account for scr refresh
            text_option.tStartRefresh = tThisFlipGlobal  # on global time
            # time at next scr refresh
            win.timeOnFlip(text_option, 'tStartRefresh')
            # update status
            text_option.status = STARTED
            text_option.setAutoDraw(True)

        # if text_option is active this frame...
        if text_option.status == STARTED:
            # update params
            pass

        # *box* updates

        for box in choice_boxes:
            # if box is starting this frame...
            if box.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                box.frameNStart = frameN  # exact frame index
                box.tStart = t  # local t and not account for scr refresh
                box.tStartRefresh = tThisFlipGlobal  # on global time
                # time at next scr refresh
                win.timeOnFlip(box, 'tStartRefresh')
                # update status
                box.status = STARTED
                box.setAutoDraw(True)

            # if box is active this frame...
            if box.status == STARTED:
                # update params
                pass

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in turnComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # --- Ending Routine "subject_turn" ---
    for thisComponent in turnComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
            stoptime = win.getFutureFlipTime(clock=None)
            thisComponent.tStopRefresh = stoptime

    # --- Save timestamp
    thisExp.addData(f'Mover', mover)
    thisExp.addData(f'choice.start', text_turn.tStartRefresh)
    thisExp.addData(f'choice.stop', text_turn.tStopRefresh)

    # check responses
    key_num_dct = {'1': 1, '2': 2, '3': 3, '4': 4}
    if mover == 'subject':
        choice_num = key_num_dct[key_choice.keys]
    else:
        choice_num = (target_num-current_num) % (step + 1)
        if choice_num == 0:
            choice_num = random.randint(1, step)

    if mover == 'subject':
        if key_choice.keys in ['', [], None]:  # No response was made
            key_choice.keys = None
        thisExp.addData('choice', key_choice.keys)
        if key_choice.keys != None:  # we had a response
            thisExp.addData('choice.rt', key_choice.rt)
            # thisExp.addData('key_choice.duration', key_choice.duration)
        thisExp.addData('missed', missed)
    else:
        thisExp.addData('choice', choice_num)
        thisExp.addData('choice.rt', text_turn.tStopRefresh -
                        text_turn.tStartRefresh)

    # the Routine "subject_turn" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # --- Prepare to start Routine "subject_choice" ---
    continueRoutine = True
    choice_boxes[choice_num-1].color = '#FFFF00'

    # keep track of which components have finished
    choiceComponents = [
        text_turn, text_current_num, text_target_num, text_option]
    choiceComponents += choice_boxes
    for thisComponent in choiceComponents:
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

    # --- Run Routine "subject_choice" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < choice_duration:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        # number of completed frames (so 0 is the first frame)
        frameN = frameN + 1
        # update/draw components on each frame

        # *text_turn* updates

        # if text_turn is starting this frame...
        if text_turn.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_turn.frameNStart = frameN  # exact frame index
            text_turn.tStart = t  # local t and not account for scr refresh
            text_turn.tStartRefresh = tThisFlipGlobal  # on global time
            # time at next scr refresh
            win.timeOnFlip(text_turn, 'tStartRefresh')
            # add timestamp to datafile
            # thisExp.timestampOnFlip(win, 'text_turn.started')
            # update status
            text_turn.status = STARTED
            text_turn.setAutoDraw(True)

        # if text_turn is active this frame...
        if text_turn.status == STARTED:
            # update params
            pass

        # if text_turn is stopping this frame...
        if text_turn.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_turn.tStartRefresh + choice_duration-frameTolerance:
                # keep track of stop time/frame for later
                text_turn.tStop = t  # not accounting for scr refresh
                text_turn.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                # thisExp.timestampOnFlip(win, 'text_turn.stopped')
                # update status
                text_turn.status = FINISHED
                text_turn.setAutoDraw(False)

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
            if tThisFlipGlobal > text_current_num.tStartRefresh + choice_duration-frameTolerance:
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
            if tThisFlipGlobal > text_target_num.tStartRefresh + choice_duration-frameTolerance:
                # keep track of stop time/frame for later
                text_target_num.tStop = t  # not accounting for scr refresh
                text_target_num.frameNStop = frameN  # exact frame index
                # update status
                text_target_num.status = FINISHED
                text_target_num.setAutoDraw(False)

        # *text_option* updates

        # if text_option is starting this frame...
        if text_option.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_option.frameNStart = frameN  # exact frame index
            text_option.tStart = t  # local t and not account for scr refresh
            text_option.tStartRefresh = tThisFlipGlobal  # on global time
            # time at next scr refresh
            win.timeOnFlip(text_option, 'tStartRefresh')
            # update status
            text_option.status = STARTED
            text_option.setAutoDraw(True)

        # if text_option is active this frame...
        if text_option.status == STARTED:
            # update params
            pass

        # if text_option is stopping this frame...
        if text_option.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_option.tStartRefresh + choice_duration-frameTolerance:
                # keep track of stop time/frame for later
                text_option.tStop = t  # not accounting for scr refresh
                text_option.frameNStop = frameN  # exact frame index
                # update status
                text_option.status = FINISHED
                text_option.setAutoDraw(False)

        # *box* updates

        # if box is starting this frame...
        for box in choice_boxes:
            if box.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                box.frameNStart = frameN  # exact frame index
                box.tStart = t  # local t and not account for scr refresh
                box.tStartRefresh = tThisFlipGlobal  # on global time
                # time at next scr refresh
                win.timeOnFlip(box, 'tStartRefresh')
                # update status
                box.status = STARTED
                box.setAutoDraw(True)

            # if box is active this frame...
            if box.status == STARTED:
                # update params
                pass

            # if box is stopping this frame...
            if box.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > box.tStartRefresh + choice_duration-frameTolerance:
                    # keep track of stop time/frame for later
                    box.tStop = t  # not accounting for scr refresh
                    box.frameNStop = frameN  # exact frame index
                    # update status
                    box.status = FINISHED
                    box.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in choiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # --- Ending Routine "subject_choice" ---
    for thisComponent in choiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
            stoptime = win.getFutureFlipTime(clock=None)
            thisComponent.tStopRefresh = stoptime

    # --- Save timestamp
    thisExp.addData(f'show_choice.start',
                    text_turn.tStartRefresh)
    thisExp.addData(f'show_choice.stop',
                    text_turn.tStopRefresh)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-choice_duration)

    return choice_num
