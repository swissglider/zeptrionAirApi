"""
Support for ZeptrionAirChannel.

For more details about this Class, please refer to the documentation at
https://github.com/swissglider/zeptrionAirApi
"""

import time
import requests


class ZeptrionAirChannelBlindController:
    """
    Support for ZeptrionAirChannel.

    For more details about this Class, please refer to the documentation at
    https://github.com/swissglider/zeptrionAirApi
    """

    def __init__(self, helper):
        """Init the ZeptrionAirChannelBlindController."""
        self.helper = helper
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
        0 = open
        100 = close
        """
        sleep_time = None
        if self._blind_position is None:
            payload = "cmd=open"
            self._control_blind(payload)
            time.sleep(float(0.2))
            while self.update():
                time.sleep(float(0.2))
            payload = "cmd=close"
            self._control_blind(payload)
            sleep_time = float(53.7/100*postion)
        elif postion < self._blind_position:
            payload = "cmd=open"
            self._control_blind(payload)
            sleep_time = float(55.3/100*(self._blind_position-postion))
        elif postion > self._blind_position:
            payload = "cmd=close"
            self._control_blind(payload)
            sleep_time = float(53.7/100*(postion-self._blind_position))
        time.sleep(sleep_time)
        payload = "cmd=stop"
        self._control_blind(payload)
        self._blind_position = postion

    def _control_blind(self, payload):
        if self.helper.channel_cat == '5':
            full_url = self.helper.panel_url
            full_url += "/zrap/chctrl/" + self.helper.channel_id
            requests.post(full_url, data=payload)
            self._state = self.update()

    def update(self):
        """Update the real status of the channel switch."""
        return self.helper.update()
