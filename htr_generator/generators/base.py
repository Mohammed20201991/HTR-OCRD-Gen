from abc import ABC, abstractmethod

class BaseGenerator(ABC):
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def generate(self, mode='line'):
        """Return (PIL.Image, meta_dict) where meta_dict contains at least 'text' and optionally bounding boxes."""
        raise NotImplementedError