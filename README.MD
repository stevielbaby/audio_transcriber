
# Audio File Converter and Transcriber

## Overview

This Python script converts audio files from WMA, M4A, and MP3 formats to MP3 and then transcribes them using the Whisper ASR (Automatic Speech Recognition) model. The script is designed to process multiple audio files in a specified directory and save the transcriptions as text files.

## Features

- **Batch Processing**: Converts and transcribes multiple audio files in a folder.
- **Audio Conversion**: Converts WMA and M4A files to MP3 using FFmpeg.
- **Transcription**: Transcribes the audio using the Whisper ASR model.
- **Error Handling**: Checks for the existence of the source directory, audio files, FFmpeg, and the Whisper model.

## Requirements

- Python 3.x
- FFmpeg
- Whisper ASR model

## Installation

1. **Clone the Repository**:  
   ```
   git clone https://github.com/stevielbaby/audio_transcriber.git
   ```

2. **Navigate to the Directory**:  
   ```
   cd audio_transcriber
   ```

3. **Install FFmpeg**:  
   Follow the installation instructions for your operating system from the [official FFmpeg website](https://ffmpeg.org/download.html).

4. **Install Whisper**:  
   ```
   pip install whisper
   ```

## Usage

1. **Set the Source Directory**:  
   Update the `folder_path` variable in the script with the path to the directory containing the audio files you want to convert and transcribe.

2. **Run the Script**:  
   ```
   python transcriber.py
   ```

3. **Enter the Name Schema**:  
   When prompted, enter the name schema for the output transcription files.

4. **Check the Output**:  
   Transcriptions will be saved in the `transcriptions` folder, and converted MP3 files will be saved in the `mp3` folder.

## Contributing

Feel free to fork the project, make changes, and submit pull requests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Feel free to modify this README to better suit your project's specific needs.