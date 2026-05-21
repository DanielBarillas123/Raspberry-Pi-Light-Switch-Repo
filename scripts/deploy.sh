# This script will clone the repository, set up a virtual environment, and install the required dependencies.
git clone https://github.com/DanielBarillas123/Raspberry-Pi-Light-Switch-Repo.git
cd Raspberry-Pi-Light-Switch-Repo
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install -r requirements.txt
deactivate