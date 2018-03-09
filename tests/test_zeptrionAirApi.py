import unittest
from zeptrionAirApi import ZeptrionAirHub

class TestZeptrionAir(unittest.TestCase):
    def setup_class(self):
        self.hub = ZeptrionAirHub(3)
    
    def test_if_Hub_is_not_None(self):
        ''' Test if hub is initialized. '''
        self.assertTrue(self.hub is not None)

    def test_if_panels_are_found(self):
        ''' Test if panels are found. '''
        panels = self.hub.all_found_panels
        self.assertTrue(panels)

    def test_if_new_panels_found(self):
        ''' Test if new panels are found. '''
        latest_panels = self.hub.latest_found_panels
        self.assertTrue(latest_panels)

    def test_if_service_type_is_correct(self):
        ''' Test if service type is correct. '''
        service_type = self.hub.service_type
        self.assertTrue(service_type == '_zapp._tcp.local.')

    def test_get_all_panels(self):
        ''' Test if get_all_pannels returns some panels. '''
        panels = self.hub.get_all_panels()
        self.assertTrue(panels)

    def test_get_all_channels(self):
        ''' Test if get_all_channels returns some channesl. '''
        channels = self.hub.get_all_channels()
        self.assertTrue(channels)

    def test_get_all_light_channels(self):
        ''' Test if get_all_light_channels returns some lights. '''
        channels = self.hub.get_all_light_channels()
        self.assertTrue(channels)

    def test_get_all_channels_by_cat5(self):
        ''' Test if get_all_channels_by_cat returns some channels with cat 5. '''
        channels = self.hub.get_all_channels_by_cat(5)
        self.assertTrue(channels)

    def test_get_all_channels_by_cat35(self):
        ''' Test if get_all_channels_by_cat returns some channels with cat 35. '''
        channels = self.hub.get_all_channels_by_cat(35)
        self.assertTrue(not channels)

    def test_get_all_channels_by_group(self):
        ''' Test if get_all_channels_by_group not None. '''
        groups = self.hub.get_all_group()
        channels = self.hub.get_all_channels_by_group(groups[1])
        self.assertTrue(channels)

    def test_panel_name(self):
        ''' Test if panel_name not None. '''
        panels = self.hub.get_all_panels()
        for panel in panels:
            self.assertTrue(panel.panel_name)

    def test_panel_type(self):
        ''' Test if panel_type not None. '''
        panels = self.hub.get_all_panels()
        for panel in panels:
            self.assertTrue(panel.panel_type)

    def test_get_device_rssi(self):
        ''' Test if get_device_rssi not None. '''
        panels = self.hub.get_all_panels()
        for panel in panels:
            self.assertTrue(panel.get_device_rssi())

    def test_panel_to_string(self):
        ''' Test if to String not None. '''
        panels = self.hub.get_all_panels()
        for panel in panels:
            self.assertTrue(str(panel))

    def test_channel_to_string(self):
        ''' Test if to String not None. '''
        channels = self.hub.get_all_channels()
        channel = channels[0]
        self.assertTrue(str(channel))

    def test_channel_panel_name(self):
        ''' Test if panel_name returns not None. '''
        channels = self.hub.get_all_channels()
        channel = channels[0]
        self.assertTrue(channel.panel_name)

    def test_channel_panel_type(self):
        ''' Test if panel_type returns not None. '''
        channels = self.hub.get_all_channels()
        channel = channels[0]
        channel.panel_type
        self.assertTrue(True)

    def test_channel_panel_ip(self):
        ''' Test if panel_ip returns not None. '''
        channels = self.hub.get_all_channels()
        channel = channels[0]
        self.assertTrue(channel.panel_ip)

    def test_channel_panel_port(self):
        ''' Test if panel_port returns not None. '''
        channels = self.hub.get_all_channels()
        channel = channels[0]
        self.assertTrue(channel.panel_port)

    def test_channel_panel_url(self):
        ''' Test if panel_url returns not None. '''
        channels = self.hub.get_all_channels()
        channel = channels[0]
        self.assertTrue(channel.panel_url)

    def test_channel_turn_on_light(self):
        ''' Test if turn_on_light returns not None. '''
        channels = self.hub.get_all_light_channels()
        channel = channels[0]
        channel.turn_on_light()
        self.assertTrue(True)

    def test_channel_turn_off_light(self):
        ''' Test if turn_off_light returns not None. '''
        channels = self.hub.get_all_light_channels()
        channel = channels[0]
        channel.turn_off_light()
        self.assertTrue(True)

    def test_channel_toggle_light(self):
        ''' Test if toggle_light returns not None. '''
        channels = self.hub.get_all_light_channels()
        channel = channels[0]
        channel.toggle_light()
        self.assertTrue(True)

    def test_control_light_with_cat5(self):
        ''' Test if toggle_light returns not None. '''
        channels = self.hub.get_all_channels_by_cat(5)
        channel = channels[0]
        channel.toggle_light()
        self.assertTrue(True)