import imgaug.augmenters as iaa
import numpy as np
from PIL import Image

class AugmentationManager:
    def __init__(self, config):
        # build a default pipeline if none provided
        if not config:
            self.seq = iaa.Sequential([
                iaa.Sometimes(0.5, iaa.Affine(rotate=(-5,5), shear=(-2,2))),
                iaa.Sometimes(0.4, iaa.GaussianBlur((0,1.5))),
                iaa.Sometimes(0.3, iaa.AdditiveGaussianNoise(scale=(0,0.03*255))),
            ])
        else:
            # map config to augmenters (left as exercise to extend)
            self.seq = iaa.Sequential([])

    def apply(self, pil_img: Image.Image):
        arr = np.array(pil_img)
        aug = self.seq(image=arr)
        return Image.fromarray(aug)