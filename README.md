# AirPlay Screen Mirror

A simple Python application to mirror your iPhone/iPad screen to your PC via AirPlay.

## Features

- Simple menu-based interface
- Customizable device name, port, password, resolution, and FPS
- Real-time status display
- Configuration saved to JSON file
- Cross-platform support (Linux, macOS, Windows with WSL)

## Prerequisites

### Linux (Ubuntu/Debian)

```bash
# Install UxPlay dependencies
sudo apt update
sudo apt install -y \
    git \
    cmake \
    build-essential \
    libssl-dev \
    libavahi-client-dev \
    libplist-dev \
    libgstreamer1.0-dev \
    libgstreamer-plugins-base1.0-dev \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good \
    gstreamer1.0-plugins-bad \
    gstreamer1.0-libav \
    gstreamer1.0-tools

# Clone and build UxPlay
git clone https://github.com/FDH2/UxPlay.git
cd UxPlay
mkdir build && cd build
cmake ..
make
sudo make install
```

### macOS

```bash
# Install dependencies with Homebrew
brew install cmake openssl avahi libplist gstreamer gst-plugins-base gst-plugins-good gst-plugins-bad gst-libav

# Clone and build UxPlay
git clone https://github.com/FDH2/UxPlay.git
cd UxPlay
mkdir build && cd build
cmake ..
make
sudo make install
```

### Windows (WSL)

Use WSL2 and follow the Linux instructions above.

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/airplay-mirror.git
cd airplay-mirror
```

2. Create a virtual environment (optional but recommended):
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python main.py
```

### Menu Options

1. **Start AirPlay Receiver** - Starts the AirPlay server
2. **Stop AirPlay Receiver** - Stops the AirPlay server
3. **Show Status** - Displays current status
4. **Settings** - Configure device name, port, password, resolution, and FPS
5. **Exit** - Exit the application

### Connecting from iPhone/iPad

1. Make sure your iPhone/iPad is on the same Wi-Fi network as your PC
2. Start the AirPlay Receiver from the menu
3. On your iPhone/iPad, open Control Center
4. Tap "Screen Mirroring"
5. Select your device name (default: "AirPlay Mirror")
6. Enter the password if you set one

## Configuration

Settings are stored in `config.json`:

```json
{
  "device_name": "AirPlay Mirror",
  "port": 7000,
  "password": "",
  "resolution": "1920x1080",
  "fps": 30
}
```

## Troubleshooting

### Device not found
- Make sure both devices are on the same network
- Check that your firewall allows connections on the configured port
- Try restarting the AirPlay Receiver

### Poor video quality
- Lower the resolution in settings
- Reduce the FPS
- Make sure you have a strong Wi-Fi connection

### uxplay not found
- Make sure UxPlay is installed and in your PATH
- Try running `which uxplay` to verify installation

## License

MIT License

## Credits

- [UxPlay](https://github.com/FDH2/UxPlay) - AirPlay receiver implementation
- [pyatv](https://github.com/postlund/pyatv) - Apple TV library
