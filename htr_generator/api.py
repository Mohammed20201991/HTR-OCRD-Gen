from htr_generator.pipeline import Pipeline
from box import Box
import yaml


def generate(config_path: str, out_dir: str, count: int = 1000, mode: str = 'line'):
    with open(config_path, 'r') as f:
        conf = Box(yaml.safe_load(f))
    pipeline = Pipeline(conf)
    pipeline.run(out_dir=out_dir, count=count, mode=mode)