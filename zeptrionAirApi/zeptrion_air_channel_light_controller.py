"""
Support for ZeptrionAirChannel.

For more details about this Class, please refer to the documentation at
https://github.com/swissglider/zeptrionAirApi
"""


class ZeptrionAirChannelLightController:
    """
    Support for ZeptrionAirChannel.

    For more details about this Class, please refer to the documentation at
    https://github.com/swissglider/zeptrionAirApi
    """

    def __init__(self, helper):
        """Init the ZeptrionAirChannelLightController."""
        self.helper = helper
        self._led_state = None

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
        if self.helper.channel_cat == '1':
            import requests
            full_url = self.helper.panel_url
            full_url += "/zrap/chctrl/" + self.helper.channel_id
            requests.post(full_url, data=payload)
            self._led_state = self.update()

    def update(self):
        """Update the real status of the channel switch."""
        return self.helper.update()
