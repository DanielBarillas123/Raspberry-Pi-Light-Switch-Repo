import explorerhat
from time import sleep
import asyncio
from pylutron_caseta.smartbridge import Smartbridge
from pylutron_caseta.pairing import async_pair

async def pair(host: str):
    def _ready():
        print("Press the small black button on the back of the bridge.")

    data = await async_pair(host, _ready)
    with open("caseta-bridge.crt", "w") as cacert:
        cacert.write(data["ca"])
    with open("caseta.crt", "w") as cert:
        cert.write(data["cert"])
    with open("caseta.key", "w") as key:
        key.write(data["key"])
    print(f"Successfully paired with {data['version']}")

# Set up the button press event handler
def on_button_press(channel, event):
    # Toggle the light on and off when the button is pressed
    if channel == 1 and event == "press":
        pass
    # Exit the program when the exit button is pressed also turns off the light
    elif channel == 4 and event == "press":
        explorerhat.output.one.off()
        exit()


async def main():
    explorerhat.output.one.on()
    bridge = Smartbridge.create_tls("192.168.1.201", "caseta.key", "caseta.crt", "caseta-bridge.crt")
    await bridge.connect()
    devices =  bridge.get_devices_by_domain("light")
    print(len(devices))
    await bridge.turn_off(devices[3]["device_id"])
    await bridge.close()
	
if __name__ == "__main__":
    asyncio.run(pair("192.168.1.201"))
    asyncio.run(main())
