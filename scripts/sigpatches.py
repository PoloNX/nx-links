from basemodule import BaseModule

class Sigpatches(BaseModule):
    def handle_module(self):
        for i in range(len(self.config)):
            self.out["sigpatches"] = "jits.cc/patches"
            self.out["version"] = "???"
