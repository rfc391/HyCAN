
#!/bin/bash
echo "🔧 Building HyCAN Linux binary..."

# Create virtualenv and install
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt pyinstaller

# Build AppImage with PyInstaller
pyinstaller --onefile hycan_cli.py --name HyCAN

# Create .deb package
mkdir -p build/DEBIAN
echo -e "Package: hycan\nVersion: 1.0\nArchitecture: all\nMaintainer: HyCAN\nDescription: Hydrogen Catalyst and Nanomaterials" > build/DEBIAN/control
mkdir -p build/usr/local/bin
cp dist/HyCAN build/usr/local/bin/hycan
dpkg-deb --build build hycan.deb
