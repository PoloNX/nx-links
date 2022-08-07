from basemodule import BaseModule

class Firmwares(BaseModule):
    def __init__(self):
        self.config = [
            {
                "username": "THZoria",
                "reponame": "NX_Firmware",
                "assetPatterns": [".*Firmware.*\\.zip"]
            }
        ]
        BaseModule.__init__(self)

    def handle_module(self):
        for i in range(len(self.config)):
            release = self.get_releases(i)
            for j in range(5):
                assets = self.get_asset_links(release[1], i)
                for asset in assets:
                    self.out[release[1].title] = asset.browser_download_url
