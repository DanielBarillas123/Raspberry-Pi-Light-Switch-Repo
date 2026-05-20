import explorerhat
from time import sleep

def main():
	explorerhat.output.one.on()
	sleep(2)
	explorerhat.output.one.off()
	


if __name__ == "__main__":
	main()
