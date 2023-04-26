from basemodule import BaseModule

class Homebrew(BaseModule):
    def __init__(self):
        self.config = [
            {
                "username": "XorTroll",
                "reponame": "Goldleaf",
                "assetPatterns": [".*Goldleaf.*\\.nro"]
            }
        ]
        BaseModule.__init__(self)

    def handle_module(self):
        a=[]
        a.append([{"username": "rashevskyv","reponame": "dbi","assetPatterns": [".*DBI.*\\.nro"]}])
        a.append([{"username": "WerWolv","reponame": "EdiZon","assetPatterns": [".*EdiZon.*\\.nro"]}])
        a.append([{"username": "mtheall","reponame": "ftpd","assetPatterns": [".*ftpd-classic.*\\.nro"]}])
        a.append([{"username": "XorTroll","reponame": "Goldleaf", "assetPatterns": [".*Goldleaf.*\\.nro"]}])
        a.append([{"username": "WerWolv","reponame": "Hekate-Toolbox","assetPatterns": [".*HekateToolbox.*\\.nro"]}])
        a.append([{"username": "J-D-K","reponame": "JKSV","assetPatterns": [".*JKSV.*\\.nro"]}])
        a.append([{"username": "tallbl0nde","reponame": "NX-Activity-Log","assetPatterns": [".*NX-Activity-Log.*\\.nro"]}])
        a.append([{"username": "PoloNX","reponame": "Ls-News","assetPatterns": [".*Ls-News.*\\.nro"]}])

        for i in a:
            self.config = i
            if self.config[0]["reponame"] == "Goldleaf":
                release = self.get_latest_pre_release(0)
            else:
                release = self.get_latest_release(0)
            asset = self.get_asset_link(release, self.config[0]["assetPatterns"][0])
            self.out[self.config[0]["reponame"]] = {"name": i[0]["reponame"] , "link": asset[0].browser_download_url, "version": release.tag_name}
