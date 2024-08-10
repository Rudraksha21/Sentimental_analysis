# Sentimental_analysis
Sentimental analysis of a Video 
Code will extract the audio from the given video and convert audio to text and perform analysis on the text for certain words and it will give result as negative, positive or neutral.

# Video Sentiment Analysis

This project extracts audio from a video file, transcribes the audio to text, and analyzes the sentiment of the transcribed text.

## Features

- **Audio Extraction:** Extracts audio from a video file using `ffmpeg`.
- **Speech Recognition:** Converts audio to text using `speech_recognition`.
- **Sentiment Analysis:** Analyzes the sentiment (polarity and subjectivity) of the transcribed text using `TextBlob`.

## Requirements

- Python 3.x
- `ffmpeg` (for extracting audio)
- Python packages:
  - `speech_recognition`
  - `textblob`

## Installation

1.sudo apt-get install ffmpeg


2. Clone this repository:
   ```bash
   git clone https://github.com/your-username/video-sentiment-analysis.git
   cd video-sentiment-analysis

3../run_analysis.sh

#Mathematica Example
Transcribed Text: Hello, welcome to the video sentiment analysis.
Sentiment Analysis: Sentiment(polarity=0.5, subjectivity=0.6)
Polarity Interpretation: Positive
Subjectivity Interpretation: More Subjective (Opinion-based)
