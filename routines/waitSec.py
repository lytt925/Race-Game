from psychopy import core, logging, visual
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import random


def waitSec(exp, duration_list=[5]):

    win = exp.win
    thisExp = exp.thisExp
    routineTimer = exp.routineTimer
    defaultKeyboard = exp.defaultKeyboard
    text_waitSec = exp.text_waitSec

    frameTolerance = 0.001
    endExpNow = False
    duration = random.choice(duration_list)

    # --- Prepare to start Routine "fixation" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    fixationComponents = [text_waitSec]
    for thisComponent in fixationComponents:
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

    # --- Run Routine "fixation" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < duration:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        # number of completed frames (so 0 is the first frame)
        frameN = frameN + 1
        # update/draw components on each frame

        # *text_waitSec* updates

        # if text_waitSec is starting this frame...
        if text_waitSec.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_waitSec.frameNStart = frameN  # exact frame index
            text_waitSec.tStart = t  # local t and not account for scr refresh
            text_waitSec.tStartRefresh = tThisFlipGlobal  # on global time
            # time at next scr refresh
            win.timeOnFlip(text_waitSec, 'tStartRefresh')
            # add timestamp to datafile
            # thisExp.timestampOnFlip(win, 'text_waitSec.started')
            # update status
            text_waitSec.status = STARTED
            text_waitSec.setAutoDraw(True)

        # if text_waitSec is active this frame...
        if text_waitSec.status == STARTED:
            # update params
            pass

        # if text_waitSec is stopping this frame...
        if text_waitSec.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_waitSec.tStartRefresh + duration-frameTolerance:
                # keep track of stop time/frame for later
                text_waitSec.tStop = t  # not accounting for scr refresh
                text_waitSec.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                # thisExp.timestampOnFlip(win, 'text_waitSec.stopped')
                # update status
                text_waitSec.status = FINISHED
                text_waitSec.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # --- Ending Routine "fixation" ---
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
            stoptime = win.getFutureFlipTime(clock=None)
            thisComponent.tStopRefresh = stoptime

    # --- Save timestamp
    thisExp.addData(f'text_waitSec.start', text_waitSec.tStartRefresh)
    thisExp.addData(f'text_waitSec.stop', text_waitSec.tStopRefresh)

    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-duration)
