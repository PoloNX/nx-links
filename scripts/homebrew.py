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
        a.append([{"username": "rashevskyv","reponame": "dbi", "homebrew": True,"assetPatterns": [".*DBI.*\\.nro"]}])
        a.append([{"username": "WerWolv","reponame": "EdiZon", "homebrew": True,"assetPatterns": [".*EdiZon.*\\.nro"]}])
        a.append([{"username": "mtheall","reponame": "ftpd", "homebrew": True,"assetPatterns": [".*ftpd-classic.*\\.nro"]}])
        a.append([{"username": "XorTroll","reponame": "Goldleaf", "homebrew": True,"assetPatterns": [".*Goldleaf.*\\.nro"]}])
        a.append([{"username": "WerWolv","reponame": "Hekate-Toolbox", "homebrew": True,"assetPatterns": [".*HekateToolbox.*\\.nro"]}])
        a.append([{"username": "J-D-K","reponame": "JKSV", "homebrew": True,"assetPatterns": [".*JKSV.*\\.nro"]}])
        a.append([{"username": "tallbl0nde","reponame": "NX-Activity-Log", "homebrew": True,"assetPatterns": [".*NX-Activity-Log.*\\.nro"]}])
        a.append([{"username": "PoloNX","reponame": "Ls-News", "homebrew": True,"assetPatterns": [".*Ls-News.*\\.nro"]}])
        a.append([{"username": "PoloNX","reponame": "SimpleModDownloader", "homebrew": True,"assetPatterns": [".*SimpleModDownloader.*\\.nro"]}])
        a.append([{"username": "nadrino","reponame": "SimpleModManager", "homebrew": True,"assetPatterns": [".*SimpleModManager.*\\.nro"]}])

        a.append([{"username": "ndeadly","reponame": "MissionControl", "homebrew": False,"assetPatterns": [".*MissionControl.*\\.zip"]}])
        a.append([{"username": "exelix11","reponame": "SysDVR", "homebrew": False,"assetPatterns": ["SysDVR.zip"]}])
        a.append([{"username": "WerWolv","reponame": "nx-ovlloader", "homebrew": False,"assetPatterns": [".*nx-ovlloader.*\\.zip"]}])
        #overlays
        a.append([{"username": "WerWolv","reponame": "Tesla-Menu", "homebrew": False,"assetPatterns": [".*ovlmenu.*\\.zip"]}])
        a.append([{"username": "Hartie95","reponame": "fastCFWswitch", "homebrew": False,"assetPatterns": [".*fastCFWswitch.*\\.zip"]}])
        a.append([{"username": "HookedBehemoth","reponame": "sys-tune", "homebrew": False,"assetPatterns": [".*sys-tune.*\\.zip"]}])
        for i in a:
            self.config = i
            if self.config[0]["reponame"] == "Goldleaf" or self.config[0]["reponame"] == "emuiibo":
                release = self.get_latest_pre_release(0)
            else:
                release = self.get_latest_release(0)
            asset = self.get_asset_link(release, self.config[0]["assetPatterns"][0])
            self.out[self.config[0]["reponame"]] = {"name": i[0]["reponame"] , "link": asset[0].browser_download_url, "version": release.tag_name, "homebrew": i[0]["homebrew"]}
