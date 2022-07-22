# https://www.geeksforgeeks.org/abstract-classes-in-python/
from abc import ABC, abstractmethod

class ExtractorBase(ABC):
    def __init__(self):
        pass

    @staticmethod
    @abstractmethod
    # TODO: what type should this be?
    def extract() -> bool:
        pass


class StickingExtractor(ExtractorBase):
    sticking = -1

    # TODO: what needs to be kept track of
    def __init__(self, sticking: str, case_sensitive):
        self.stick

    @staticmethod
    def extract() -> bool:
        pass
