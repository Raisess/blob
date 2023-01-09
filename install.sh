#! /usr/bin/env bash
#
echo "Installing blob..."

sudo cp ./bin/blob /usr/local/bin/blob

sudo rm -rf /usr/local/lib/blob
sudo cp -r ./src /usr/local/lib/blob

sudo rm -rf /usr/local/etc/blob
sudo mkdir -p /usr/local/etc/blob/themes
sudo cp -r ./themes/* /usr/local/etc/blob/themes

echo "Installed successfully!"
