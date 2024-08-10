
### `run_analysis.sh`

```bash
#!/bin/bash

# Check if ffmpeg is installed
if ! command -v ffmpeg &> /dev/null
then
    echo "ffmpeg could not be found, please install it first."
    exit
fi

# Run the Python script
python3 main.py

