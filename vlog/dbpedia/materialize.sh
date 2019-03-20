#!/bin/bash

rm -rf ../../data/dbpedia/mat/
../../../vlog/build/vlog mat -e edb.conf --rules rules.dlog --storemat_path ../../data/dbpedia/mat/ --storemat_format csv --decompressmat 1
