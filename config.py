import json
import os
from pathlib import Path


class Config:
    CONFIG_FILE = "config.json"

    def __init__(self):
        self.device_name = "AirPlay Mirror"
        self.port = 7000
        self.password = ""
        self.resolution = "1920x1080"
        self.fps = 30
        self.load()

    def load(self):
        config_path = Path(self.CONFIG_FILE)
        if config_path.exists():
            try:
                with open(config_path, "r") as f:
                    data = json.load(f)
                self.device_name = data.get("device_name", self.device_name)
                self.port = data.get("port", self.port)
                self.password = data.get("password", self.password)
                self.resolution = data.get("resolution", self.resolution)
                self.fps = data.get("fps", self.fps)
            except (json.JSONDecodeError, IOError):
                pass

    def save(self):
        data = {
            "device_name": self.device_name,
            "port": self.port,
            "password": self.password,
            "resolution": self.resolution,
            "fps": self.fps,
        }
        with open(self.CONFIG_FILE, "w") as f:
            json.dump(data, f, indent=2)
