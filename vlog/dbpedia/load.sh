#!/bin/bash

echo "Running as user $USER, using folder /var/scratch/$USER/"

echo "Removing existing kb..."
rm -rf "/var/scratch/$USER/dbpedia/kb/"

echo "Starting VLog load..."
~/vlog/build/vlog load -i "/var/scratch/$USER/dbpedia/db_ttl/" -o "/var/scratch/$USER/dbpedia/kb/"
