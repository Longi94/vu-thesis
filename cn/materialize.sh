#!/bin/bash

echo "Running as user $USER, using folder /var/scratch/$USER/"

rm -rf "/var/scratch/$USER/conceptnet/mat/"
~/vlog/build/vlog mat -e edb.conf --rules rules.dlog --storemat_path "/var/scratch/$USER/conceptnet/mat/" --storemat_format csv --decompressmat 1
