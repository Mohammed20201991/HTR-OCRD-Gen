# HTR-OCRD-Gen
HTR-OCR Dataset Generator

Overview

This repository is a complete, ready-to-run project scaffolding to generate HTR (Handwritten Text Recognition) and OCR datasets.
It combines several approaches and libraries (TRDG, SynthText ideas, Pillow, imgaug, OpenCV, Faker) under a unified CLI and Python API. 
It can produce line-/word-/paragraph-level images and export labels in multiple formats (IAM-style, COCO, JSONL, PAGE-XML, plain TSV). 
It also supports augmentation, background blending, fonts management, and dataset splitting.


Project Structuer 
```
htr_ocr_generator/
├── README.md
├── requirements.txt
├── setup.py
├── LICENSE
├── configs/
│   └── default.yaml
├── data/
│   ├── backgrounds/          # user-provided background images
│   └── fonts/                # user-provided fonts (TTF/OTF)
├── htr_generator/            # python package
│   ├── __init__.py
│   ├── cli.py                # entrypoint CLI
│   ├── api.py                # high-level API
│   ├── pipeline.py           # orchestration: generator -> augment -> label
│   ├── generators/
│   │   ├── base.py
│   │   ├── pillow_gen.py     # simple generator using Pillow + Faker
│   │   ├── trdg_wrapper.py   # optional wrapper to call TRDG if installed
│   │   └── synthtext_wrapper.py # scaffolding for synthtext-like generation
│   ├── augmentations.py      # imgaug based augmentation wrappers
│   ├── utils/
│   │   ├── fonts.py          # font discovery & randomization
│   │   ├── images.py         # helpers: save, blend, distort
│   │   └── labelers.py       # label format conversions
│   └── exporters/
│       ├── coco_exporter.py
│       ├── iam_exporter.py
│       └── pagexml_exporter.py
├── examples/
│   ├── gen_lines.py
│   └── gen_words.py
└── tests/
    └── test_basic.py
```



```
from htr_generator.api import generate
generate('configs/default.yaml', out_dir='out_dataset', count=1000, mode='line')
```