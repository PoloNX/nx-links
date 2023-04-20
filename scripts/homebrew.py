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
        release = self.get_latest_pre_release(0)
        asset = self.get_asset_link(release, self.config[0]["assetPatterns"][0])
        self.out["Goldleaf"] = asset[0].browser_download_url
        self.out["Goldleaf_version"] = release.tag_name
        
        self.config = [{"username": "J-D-K","reponame": "JKSV","assetPatterns": [".*JKSV.*\\.nro"]}]
        release = self.get_latest_release(0)
        asset = self.get_asset_link(release, self.config[0]["assetPatterns"][0])
        self.out["JKSV"] = asset[0].browser_download_url
        self.out["JKSV_version"] = release.tag_name

        self.config = [{"username": "mtheall","reponame": "ftpd","assetPatterns": [".*ftpd-classic.*\\.nro"]}]
        release = self.get_latest_release(0)
        asset = self.get_asset_link(release, self.config[0]["assetPatterns"][0])
        self.out["FTPD"] = asset[0].browser_download_url
        self.out["FTPD_version"] = release.tag_name

        self.config = [{"username": "rashevskyv","reponame": "dbi","assetPatterns": [".*DBI.*\\.nro"]}]
        release = self.get_latest_release(0)
        asset = self.get_asset_link(release, self.config[0]["assetPatterns"][0])
        self.out["DBI"] = asset[0].browser_download_url
        self.out["DBI_version"] = release.tag_name
        
        self.config = [{"username": "PoloNX","reponame": "Ls-News","assetPatterns": [".*Ls-News.*\\.nro"]}]
        release = self.get_latest_release(0)
        asset = self.get_asset_link(release, self.config[0]["assetPatterns"][0])
        self.out["Ls-News"] = asset[0].browser_download_url
        self.out["Ls-News_version"] = release.tag_name

