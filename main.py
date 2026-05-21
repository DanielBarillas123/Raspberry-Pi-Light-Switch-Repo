import explorerhat
from time import sleep
import asyncio
import os
from ast import literal_eval
from pathlib import Path
from pylutron_caseta.smartbridge import Smartbridge
from pylutron_caseta.pairing import async_pair

#This function loads the HOST variable from a .env file so no information is stored in the code. although it is a lan IP address it's just good practice.
def load_env(path: str = ".env") -> None:
    p = Path(path)
    if not p.exists():
        return
    for raw in p.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        key, val = line.split("=", 1)
        key = key.strip()
        val = val.strip().strip('"').strip("'")
        os.environ.setdefault(key, val)


load_env()
HOST = os.getenv("HOST")
if not HOST:
    raise RuntimeError(
        "HOST is not set. Create a .env file with HOST=<Hub-IP>"
    )

async def pair(host: str):
    # press pair button on the switch hub.
    data = await async_pair(host)

    # save the certificates and key to files for use in the main program
    with open("caseta-bridge.crt", "w") as cacert:
        cacert.write(data["ca"])
    with open("caseta.crt", "w") as cert:
        cert.write(data["cert"])
    with open("caseta.key", "w") as key:
        key.write(data["key"])

    # print that the pairing was successful and show the version of the switch hub
    print(f"Successfully paired with {data['version']}")

# Set up the button press event handler
async def on_button_press(channel, event):
    # Toggle the light on and off when the button is pressed
    if channel == 1 and event == "press":
        if device['current_state'] > 0:
            await bridge.turn_off(device['device_id'])
        else:
            await bridge.turn_on(device['device_id'])
    # Exit the program when the exit button is pressed also turns off the light
    elif channel == 4 and event == "press":
        explorerhat.output.one.off()
        await bridge.close()
        exit()


async def Enable_room_device():
    # Turn on the light to indicate that the program is running
    explorerhat.output.one.on()

    # use the certificates and key to connect to the switch hub and control the devices
    global bridge
    bridge = Smartbridge.create_tls(HOST, "caseta.key", "caseta.crt", "caseta-bridge.crt")

    # Connect to the switch hub and get the list of devices, then find the device with the name "Daniel's Room_Main Lights" and store it in a global variable for use in the button press event handler
    await bridge.connect()
    devices = bridge.get_devices()
    global device
    for i in devices:
        if devices[i]['name'] == "Daniel's Room_Main Lights":
            device = devices[i]
    print (device)


def cert_files_exist() -> bool:
    # this returns a true or false value based on if the certificate/key files exist.
    return (
        Path("caseta.key").exists()
        and Path("caseta.crt").exists()
        and Path("caseta-bridge.crt").exists()
    )


if __name__ == "__main__":
    # Check if the certificate files exist, if not run the pairing process to create them. This allows the program to be run without needing to pair every time.
    if not cert_files_exist():
        print("Certificate files missing — running pairing go hit pairing button...")
        try:
            asyncio.run(pair(HOST))
        except Exception as e:
            print(f"Pairing failed: {e}")
            raise
    # Run the main program to set device as the correct room light
    asyncio.run(Enable_room_device())
    # Set up the button press event handler and keep the program running to listen for button presses
    while True:
        explorerhat.touch.pressed(asyncio.run(on_button_press))