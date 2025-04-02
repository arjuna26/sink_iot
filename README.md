# sink_iot
CPSC341 Final Project - Team Sink

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
