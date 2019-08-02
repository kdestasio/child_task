# Child Task

Programmed for the Social and Affective Neuroscience Lab by Krista DeStasio.  

## Introduction

An event-related image rating task for use in an fMRI scanner.  

Basic parameters:  

- Conditions: picture of own child, picture of other reward, neutral picture. 
- Trial structure: cue indicating reward type (~4s), jitter (~1s), picture (5s), 1-5 rating (4s), inter trial interval (~1s) => 14s/trial.  
- Duration: 20 trials/condition = 7.5 minutes x 2 runs.  

## Tutorial

1. Launch the PsychoPy Builder.
2. Open the file `child_task.psyexp`.
3. Click the icon at the top of the Builder window that looks like a running person.
4. If running outside the scanner, use the apostrophe key to start the task ( this key `'`)

### Stimuli

The images used during the task should be stored in `images/`.  

The `images/` subfolders are currently named:  

- `myBaby/`  
- `notBaby/`  
- `otherBaby/`  

Each of these subfolders contains 20 images of the format {subfoldername}{number}.jpg  

For example, `images/myBaby/myBaby1.jpg` and `images/notBaby/notBaby19.jpg`  

The folder and file names may be changed to suit the user. If they are changed, the changes must be reflected in the file `image_stimuli.xlsx`, in the first column titled `imageFile`.  

For example, if the user wants to rename the folder `notBaby` to `neutral`, the corresponding change in the `image_stimuli.xlsx` file would be made for each entry from `images/notBaby/notBaby1.jpg` to `images/neutral/notBaby1.jpg`.  

The same principle applies when changing image file names, e.g. from `images/notBaby/notBaby1.jpg` to `images/notBaby/notBaby_01.jpg`.  






## Developer documentation

Developed with PsychoPy v3.1.5

In depth documentation: https://uoregonctn.atlassian.net/wiki/spaces/SW/pages/210239549/Child+Task+-+PsychoPy. 