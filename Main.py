import subprocess
from speech_recognition import Recognizer, AudioFile
from textblob import TextBlob

# Step 1: Extract audio from video using ffmpeg
def extract_audio(video_path, audio_path):
    command = [
        'ffmpeg', '-i', video_path,
        '-q:a', '0', '-map', 'a',
        audio_path
    ]
    subprocess.run(command, check=True)

# Step 2: Transcribe audio to text
def transcribe_audio(audio_path):
    recognizer = Recognizer()
    with AudioFile(audio_path) as source:
        audio = recognizer.record(source)
    return recognizer.recognize_google(audio)

# Step 3: Analyze sentiment of the transcribed text
def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment

def interpret_sentiment(polarity, subjectivity):
    # Interpretation of Polarity
    if polarity > 0.5:
        polarity_interpretation = "Very Positive"
    elif polarity > 0:
        polarity_interpretation = "Positive"
    elif polarity == 0:
        polarity_interpretation = "Neutral"
    elif polarity > -0.5:
        polarity_interpretation = "Negative"
    else:
        polarity_interpretation = "Very Negative"

    # Interpretation of Subjectivity
    if subjectivity > 0.5:
        subjectivity_interpretation = "More Subjective (Opinion-based)"
    else:
        subjectivity_interpretation = "More Objective (Factual)"

    return polarity_interpretation, subjectivity_interpretation

def main():
    video_path = 'video1.mp4'
    audio_path = 'extracted_audio.wav'

    # Extract audio from video
    extract_audio(video_path, audio_path)

    # Transcribe audio to text
    text = transcribe_audio(audio_path)
    print(f"Transcribed Text: {text}")

    # Analyze sentiment
    sentiment = analyze_sentiment(text)
    print(f"Sentiment Analysis: {sentiment}")

    # Interpret sentiment
    polarity_interpretation, subjectivity_interpretation = interpret_sentiment(sentiment.polarity, sentiment.subjectivity)
    print(f"Polarity Interpretation: {polarity_interpretation}")
    print(f"Subjectivity Interpretation: {subjectivity_interpretation}")

if __name__ == '__main__':
    main()
    
