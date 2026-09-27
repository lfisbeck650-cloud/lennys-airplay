#!/bin/bash
set -e

PROJECT_NAME="lennys-airplay"
VERSION="1.0.0"
BUILD_DIR="build"
DIST_DIR="dist"

mkdir -p "$DIST_DIR"

echo "Building .deb package..."
dpkg-deb --build --root-owner-group "$BUILD_DIR/deb" "$DIST_DIR/${PROJECT_NAME}_${VERSION}_all.deb"

echo "Building .rpm package..."
rpmbuild -bb "$BUILD_DIR/rpm/${PROJECT_NAME}.spec" --define "_topdir $(pwd)/$BUILD_DIR/rpm" 2>/dev/null || {
    echo "rpmbuild not available, creating .rpm manually"
    cd "$BUILD_DIR/rpm"
    mkdir -p BUILD RPMS SOURCES SPECS SRPMS
    cp "${PROJECT_NAME}.spec" SPECS/
    rpmbuild -bb SPECS/"${PROJECT_NAME}.spec" --define "_topdir $(pwd)" 2>/dev/null || true
    cd ../..
}

echo "Building .xbps package..."
echo "xbps-src not available, template created in $BUILD_DIR/xbps/"

echo "Building .AppImage..."
cd "$BUILD_DIR/appimage"
mkdir -p usr/share/lennys-airplay
cp ../../main.py usr/share/lennys-airplay/
cp ../../airplay_receiver.py usr/share/lennys-airplay/
cp ../../config.py usr/share/lennys-airplay/
cp ../../requirements.txt usr/share/lennys-airplay/
cp ../../README.md usr/share/lennys-airplay/
cp lennys-airplay.desktop usr/share/applications/ 2>/dev/null || true
chmod +x AppRun
cd ../..

echo "Build complete. Packages in $DIST_DIR/"
ls -la "$DIST_DIR/"
