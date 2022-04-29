import sys
import logging
import importlib
import socket
from pathlib import Path

def load_plugins(plugin_name):
    path = Path(f"mybot/plugins/{plugin_name}.py")
    name = "mybot.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["mybot.plugins." + plugin_name] = load
    print("Imported These Plugins--> " + plugin_name)


async def _netcat(host, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, int(port)))
    s.sendall(content.encode())
    s.shutdown(socket.SHUT_WR)
    while True:
        data = s.recv(4096).decode('utf-8').strip('\n\x00')
        if not data:
            break
        return data
    s.close()

async def paste(content):
    link = await _netcat('ezup.dev', 9999, content)
    return link
