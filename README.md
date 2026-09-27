# Lennys AirPlay

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
```

### Linux (Alpine)

```bash
sudo apk add \
    build-base \
    cmake \
    openssl-dev \
    avahi-dev \
    libplist-dev \
    gstreamer-dev \
    gst-plugins-base-dev \
    gst-plugins-good \
    gst-plugins-bad-dev \
    gst-plugins-ugly \
    gst-libav
```

### macOS

```bash
brew install cmake openssl avahi libplist gstreamer gst-plugins-base gst-plugins-good gst-plugins-bad gst-libav
```

## Installation

### From Source

1. Clone this repository:
```bash
git clone https://github.com/lennyfisbeck/lennys-airplay.git
cd lennys-airplay
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

4. Build and install UxPlay:
```bash
git clone https://github.com/FDH2/UxPlay.git
cd UxPlay
mkdir build && cd build
cmake ..
make
sudo make install
```

5. Run the application:
```bash
python main.py
```

### From Package

#### Debian/Ubuntu (.deb)

```bash
sudo dpkg -i lennys-airplay_1.0.0_all.deb
sudo apt-get install -f
```

#### Fedora/RHEL (.rpm)

```bash
sudo rpm -i lennys-airplay-1.0.0-1.noarch.rpm
```

#### Void Linux (.xbps)

```bash
sudo xbps-install -f lennys-airplay
```

#### AppImage

```bash
chmod +x LennysAirPlay-1.0.0-x86_64.AppImage
./LennysAirPlay-1.0.0-x86_64.AppImage
```

## Usage

Run the application:
```bash
python main.py
```

Or if installed globally:
```bash
lennys-airplay
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

## Building Packages

To build all packages, run:
```bash
./build.sh
```

This creates:
- `dist/lennys-airplay_1.0.0_all.deb` (Debian/Ubuntu)
- `dist/lennys-airplay-1.0.0-1.noarch.rpm` (Fedora/RHEL)
- `dist/LennysAirPlay-1.0.0-x86_64.AppImage` (AppImage)

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
