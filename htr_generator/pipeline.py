import os
from tqdm import tqdm
from .generators.pillow_gen import PillowGenerator
from .generators.trdg_wrapper import TRDGWrapper
from .augmentations import AugmentationManager
from .utils.labelers import LabelManager


class Pipeline:
    def __init__(self, config):
        self.config = config
        # choose generator depending on availability and config preference
        gen_type = config.get('generator', 'pillow')
        if gen_type == 'trdg':
            self.generator = TRDGWrapper(config)
        else:
            self.generator = PillowGenerator(config)
        self.augmentor = AugmentationManager(config.get('augment', {}))
        self.labeler = LabelManager(config.get('labels', {}))

    def run(self, out_dir: str, count: int = 1000, mode: str = 'line'):
        os.makedirs(out_dir, exist_ok=True)
        images_dir = os.path.join(out_dir, 'images')
        os.makedirs(images_dir, exist_ok=True)
        labels = []
        for i in tqdm(range(count)):
            img, meta = self.generator.generate(mode=mode)
            img = self.augmentor.apply(img)
            name = f"img_{i:06d}.png"
            path = os.path.join(images_dir, name)
            img.save(path)
            labels.append(self.labeler.make_label(name, meta))
        # export labels
        self.labeler.export(labels, out_dir)