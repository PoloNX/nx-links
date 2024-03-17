from basemodule import BaseModule


class Tab(BaseModule):
    def __init__(self):
        BaseModule.__init__(self)

    def handle_module(self):
        self.out = {
            "Pack" : True,
            "App" : True,
            "Homebrew" : True,
            "Firmware" : True,
            "Sigpatches" : False
        }
