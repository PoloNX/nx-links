from basemodule import BaseModule


class Sigpatches(BaseModule):
    def __init__(self):
        self.config = [
            {
                "username": "PHRetroGamers",
                "reponame": "signature_gpd",
                "assetPatterns": [".*signature_gpd.*\\.zip"]
            }
        ]
        BaseModule.__init__(self)

    def handle_module(self):
        for i in range(len(self.config)):
            self.out["sigpatches"] = "sigmapatches.coomer.party/sigpatches.zip?latest"
            self.out["version"] = "latest"
