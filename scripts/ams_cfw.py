from codeberg import CodebergModule
import requests

class Ams_cfw(CodebergModule):
    def __init__(self):
        self.config = [
            {
                "username": "Zoria",
                "reponame": "AmoPack-Vanilla",
                "assetPatterns": [".*AtmoPack-Vanilla_Latest.*\\.zip"]
            }
        ]
        CodebergModule.__init__(self)

    def handle_module(self):
        for i in range(len(self.config)):
            release = self.get_latest_release(i)
            if release is not None:
                assets = self.get_asset_links(release, i)
                for asset in assets:
                    self.out[release.get("name")] = asset.get("browser_download_url")
                self.out["version"] = release.get("tag_name")

