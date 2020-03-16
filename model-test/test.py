import argparse
from fastai.vision import load_learner, open_image

MODEL_PATH = '../model-train/'

def predict_class(image_path: str, model_path: str):
    img = open_image(image_path)
    learn = load_learner(model_path)
    print(learn.predict(img))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Predict inside/outside for a user-submitted image.')
    parser.add_argument('--image_path',
                        help='The full path to the image file.',
                        action='store',
                        type=str,
                        required=True)
    args = parser.parse_args()
    predict_class(image_path=args.image_path, model_path=MODEL_PATH)
