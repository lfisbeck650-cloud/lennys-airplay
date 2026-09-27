import subprocess
import socket
import os
import signal
import time
import json
from pathlib import Path


class AirPlayReceiver:
    def __init__(self, config):
        self.config = config
        self.process = None
        self.connected_devices = []
        self.log_file = Path("airplay_receiver.log")

    def get_local_ip(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except Exception:
            return "127.0.0.1"

    def start(self):
        if self.process and self.process.poll() is None:
            print("AirPlay Receiver is already running!")
            return False

        self.connected_devices = []

        cmd = [
            "uxplay",
            "-n", self.config.device_name,
            "-p", str(self.config.port),
            "-s", self.config.resolution,
            "-fps", str(self.config.fps),
        ]

        if self.config.password:
            cmd.extend(["-pw", self.config.password])

        try:
            self.process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            time.sleep(2)

            if self.process.poll() is not None:
                stdout, stderr = self.process.communicate()
                print(f"Error starting AirPlay Receiver:")
                print(stderr)
                return False

            return True
        except FileNotFoundError:
            print("Error: uxplay not found!")
            print("Please install UxPlay first:")
            print("  sudo apt install uxplay")
            print("Or build from source:")
            print("  git clone https://github.com/FDH2/UxPlay.git")
            print("  cd UxPlay && mkdir build && cd build")
            print("  cmake .. && make && sudo make install")
            return False
        except Exception as e:
            print(f"Error starting AirPlay Receiver: {e}")
            return False

    def stop(self):
        if self.process and self.process.poll() is None:
            self.process.terminate()
            try:
                self.process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.process.kill()
                self.process.wait()
            self.process = None
            self.connected_devices = []
            return True
        return False

    def get_status(self):
        is_running = self.process and self.process.poll() is None

        if is_running:
            status = "Running"
        else:
            status = "Stopped"

        return {
            "status": status,
            "device_name": self.config.device_name,
            "ip_address": self.get_local_ip(),
            "port": self.config.port,
            "connected_devices": len(self.connected_devices),
        }

    def is_running(self):
        return self.process and self.process.poll() is None
