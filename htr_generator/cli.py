"""Simple CLI to generate datasets."""
import argparse
from htr_generator.api import generate

parser = argparse.ArgumentParser(prog='htr-gen')
parser.add_argument('--config', '-c', type=str, default='configs/default.yaml')
parser.add_argument('--out', '-o', type=str, required=True)
parser.add_argument('--count', type=int, default=1000)
parser.add_argument('--mode', choices=['line','word','paragraph'], default='line')
args = parser.parse_args()

if __name__ == '__main__':
    generate(config_path=args.config, out_dir=args.out, count=args.count, mode=args.mode)