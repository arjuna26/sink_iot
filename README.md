# CPSC341 Final Project - Team Sink 

### project overview
in this project, we hooked a webcam up to a raspberry pi with the goal of digitzing/running OCR over captured images of handwritten notes. \
\
this involves a few scripts. first, the image has to be taken, so we have ```img_processsor.py``` which captures an image using the webcam when the user presses the button on the pi. \
\
next, this image has to be stored somewhere on the cloud so we can access it to run OCR over it. ```img_uploader.py``` is a script that listens to changes in our img/ directory and uploads new images to our Google Cloud Services bucket.

**write about OCR script here**

### setting up
* ssh into pi
* ```bash
  cd dev/sink_iot
  ```
* ```bash
  tmux new-session -s processor
  python img_processor.py
  ```
  ctrl + b then d
* ```bash
  tmux new-session -s uploader
  source venv/bin/activate
  python img_uploader.py
  ```
  ctrl + b then d
* click joystick button to take image
