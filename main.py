import botpy
import os
from botpy.ext.cog_yaml import read
from client import Client

config = read(os.path.join(os.path.dirname(__file__), "config.yaml"))

if __name__ == "__main__":
    intents = botpy.Intents(public_messages=True)
    client = Client(intents=intents, is_sandbox=True)
    client.run(appid=config["appid"], secret=config["secret"])
