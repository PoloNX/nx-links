from github import Github, GithubException
import re
import argparse
import json
import requests

parser = argparse.ArgumentParser(description="Get links for AtmoPackUpdater")
base_url = "https://codeberg.org/api/v1/repos"

class CodebergModule:
    def __init__(self, config={}):
        print("Init module: ", self.__module__)
        self.path = self.__module__ + ".json"
        self.out = {}
        self.handle_module()

    def get_latest_release(self, index):
        response = requests.get("{}/{}/{}/releases/latest".format(base_url, self.config[index]["username"], self.config[index]["reponame"]))

        if response.status_code == 200:
            return response.json()

    def get_asset_link(self, release, pattern):
        assets = []
        for asset in release["assets"]:
            if re.search(pattern, asset.get("browser_download_url")):
                assets.append(asset)
        return assets

    def get_asset_links(self, release, index):
        assetPaths = []
        if release is not None:
            for pattern in self.config[index]["assetPatterns"]:
                assetPaths += self.get_asset_link(release, pattern)
        return assetPaths

    def handle_module(self):
        for i in range(len(self.config)):
            release = self.get_latest_release(i)
            assets = self.get_asset_links(release, i)
            for a in assets:
                self.out[a.name] = a.browser_download_url

    def write_json(self):
        with open(self.path, 'w') as write_file:
            json.dump(self.out, write_file, indent=4)
