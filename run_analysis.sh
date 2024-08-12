#!/bin/bash

# Update package lists
sudo apt-get update

# Check if python3-venv is installed
if ! dpkg -l | grep -q python3-venv; then
    echo "python3-venv could not be found, installing..."
    sudo apt-get install -y python3-venv
else
    echo "python3-venv is already installed."
fi

# Create a virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "Virtual environment created."
fi

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip inside the virtual environment
pip install --upgrade pip

# Install necessary Python packages inside the virtual environment
pip install SpeechRecognition textblob

# Check if ffmpeg is installed
if ! command -v ffmpeg &> /dev/null
then
    echo "ffmpeg could not be found, installing..."
    sudo apt-get install -y ffmpeg
else
    echo "ffmpeg is already installed."
fi

echo "Environment setup complete."

# Check if a video file was provided as an argument
if [ -z "$1" ]
then
    echo "Usage: $0 <video_file>"
    exit 1
fi

# Run the Python script with the provided video file name
python3 Main.py "$1"

# Deactivate the virtual environment
deactivate
