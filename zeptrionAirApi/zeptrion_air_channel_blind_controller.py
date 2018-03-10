"""
Support for ZeptrionAirChannel.

For more details about this Class, please refer to the documentation at
https://github.com/swissglider/zeptrionAirApi
"""

import time
import requests
import xml.etree.ElementTree as ET


class ZeptrionAirChannelBlindController:
    """
    Support for ZeptrionAirChannel.

    For more details about this Class, please refer to the documentation at
    https://github.com/swissglider/zeptrionAirApi
    """

    def __init__(
            self, channel_cat, channel_id, panel_url):
        """Init the ZeptrionAirChannelBlindController."""
        self._panel_url = panel_url
        self._channel_cat = channel_cat
        self._channel_id = channel_id
        self._blind_position = None
        self._state = None

    def move_up_blind(self):
        """Move up blind."""
        self._control_blind("cmd=open")
        self._blind_position = None

    def move_down_blind(self):
        """Move down blind."""
        self._control_blind("cmd=close")
        self._blind_position = None

    def stop_blind(self):
        """Move stop blind."""
        self._control_blind("cmd=stop")
        self._blind_position = None

    def tilt_up_blind(self):
        """Tilt up blind."""
        self.move_up_blind()
        time.sleep(float(0.2))
        self.stop_blind()
        self._blind_position = None

    def tilt_down_blind(self):
        """Tilt up blind."""
        self.move_down_blind()
        time.sleep(float(0.2))
        self.stop_blind()
        self._blind_position = None

    def blind_is_stoped(self):
        """Tilt up blind."""
        return self.update()

    def go_to_position(self, postion):
        """
        Move blind to position.

        If position is not yet set, it goes first totally down
        """
        sleep_time = None
        if self._blind_position is None:
            payload = "cmd=close"
            self._control_blind(payload)
            time.sleep(float(0.2))
            while self.update():
                time.sleep(float(0.2))
            payload = "cmd=open"
            self._control_blind(payload)
            sleep_time = float(55.3/100*postion)
        elif postion < self._blind_position:
            payload = "cmd=open"
            self._control_blind(payload)
            sleep_time = float(53.7/100*(self._blind_position-postion))
        elif postion > self._blind_position:
            payload = "cmd=close"
            self._control_blind(payload)
            sleep_time = float(55.3/100*(postion-self._blind_position))
        time.sleep(sleep_time)
        payload = "cmd=stop"
        self._control_blind(payload)
        self._blind_position = postion

    def _control_blind(self, payload):
        if self._channel_cat == '5':
            import requests
            full_url = self._panel_url
            full_url += "/zrap/chctrl/" + self._channel_id
            requests.post(full_url, data=payload)
            self._state = self.update()

    def update(self):
        """Update the real status of the channel switch."""
        full_url = self._panel_url
        full_url += "/zrap/chscan/" + self._channel_id
        device_info_response = requests.get(full_url)
        if device_info_response.status_code == 200:
            root = ET.fromstring(device_info_response.text)
            if root[0][0].text == '100':
                return True
            return False
        return False  # pragma: no cover
