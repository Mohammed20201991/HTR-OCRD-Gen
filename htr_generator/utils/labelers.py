import json, os

class LabelManager:
    def __init__(self, config):
        self.config = config or {}
        self.format = self.config.get('format', 'jsonl')

    def make_label(self, filename, meta: dict):
        # meta must contain at least text
        return {'image': filename, 'text': meta.get('text',''), 'meta': meta}

    def export(self, labels, out_dir):
        if self.format == 'jsonl':
            p = os.path.join(out_dir, 'labels.jsonl')
            with open(p,'w',encoding='utf8') as f:
                for item in labels:
                    f.write(json.dumps(item, ensure_ascii=False) + '\n')
        else:
            # implement other exporters
            self._export_simple(labels, out_dir)

    def _export_simple(self, labels, out_dir):
        p = os.path.join(out_dir, 'labels.txt')
        with open(p, 'w', encoding='utf8') as f:
            for item in labels:
                f.write(f"{item['image']}\t{item['text']}\n")