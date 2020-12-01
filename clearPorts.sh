#!/bin/bash
echo -e "Clearing port 4000"
sudo fuser -k 4000/tcp

echo -e "Clearing port 4001"
sudo fuser -k 4001/tcp

echo -e "Clearing port 4002"
sudo fuser -k 4002/tcp

echo -e "Clearing port 5000"
sudo fuser -k 5000/tcp

echo -e "Clearing port 5001"
sudo fuser -k 5001/tcp
