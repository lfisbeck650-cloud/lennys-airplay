import sys
import os
import subprocess
import signal
import time
import json
from pathlib import Path

from airplay_receiver import AirPlayReceiver
from config import Config


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header():
    print("=" * 50)
    print("       AirPlay Screen Mirror")
    print("=" * 50)
    print()


def print_menu():
    print("1. Start AirPlay Receiver")
    print("2. Stop AirPlay Receiver")
    print("3. Show Status")
    print("4. Settings")
    print("5. Exit")
    print()


def print_status(receiver):
    status = receiver.get_status()
    print("-" * 50)
    print(f"Status: {status['status']}")
    print(f"Device Name: {status['device_name']}")
    print(f"IP Address: {status['ip_address']}")
    print(f"Port: {status['port']}")
    print(f"Connected Devices: {status['connected_devices']}")
    print("-" * 50)
    print()


def print_settings(config):
    print("-" * 50)
    print("Current Settings:")
    print(f"  Device Name: {config.device_name}")
    print(f"  Port: {config.port}")
    print(f"  Password: {'*' * len(config.password) if config.password else 'Not set'}")
    print(f"  Resolution: {config.resolution}")
    print(f"  FPS: {config.fps}")
    print("-" * 50)
    print()


def settings_menu(config):
    while True:
        clear_screen()
        print_header()
        print_settings(config)
        print("Settings Menu:")
        print("1. Change Device Name")
        print("2. Change Port")
        print("3. Change Password")
        print("4. Change Resolution")
        print("5. Change FPS")
        print("6. Back to Main Menu")
        print()

        choice = input("Select option: ").strip()

        if choice == "1":
            new_name = input("Enter new device name: ").strip()
            if new_name:
                config.device_name = new_name
                config.save()
                print("Device name updated!")
                time.sleep(1)
        elif choice == "2":
            try:
                new_port = int(input("Enter new port (1024-65535): ").strip())
                if 1024 <= new_port <= 65535:
                    config.port = new_port
                    config.save()
                    print("Port updated!")
                else:
                    print("Invalid port range!")
            except ValueError:
                print("Invalid input!")
            time.sleep(1)
        elif choice == "3":
            new_password = input("Enter new password (leave empty for no password): ").strip()
            config.password = new_password
            config.save()
            print("Password updated!")
            time.sleep(1)
        elif choice == "4":
            print("Available resolutions:")
            print("1. 1920x1080 (Full HD)")
            print("2. 1280x720 (HD)")
            print("3. 3840x2160 (4K)")
            res_choice = input("Select resolution: ").strip()
            resolutions = {"1": "1920x1080", "2": "1280x720", "3": "3840x2160"}
            if res_choice in resolutions:
                config.resolution = resolutions[res_choice]
                config.save()
                print("Resolution updated!")
            else:
                print("Invalid choice!")
            time.sleep(1)
        elif choice == "5":
            try:
                new_fps = int(input("Enter new FPS (15-60): ").strip())
                if 15 <= new_fps <= 60:
                    config.fps = new_fps
                    config.save()
                    print("FPS updated!")
                else:
                    print("Invalid FPS range!")
            except ValueError:
                print("Invalid input!")
            time.sleep(1)
        elif choice == "6":
            break


def main():
    config = Config()
    receiver = AirPlayReceiver(config)

    def signal_handler(sig, frame):
        print("\nShutting down...")
        receiver.stop()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    while True:
        clear_screen()
        print_header()
        print_menu()

        choice = input("Select option: ").strip()

        if choice == "1":
            clear_screen()
            print_header()
            print("Starting AirPlay Receiver...")
            print()
            receiver.start()
            print()
            print("AirPlay Receiver started!")
            print(f"Look for '{config.device_name}' on your iPhone/iPad")
            print()
            input("Press Enter to continue...")
        elif choice == "2":
            clear_screen()
            print_header()
            print("Stopping AirPlay Receiver...")
            receiver.stop()
            print("AirPlay Receiver stopped!")
            print()
            input("Press Enter to continue...")
        elif choice == "3":
            clear_screen()
            print_header()
            print_status(receiver)
            input("Press Enter to continue...")
        elif choice == "4":
            settings_menu(config)
        elif choice == "5":
            clear_screen()
            print_header()
            print("Goodbye!")
            receiver.stop()
            sys.exit(0)
        else:
            print("Invalid option!")
            time.sleep(1)


if __name__ == "__main__":
    main()
