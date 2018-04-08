"""
Support for ZeptrionAirChannel.

For more details about this Class, please refer to the documentation at
https://github.com/swissglider/zeptrionAirApi
"""

import xml.etree.ElementTree as ET
import requests


class ZeptrionAirChannelUpdatHelper:
    """
    Support for ZeptrionAirChannel.

    For more details about this Class, please refer to the documentation at
    https://github.com/swissglider/zeptrionAirApi
    """

    def __init__(
            self, channel_cat, channel_id, panel_url):
        """Init the ZeptrionAirChannelBlindController."""
        self._channel_cat = channel_cat
        self._panel_url = panel_url
        self._channel_id = channel_id

    @property
    def panel_url(self):
        """Return panel url."""
        return self._panel_url

    @property
    def channel_cat(self):
        """Return channel categorie."""
        return self._channel_cat

    @property
    def channel_id(self):
        """Return channel uidrl."""
        return self._channel_id

    def update(self):
        """Update the real status of the channel switch."""
        full_url = self.panel_url
        full_url += "/zrap/chscan/" + self.channel_cat
        device_info_response = requests.get(full_url)
        if device_info_response.status_code == 200:
            root = ET.fromstring(device_info_response.text)
            if root[0][0].text == '100':
                return True
            return False
        return False  # pragma: no cover
