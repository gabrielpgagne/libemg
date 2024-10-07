from abc import ABC, abstractmethod
from pathlib import Path
import pickle

import pygame

from libemg.environments.controllers import Controller

class Environment(ABC):
    def __init__(self, controller: Controller, fps: int, log_dictionary: dict, save_file: str | None = None):
        # Assumes this is a pygame environment
        self.controller = controller
        self.done = False   # flag to determine when loop should be exited
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.log_dictionary = log_dictionary
        self.save_file = save_file
        pygame.init()
        pygame.font.init()
        pygame.mixer.init() 

    def run(self):
        if not self.controller.is_alive():
            self.controller.start()

        while not self.done:
            self._run_helper()
            pygame.display.update()
            self.clock.tick(self.fps)

        self.save_results()
        pygame.quit()

    @abstractmethod
    def _run_helper(self):
        # If there's a use case, we could a block = True flag so we'd put this in a different thread if False
        ...

    def save_results(self):
        if self.save_file is None:
            # Don't log anything
            return

        file = Path(self.save_file).absolute()
        file.parent.mkdir(parents=True, exist_ok=True) # create parent directories if they don't exist
        with open(self.save_file, 'wb') as f:
            pickle.dump(self.log_dictionary, f)
