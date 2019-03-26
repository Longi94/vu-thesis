#!/bin/bash

echo "Running as user $USER, using folder /var/scratch/$USER/"

rm -rf "/var/scratch/$USER/dbpedia/mat/"
~/vlog/build/vlog mat -e edb.conf --rules rules.dlog --storemat_path "/var/scratch/$USER/dbpedia/mat/" --storemat_format csv --decompressmat 1
