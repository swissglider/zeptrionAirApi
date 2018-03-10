"""
Support for ZeptrionAirChannel.

For more details about this Class, please refer to the documentation at
https://github.com/swissglider/zeptrionAirApi
"""

import time


class ZeptrionAirChannelLightController:
    """
    Support for ZeptrionAirChannel.

    For more details about this Class, please refer to the documentation at
    https://github.com/swissglider/zeptrionAirApi
    """

    def __init__(
            self, channel_cat, channel_id, panel_url):
        """Init the ZeptrionAirChannelLightController. """
        self._panel_url = panel_url
        self._channel_cat = channel_cat
        self._channel_id = channel_id
        self._blind_position = None

    def update(self):
        """Update the real status of the channel switch."""
        import requests
        import xml.etree.ElementTree as ET
        full_url = self._panel_url
        full_url += "/zrap/chscan/" + self._channel_id
        device_info_response = requests.get(full_url)
        if device_info_response.status_code == 200:
            root = ET.fromstring(device_info_response.text)
            if root[0][0].text == '100':
                return True
            return False
        return False  # pragma: no cover

    def turn_on_light(self):
        """Turn the real light switch off."""
        self._control_light("cmd=on")

    def turn_off_light(self):
        """Turn the real light switch off."""
        self._control_light("cmd=off")

    def toggle_light(self):
        """Toggles the real light switch."""
        self._control_light("cmd=toggle")

    def _control_light(self, payload):
        if self._channel_cat == '1':
            import requests
            full_url = self._panel_url
            full_url += "/zrap/chctrl/" + self._channel_id
            requests.post(full_url, data=payload)
            self._state = self.update()