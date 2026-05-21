#!/bin/bash
cd /home/pi/Raspberry-Pi-Light-Switch-Repo
git pull origin main
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install -r requirements.txt
deactivate
