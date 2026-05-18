from sc2.data import Race


class Macro:
    def __init__(self, ai, config: dict):
        self.ai = ai
        self.config = config

    def on_step(self) -> None:
        pass
