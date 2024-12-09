import requests

class AmsCfw:
    def __init__(self):
        self.download_url = "https://sighya.fr/AtmoPackFetcherBrowser/AtmoPack-Vanilla_Latest.zip"
        self.output_file = "AtmoPack-Vanilla_Latest.zip"
        self.out = {}

    def download_file(self):
        try:
            response = requests.get(self.download_url, stream=True)
            if response.status_code == 200:
                with open(self.output_file, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=1024):
                        if chunk:
                            file.write(chunk)
                self.out["status"] = "success"
                self.out["file"] = self.output_file
                print(f"Downloaded: {self.output_file}")
            else:
                self.out["status"] = "failed"
                self.out["error"] = f"HTTP {response.status_code}"
                print(f"Failed to download: HTTP {response.status_code}")
        except Exception as e:
            self.out["status"] = "failed"
            self.out["error"] = str(e)
            print(f"Error: {e}")

ams_cfw = AmsCfw()
ams_cfw.download_file()
