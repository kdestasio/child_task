#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.5),
    on Sat Jul 20 17:49:19 2019
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.1.5'
expName = 'child_task'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/kdestasio/Temp/child_task/child_task_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "welcome_screen"
welcome_screenClock = core.Clock()
text_welcome = visual.TextStim(win=win, name='text_welcome',
    text='Please be still.\n\nPress the apostrophe key to start the task when not scanning.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "cue"
cueClock = core.Clock()
text_cue = visual.TextStim(win=win, name='text_cue',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "jitter"
jitterClock = core.Clock()
jitter_blank = visual.TextStim(win=win, name='jitter_blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "image"
imageClock = core.Clock()
display_image = visual.ImageStim(
    win=win,
    name='display_image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "response"
responseClock = core.Clock()
text_response = visual.TextStim(win=win, name='text_response',
    text='1   2   3   4   5',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fixation_cross = visual.TextStim(win=win, name='fixation_cross',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.4, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "end_screen"
end_screenClock = core.Clock()
text_end = visual.TextStim(win=win, name='text_end',
    text='Done.\n\nPlease stay still.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "welcome_screen"-------
t = 0
welcome_screenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_welcome = keyboard.Keyboard()
# keep track of which components have finished
welcome_screenComponents = [text_welcome, key_welcome]
for thisComponent in welcome_screenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "welcome_screen"-------
while continueRoutine:
    # get current time
    t = welcome_screenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_welcome* updates
    if t >= 0.0 and text_welcome.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_welcome.tStart = t  # not accounting for scr refresh
        text_welcome.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_welcome, 'tStartRefresh')  # time at next scr refresh
        text_welcome.setAutoDraw(True)
    
    # *key_welcome* updates
    if t >= 0.0 and key_welcome.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_welcome.tStart = t  # not accounting for scr refresh
        key_welcome.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_welcome, 'tStartRefresh')  # time at next scr refresh
        key_welcome.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_welcome.clock.reset)  # t=0 on next screen flip
        key_welcome.clearEvents(eventType='keyboard')
    if key_welcome.status == STARTED:
        theseKeys = key_welcome.getKeys(keyList=['apostrophe'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_welcome.keys = theseKeys.name  # just the last key pressed
            key_welcome.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcome_screenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome_screen"-------
for thisComponent in welcome_screenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_welcome.started', text_welcome.tStartRefresh)
thisExp.addData('text_welcome.stopped', text_welcome.tStopRefresh)
# check responses
if key_welcome.keys in ['', [], None]:  # No response was made
    key_welcome.keys = None
thisExp.addData('key_welcome.keys',key_welcome.keys)
if key_welcome.keys != None:  # we had a response
    thisExp.addData('key_welcome.rt', key_welcome.rt)
thisExp.addData('key_welcome.started', key_welcome.tStartRefresh)
thisExp.addData('key_welcome.stopped', key_welcome.tStopRefresh)
thisExp.nextEntry()
# the Routine "welcome_screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('image_simuli.xlsx', selection='0:61'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "cue"-------
    t = 0
    cueClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    text_cue.setText(textCue)
    # keep track of which components have finished
    cueComponents = [text_cue]
    for thisComponent in cueComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "cue"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = cueClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_cue* updates
        if t >= 0.0 and text_cue.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_cue.tStart = t  # not accounting for scr refresh
            text_cue.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_cue, 'tStartRefresh')  # time at next scr refresh
            text_cue.setAutoDraw(True)
        frameRemains = 0.0 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_cue.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            text_cue.tStop = t  # not accounting for scr refresh
            text_cue.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_cue, 'tStopRefresh')  # time at next scr refresh
            text_cue.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in cueComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "cue"-------
    for thisComponent in cueComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_cue.started', text_cue.tStartRefresh)
    trials.addData('text_cue.stopped', text_cue.tStopRefresh)
    
    # ------Prepare to start Routine "jitter"-------
    t = 0
    jitterClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    jitter_duration = random() + .5 
    thisExp.addData('jitter_duration', jitter_duration)
    # keep track of which components have finished
    jitterComponents = [jitter_blank]
    for thisComponent in jitterComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "jitter"-------
    while continueRoutine:
        # get current time
        t = jitterClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *jitter_blank* updates
        if t >= 0.0 and jitter_blank.status == NOT_STARTED:
            # keep track of start time/frame for later
            jitter_blank.tStart = t  # not accounting for scr refresh
            jitter_blank.frameNStart = frameN  # exact frame index
            win.timeOnFlip(jitter_blank, 'tStartRefresh')  # time at next scr refresh
            jitter_blank.setAutoDraw(True)
        frameRemains = 0.0 + jitter_duration- win.monitorFramePeriod * 0.75  # most of one frame period left
        if jitter_blank.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            jitter_blank.tStop = t  # not accounting for scr refresh
            jitter_blank.frameNStop = frameN  # exact frame index
            win.timeOnFlip(jitter_blank, 'tStopRefresh')  # time at next scr refresh
            jitter_blank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in jitterComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "jitter"-------
    for thisComponent in jitterComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('jitter_blank.started', jitter_blank.tStartRefresh)
    trials.addData('jitter_blank.stopped', jitter_blank.tStopRefresh)
    # the Routine "jitter" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "image"-------
    t = 0
    imageClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    display_image.setImage(imageFile)
    # keep track of which components have finished
    imageComponents = [display_image]
    for thisComponent in imageComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "image"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = imageClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *display_image* updates
        if t >= 0 and display_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            display_image.tStart = t  # not accounting for scr refresh
            display_image.frameNStart = frameN  # exact frame index
            win.timeOnFlip(display_image, 'tStartRefresh')  # time at next scr refresh
            display_image.setAutoDraw(True)
        frameRemains = 0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if display_image.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            display_image.tStop = t  # not accounting for scr refresh
            display_image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(display_image, 'tStopRefresh')  # time at next scr refresh
            display_image.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in imageComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "image"-------
    for thisComponent in imageComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('display_image.started', display_image.tStartRefresh)
    trials.addData('display_image.stopped', display_image.tStopRefresh)
    
    # ------Prepare to start Routine "response"-------
    t = 0
    responseClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    key_response = keyboard.Keyboard()
    # keep track of which components have finished
    responseComponents = [key_response, text_response]
    for thisComponent in responseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "response"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = responseClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_response* updates
        if t >= 0 and key_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_response.tStart = t  # not accounting for scr refresh
            key_response.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_response, 'tStartRefresh')  # time at next scr refresh
            key_response.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_response.clock.reset)  # t=0 on next screen flip
            key_response.clearEvents(eventType='keyboard')
        frameRemains = 0 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_response.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            key_response.tStop = t  # not accounting for scr refresh
            key_response.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_response, 'tStopRefresh')  # time at next scr refresh
            key_response.status = FINISHED
        if key_response.status == STARTED:
            theseKeys = key_response.getKeys(keyList=['5', '6', '7', '8', '9'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_response.keys = theseKeys.name  # just the last key pressed
                key_response.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # *text_response* updates
        if t >= 0.0 and text_response.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_response.tStart = t  # not accounting for scr refresh
            text_response.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_response, 'tStartRefresh')  # time at next scr refresh
            text_response.setAutoDraw(True)
        frameRemains = 0.0 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_response.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            text_response.tStop = t  # not accounting for scr refresh
            text_response.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_response, 'tStopRefresh')  # time at next scr refresh
            text_response.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in responseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "response"-------
    for thisComponent in responseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_response.keys in ['', [], None]:  # No response was made
        key_response.keys = None
    trials.addData('key_response.keys',key_response.keys)
    if key_response.keys != None:  # we had a response
        trials.addData('key_response.rt', key_response.rt)
    trials.addData('key_response.started', key_response.tStartRefresh)
    trials.addData('key_response.stopped', key_response.tStopRefresh)
    trials.addData('text_response.started', text_response.tStartRefresh)
    trials.addData('text_response.stopped', text_response.tStopRefresh)
    
    # ------Prepare to start Routine "fixation"-------
    t = 0
    fixationClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    fixation_duration = random() + .5 
    thisExp.addData('fixation_duration', fixation_duration)
    # keep track of which components have finished
    fixationComponents = [fixation_cross]
    for thisComponent in fixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "fixation"-------
    while continueRoutine:
        # get current time
        t = fixationClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_cross* updates
        if t >= 0.0 and fixation_cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_cross.tStart = t  # not accounting for scr refresh
            fixation_cross.frameNStart = frameN  # exact frame index
            win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
            fixation_cross.setAutoDraw(True)
        frameRemains = 0.0 + fixation_duration- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_cross.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            fixation_cross.tStop = t  # not accounting for scr refresh
            fixation_cross.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fixation_cross, 'tStopRefresh')  # time at next scr refresh
            fixation_cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation"-------
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('fixation_cross.started', fixation_cross.tStartRefresh)
    trials.addData('fixation_cross.stopped', fixation_cross.tStopRefresh)
    # the Routine "fixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "end_screen"-------
t = 0
end_screenClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
# keep track of which components have finished
end_screenComponents = [text_end]
for thisComponent in end_screenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end_screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = end_screenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_end* updates
    if t >= 0.0 and text_end.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_end.tStart = t  # not accounting for scr refresh
        text_end.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_end, 'tStartRefresh')  # time at next scr refresh
        text_end.setAutoDraw(True)
    frameRemains = 0.0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_end.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_end.tStop = t  # not accounting for scr refresh
        text_end.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_end, 'tStopRefresh')  # time at next scr refresh
        text_end.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_screenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end_screen"-------
for thisComponent in end_screenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_end.started', text_end.tStartRefresh)
thisExp.addData('text_end.stopped', text_end.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
