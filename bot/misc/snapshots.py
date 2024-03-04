import os.path
from abc import ABC, abstractmethod


class Snapshot(ABC):
    TEXT_ENCODING = 'UTF-8'

    def __init__(self, screenshot_path: str, snapshot_path: str):
        self.screenshot_path = screenshot_path
        self.snapshot_path = snapshot_path

    @abstractmethod
    def make_snapshot(self, content: str):
        pass

    @abstractmethod
    def get_snapshot(self) -> str:
        with open(self.snapshot_path, 'r', encoding=self.TEXT_ENCODING) as snapshot:
            content = snapshot.read()
            return content


class SiteSnapshot(Snapshot):

    def __init__(self, screenshot_path: str, snapshot_path: str):
        super().__init__(screenshot_path, snapshot_path)

    def get_snapshot(self) -> str:
        return super().get_snapshot()

    def make_snapshot(self, content: str):
        with open(self.snapshot_path, 'w+', encoding=self.TEXT_ENCODING) as snapshot:
            snapshot.write(content)
