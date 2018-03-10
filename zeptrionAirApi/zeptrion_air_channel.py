"""
Support for ZeptrionAirChannel.

For more details about this Class, please refer to the documentation at
https://github.com/swissglider/zeptrionAirApi
"""

from .zeptrion_air_channel_blind_controller import ZeptrionAirChannelBlindController  # noqa: E501
from .zeptrion_air_channel_light_controller import ZeptrionAirChannelLightController  # noqa: E501


class ZeptrionAirChannel:
    """
    Support for ZeptrionAirChannel.

    For more details about this Class, please refer to the documentation at
    https://github.com/swissglider/zeptrionAirApi
    """

    def __init__(
            self, channel_info, panel):
        """
        Init the ZeptrionAirChannel.

            :param channel_info: -- dictornary with at least
                :channel_info['channel_id']
                :channel_info['channel_name']
                :channel_info['channel_group']
                :channel_info['channel_icon']
                :channel_info['channel_type']
                :channel_info['channel_cat']
            :param panel: -- ZeptrionAirPanel that hosts that channel
        """
        self._channel_info = channel_info
        self._panel = panel
        self._blind_controller = ZeptrionAirChannelBlindController(
            self._channel_info['channel_cat'],
            self._channel_info['channel_id'],
            self._panel.panel_url)
        self._light_controller = ZeptrionAirChannelLightController(
            self._channel_info['channel_cat'],
            self._channel_info['channel_id'],
            self._panel.panel_url)
        '''
        Cat:
            -1: Not configured
             1: Light
             5: Storen auf/ab
        '''

    @property
    def channel_uniq_id(self):
        """Return the uniq ID from the channel."""
        return str(self.panel_name)+str(self.channel_id)

    @property
    def channel_id(self):
        """Return the ID from the channel."""
        return self._channel_info['channel_id']

    @property
    def channel_name(self):
        """Return the Name from the channel."""
        return self._channel_info['channel_name']

    @property
    def channel_group(self):
        """Return the Group Name from the channel."""
        return self._channel_info['channel_group']

    @property
    def channel_icon(self):
        """Return the Icon from the channel."""
        return self._channel_info['channel_icon']

    @property
    def channel_type(self):
        """Return the Type from the channel."""
        return self._channel_info['channel_type']

    @property
    def channel_cat(self):
        """Return the Category from the channel."""
        return self._channel_info['channel_cat']

    @property
    def panel_name(self):
        """Return the Panel-Name from the channel."""
        return self._panel.panel_name

    @property
    def panel_type(self):
        """Return the Panel-Type from the channel."""
        return self._panel.panel_type

    @property
    def panel_ip(self):
        """Return the IP from the channel/panel."""
        return self._panel.panel_ip

    @property
    def panel_port(self):
        """Return the Port from the channel/panel."""
        return self._panel.panel_port

    @property
    def panel_url(self):
        """Return the URL from the channel/panel."""
        return self._panel.panel_url

    @property
    def channel_blind_state(self):
        """Return the URL from the channel/panel."""
        return self._blind_controller.update()

    @property
    def channel_light_state(self):
        """Return the URL from the channel/panel."""
        return self._light_controller.update()

    @property
    def blind_controller(self):
        """Return the URL from the channel/panel."""
        return self._blind_controller

    @property
    def light_controller(self):
        """Return the URL from the channel/panel."""
        return self._light_controller

    def __repr__(self):
        """Return a String representing the ZeptrionAirChannel."""
        return_str = "ID: " + str(self.channel_id) + '\n'
        return_str += "\tName: " + str(self.channel_name) + '\n'
        return_str += "\tGroup: " + str(self.channel_group) + '\n'
        return_str += "\tIcon: " + str(self.channel_icon) + '\n'
        return_str += "\tType: " + str(self.channel_type) + '\n'
        return_str += "\tCat: " + str(self.channel_cat) + '\n'
        return_str += "\tIP: " + str(self.panel_ip) + '\n'
        return_str += '\n'
        return return_str
