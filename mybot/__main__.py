import glob
import logging
from pathlib import Path
from mybot.utils import load_plugins
from . import Turtle

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = "mybot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        thepath = Path(a.name)
        plugin_name = thepath.stem
        load_plugins(plugin_name.replace(".py", ""))

print("Successfully deployed!")

if __name__ == "__main__":
    Turtle.run_until_disconnected()
