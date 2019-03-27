#!/bin/bash

echo "Running as user $USER, using folder /var/scratch/$USER/"

echo "Removing existing kb..."
rm -rf "/var/scratch/$USER/conceptnet/kb/"

echo "Starting VLog load..."
~/vlog/build/vlog load -i "/var/scratch/$USER/conceptnet/ttl/" -o "/var/scratch/$USER/conceptnet/kb/"
