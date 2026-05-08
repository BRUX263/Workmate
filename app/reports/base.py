from abc import ABC, abstractmethod
from typing import Iterable


class BaseReport(ABC):

    @abstractmethod
    def generate(self, videos: Iterable):
        pass