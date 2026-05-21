git clone https://github.com/DanielBarillas123/Raspberry-Pi-Light-Switch-Repo.git
cd Raspberry-Pi-Light-Switch-Repo
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt