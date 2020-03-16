

# Requirements
- [ffmpeg](https://anaconda.org/conda-forge/ffmpeg)
- [youtube-dl](https://anaconda.org/conda-forge/youtube-dl)
- [fastai](https://anaconda.org/fastai/fastai)
- Optional: [jupyter](https://anaconda.org/anaconda/jupyter)

# Download multiple category videos and ids
- `cd data-fetch`
- Run the following commands:
- `bash downloadmulticategoryvideos.sh <number-of-videos-per-category> inside-categories.txt`.
- `bash downloadmulticategoryvideos.sh <number-of-videos-per-category> outside-categories.txt`.

# Generate frames from downloaded videos
-Run the following commands:
`bash generateframesfromvideos.sh inside-videos inside-frames png`
`bash generateframesfromvideos.sh outside-videos outside-frames png`

# Create folder structure for model training
-Run the following command:
`python3 data-preprocess/main.py`

# Train the model
-Run the following command:
`python3 model-train/train.py`

# Test a sample image
-Run the following command:
`python3 model-test/test.py`
