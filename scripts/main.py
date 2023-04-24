import json

import ams_cfw
import firmwares
import sigpatches
import app
import homebrew
import tab

if __name__ == '__main__':

    json_file = "nx-links-new.json"
    try:
        with open(json_file, "r") as old_file:
            out = json.load(old_file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        out = {}

    modules = [
        ams_cfw.Ams_cfw(),
        sigpatches.Sigpatches(),
        firmwares.Firmwares(),
        app.App(),
        homebrew.Homebrew(),
        tab.Tab()
    ]
    for module in modules:
        if module.out == {}:
            print(f"Module {module.__module__} returned an empty dict.")
        out[module.__module__] = module.out

    with open(json_file, 'w') as out_file:
        json.dump(out, out_file, indent=4)
