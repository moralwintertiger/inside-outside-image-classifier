# Overview:

This repo contains an inside-versus-outside image classifier as well as the code used to build the classifier and a script to run inference on single images from the command line. 

-All images were collected from youtube videos (via youtube-8m). 

-Inside versus outside videos were collected based on associated category tags (for example 'skiing' category videos were collected as 'outside'). A full list of inside versus outside categories can be found in inside-categories.txt and outside-categories.txt. 

-For each image, .5 frames per second were collected as pngs. 

-3500 images per class were used to fine-tune the Resnet34 convnet, provided by FastAI and Pytorch. Model was trained for 5 epochs, unfrozen, and trained for one additional epoch, with learning rate determined by the lr_find method. 

-Fine-tuned model is included in this repo. Final model accuracy on an image validation set is ~98.4%.

# Requirements
- [ffmpeg](https://anaconda.org/conda-forge/ffmpeg)
- [youtube-dl](https://anaconda.org/conda-forge/youtube-dl)
- [fastai](https://anaconda.org/fastai/fastai)
- Optional: [jupyter](https://anaconda.org/anaconda/jupyter)

# Download multiple category videos and ids
- `cd data-fetch`
- Run the following commands:

- `bash downloadmulticategoryvideos.sh <number-of-videos-per-category> <output-directory> inside-categories.txt`.

- `bash downloadmulticategoryvideos.sh <number-of-videos-per-category> <output_directory> outside-categories.txt`.

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

`python3 model-test/test.py --image_path`
