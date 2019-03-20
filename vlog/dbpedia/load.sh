#!/bin/bash

rm -rf ../../data/dbpedia/kb/
../../../vlog/build/vlog load -i ../../data/dbpedia/db_ttl/ -o ../../data/dbpedia/kb/
