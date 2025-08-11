import os, random

class FontPool:
    def __init__(self, config_or_path):
        if isinstance(config_or_path, dict):
            font_dirs = config_or_path.get('dirs', ['data/fonts'])
        else:
            font_dirs = [config_or_path]
        self.font_files = []
        for d in font_dirs:
            if os.path.isdir(d):
                for f in os.listdir(d):
                    if f.lower().endswith(('.ttf','.otf')):
                        self.font_files.append(os.path.join(d,f))
        if not self.font_files:
            raise RuntimeError('No fonts found. Please add fonts to data/fonts/')

    def random(self):
        return random.choice(self.font_files)