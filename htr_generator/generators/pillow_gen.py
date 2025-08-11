from PIL import Image, ImageDraw, ImageFont
import random
from ..generators.base import BaseGenerator
from ..utils.fonts import FontPool

class PillowGenerator(BaseGenerator):
    def __init__(self, config):
        super().__init__(config)
        self.font_pool = FontPool(config.get('fonts', {}))
        self.bg_images = config.get('backgrounds', [])

    def _sample_text(self, mode):
        # simple text sampling; production should use corpora and language models
        fake = __import__('faker').Factory.create('en_US')
        if mode == 'word':
            return fake.word()
        elif mode == 'paragraph':
            return fake.paragraph(nb_sentences=3)
        return fake.sentence(nb_words=6)

    def generate(self, mode='line'):
        text = self._sample_text(mode)
        font_path = self.font_pool.random()
        font_size = random.randint(20, 60)
        font = ImageFont.truetype(font_path, font_size)
        # estimate size
        w, h = font.getsize_multiline(text)
        canvas_w = max(w + 40, 128)
        canvas_h = max(h + 40, 32)
        img = Image.new('RGB', (canvas_w, canvas_h), color='white')
        draw = ImageDraw.Draw(img)
        draw.text((20, 20), text, font=font, fill=(0,0,0))
        meta = {'text': text}
        return img, meta