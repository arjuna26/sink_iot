# CPSC341 Final Project - Team Sink 

### project overview
in this project, we hooked a webcam up to a raspberry pi with the goal of digitzing/running OCR over captured images of handwritten notes. \
\
this involves a few scripts. first, the image has to be taken, so we have ```img_processsor.py``` which captures an image using the webcam when the user presses the button on the pi. \
\
next, this image has to be stored somewhere on the cloud so we can access it to run OCR over it. ```img_uploader.py``` is a script that listens to changes in our img/ directory and uploads new images to our Google Cloud Services bucket.
\
the captured notes will appear on our vite + react UI. 

### Project block diagram

![block](img/block_diagram.drawio.png)

---

### IoT Four Layer Description and Components

* **Sensors & Data Sources**: The camera module acts as the primary sensor, it will capture an image of notes, push button is used to trigger the image capture process, Raspberry Pi processes the image and applies OCR to extract text
* **Networking**: Extracted text data transferred via Wi-Fi from RPi to cloud service, system will connect to local network to upload files
* **Data Storage**: The original image will be processed using Textract OCR, the extracted text will be stored in something like Google Drive or OneDrive
* **Visualization**: LED indicator will confirm when the image has been processed and sent, users will receive a text document or PDF in their email/cloud storage


---

### Hardware and Other Project Components List

| Part name | Quantity | Description
| -------- | ------- | ------- |
| Raspberry Pi | 1 |  Processing unit for image capture/OCR |
| Rpi Camera Module | 1 | Captures image of notes on surface |
| Push Button | 1 | Triggers camera image capture |
| LED indicator | 1 | Lights up when image processed/sent |





---

### Team Info

Term: Spring 2025

Team Members:
* Arjuna
* Louis
* Finn

### setting up
* ssh into pi
* ```bash
  cd dev/sink_iot
  ```
* ```bash
  chmod +x run_all.sh
  ./run_all.sh
  ```
* to check what IP ui is running at:
 ```bash
  tmux a -t notes-ui
  ```
  ctrl + b then d
* click joystick button to take image

