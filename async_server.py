import asyncio
import time
from zeptrion_air_api import Hub

async def do_close(hub):
    """ Close the System. """
    await hub.close()

def press_info_handler(press_info):
    """ Handle if the button is pressed. """
    print(press_info)

def found_new_panels(panel):
    """ Handle if a new Zeptrion Air Panel is found. """
    print('Register new zeptrion device [%s][%s]' % (panel.ip, panel.name))
    for button in panel.all_buttons:
        if button:
            button.listen_to(press_info_handler)

if __name__ == '__main__':
    """ Init the main test. """
    loop = asyncio.get_event_loop()
    za_hub = Hub(loop, found_new_panels)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        print("Unregistering...")
        loop.run_until_complete(do_close(za_hub))
    finally:
        loop.close()
