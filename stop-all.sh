#!/bin/bash
echo -e "\e[1m\e[36mINFO:\e[0m Stopping process/thread running at port \e[1m4000\e[0m"
sudo fuser -k 4000/tcp 2>/dev/null

echo -e "\e[1m\e[36mINFO:\e[0m Stopping process/thread running at port \e[1m4001\e[0m"
sudo fuser -k 4001/tcp 2>/dev/null

echo -e "\e[1m\e[36mINFO:\e[0m Stopping process/thread running at port \e[1m4002\e[0m"
sudo fuser -k 4002/tcp 2>/dev/null

echo -e "\e[1m\e[36mINFO:\e[0m Stopping process/thread running at port \e[1m5000\e[0m"
sudo fuser -k 5000/tcp 2>/dev/null

echo -e "\e[1m\e[36mINFO:\e[0m Stopping process/thread running at port \e[1m5001\e[0m"
sudo fuser -k 5001/tcp 2>/dev/null
