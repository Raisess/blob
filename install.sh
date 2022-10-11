#! /usr/bin/env bash

BIN=/usr/local/bin/blob
ETC=/usr/local/etc/blob
LIB=/usr/local/lib/blob

sudo mkdir -p $LIB
sudo cp ./src/**.py $LIB
sudo mkdir -p $ETC/themes
sudo cp ./base.html $ETC/themes

echo "
#! /usr/bin/env bash

$LIB/main.py \$1 \$2
" > cli.sh

sudo chmod +x cli.sh
sudo mv cli.sh $BIN
