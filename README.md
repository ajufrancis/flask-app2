# Data Processing Flask Application

A Flask-based web application that allows users to upload data files (text, image, or audio), display them, preprocess them, and augment them. This application demonstrates basic data handling and processing techniques for different file types.

## Features

- **File Upload:** Upload text (.txt), image (.png, .jpg, etc.), or audio (.wav, .mp3) files.
- **Display:** View the uploaded file in the browser.
  - Text files are displayed in plain text.
  - Images are rendered in the browser.
  - Audio files can be played using an HTML audio player.

## Preprocessing:
- **Text:** Convert text to lowercase.
- **Images:** Convert images to grayscale.
- **Audio:** Normalize audio volume.

## Augmentation:
- **Text:** Append a predefined sentence.
- **Images:** Rotate images by 45 degrees.
- **Audio:** Speed up audio playback.

## Prerequisites

- Python 3.x
- pip (Python package manager)
- FFmpeg (for audio processing)
  - Download and install from FFmpeg Official Website.
 
## Installation

1. Clone the Repository
   ```
       git clone https://github.com/yourusername/your-repo-name.git
       cd your-repo-name
   ```
2. Install Dependencies
   ```
     pip install -r requirements.txt
   ```
3. Run the Application
   ```
     python app.py
   ```
4. Access the Web Interface
   ```
    http://localhost:5000
   ```

## Application Workflow

- **Upload a File:** Click on "Choose File" and select a text, image, or audio file to upload.
- **Display the File:** After uploading, the file will be displayed appropriately.
- **Preprocess the File:** Click the "Preprocess" button to apply preprocessing.
- **Augment the File:** Click the "Augment" button to apply augmentation.





