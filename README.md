# Raspberry-Pi-Light-Switch-Repo
If you are deploying on a system that doesn't already have the repo you can use the deploy script
The redeploy script is mainly there for development purposes so I don't need to type the commands by hand when I want to update the repo
When using the deploy script you want to nano a new bash file into the terminal "nano deploy.sh"
You then need to copy the lines within the deploy script within the github repo into the file you just made.
After that, save the file then type "chmod +x ./deploy.sh" which allows you to run the file using "./deploy.sh"
After you run it, it should create the repo and from there you can check it out inside an IDE or you can activate the .venv again using "source .venv/bin/activate" to be able to use "python3 main.py" to run the program in the command line.

## Materials
Explorer hat
Up to date raspberry pi
Python 3.7.3 or higher
LED connected to 5V and output 1

## Controls
There aren't many just button one on the explorer hat and button 4.

## Reasources
https://pypi.org/project/pylutron-caseta/#description
here is the page to the package that I used just incase you are curious
