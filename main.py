import botpy
import os
from client import Client
from botpy.ext.cog_yaml import read

config = read(os.path.join(os.path.dirname(__file__), "config.yaml"))

if __name__ == "__main__":
    intents = botpy.Intents(public_messages=True)
    client = Client(intents=intents)
    client.run(appid=config["appid"], secret=config["secret"])
