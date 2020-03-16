from fastai.vision import get_transforms, ImageDataBunch, cnn_learner, models
from fastai.metrics import error_rate

DATA_DIRECTORY = '../data_bunch'


def fine_tune_convnet(path: str):
    """
    Path must be in the format of a FastAI data bunch, ie Train/Test/Valid dirs
    and then one subdirectory per class in each of those dirs.
    """

    tfms = get_transforms(do_flip=False)
    data = ImageDataBunch.from_folder(path, ds_tfms=tfms, size=64)
    learn = cnn_learner(data, models.resnet34, metrics=error_rate)
    learn.fit_one_cycle(5)
    learn.save('stage-1')
    learn.unfreeze()
    learn.fit_one_cycle(1, max_lr=slice(1e-6, 1e-3))
    learn.save('stage-2')
    learn.export(file="two-stage-model.pkl")


if __name__ == '__main__':
    fine_tune_convnet(path=DATA_DIRECTORY)
