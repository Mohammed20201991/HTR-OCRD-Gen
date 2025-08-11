# this wrapper uses TRDG if installed. It falls back cleanly if TRDG not available.
try:
    from trdg.generate import GeneratorFromStrings
    TRDG_AVAILABLE = True
except Exception:
    TRDG_AVAILABLE = False

from .base import BaseGenerator

class TRDGWrapper(BaseGenerator):
    def __init__(self, config):
        super().__init__(config)
        if not TRDG_AVAILABLE:
            raise RuntimeError("TRDG is not installed. Please `pip install trdg` or choose another generator.")
        self.conf = config

    def generate(self, mode='line'):
        # TRDG yields image bytes; simplify by asking for a single image
        text = "hello"  # placeholder; in practice sample from corpora
        g = GeneratorFromStrings([text], count=1, **self.conf.get('trdg_args', {}))
        img = next(g)  # PIL Image
        return img, {'text': text}