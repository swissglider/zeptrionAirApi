"""
Support for ZeptrionAirHub.

For more details about this Class, please refer to the documentation at
https://github.com/swissglider/zeptrionAirApi
"""
import time
from .zeptrion_air_panel import ZeptrionAirPanel


class ZeptrionAirHub:
    """
    The ZeptrionAir Hub handles all the ZeptrionAir Panels.

    The Hub is searching (browse) the panels with mDNS (zeroconf).
    If panels are found with mDNS the Hub is requesting the panels
    for all additional needed informations.

    In the initialization it browses already the first time.
    On the
    """

    def __init__(self, browseTime=5):
        """
        Init the ZeptrionAirHub.

            :param browseTime=5: -- this is the browse time in seconds
        """
        self._service_type = '_zapp._tcp.local.'
        self._panels = {}
        self._new_found_panels = {}
        self.browse(browseTime)

    @property
    def latest_found_panels(self):
        """Return the latest found panels as Dic."""
        return self._new_found_panels

    @property
    def all_found_panels(self):
        """Return all found panels as Dic."""
        return self._panels

    @property
    def service_type(self):
        """Return all found panels."""
        return self._service_type

    def browse(self, browse_time=5):
        """
        Browse is searching for new ZeptrionAirPanels over mDNS.

        returns new found panels as list
        and adds new found to the panels list
            :param browse_time=5: -- this is the browse time in seconds
        """
        from zeroconf import ServiceBrowser, Zeroconf
        zeroconf = Zeroconf()
        browser = ServiceBrowser(
            zeroconf, self.service_type,
            handlers=[self._on_service_state_change])
        time.sleep(float(browse_time))
        browser.cancel()
        zeroconf.close()
        return self._new_found_panels.values()

    def _on_service_state_change(
            self, zeroconf, service_type, name, state_change):
        info = zeroconf.get_service_info(service_type, name)
        state_change = state_change
        if name not in self._panels:
            temp_panel = ZeptrionAirPanel(info, name, service_type)
            self._panels[name] = temp_panel
            self._new_found_panels[name] = temp_panel

    def get_all_panels(self):
        """Return all found panels as list."""
        return self._panels.values()

    def get_all_channels(self):
        """Return all found channels as list."""
        temp_channels = []
        for panel in self._panels.values():
            temp_channels.extend(panel.panel_channels)
        return list(set(temp_channels))

    def get_all_light_channels(self):
        """Return all found channels representing a light (cat=1) as list."""
        return self.get_all_channels_by_cat('1')

    def get_all_channels_by_cat(self, cat):
        """
        Return all found channels representing the given category as list.

            :param cat: -- the category to give back all channels
        """
        temp_channels_by_cat = []
        for panel in self._panels.values():
            temp_channels = panel.panel_channels
            for temp_channel in temp_channels:
                if str(temp_channel.channel_cat) == str(cat):
                    temp_channels_by_cat.append(temp_channel)
        return list(set(temp_channels_by_cat))

    def get_all_channels_by_group(self, group_name):
        """
        Return all the Channels belowing to that group.

        Groups are configured on the zeptrion app
            :param group_name: -- the group to give back all channels
        """
        temp_channels_by_group = []
        for panel in self._panels.values():
            temp_channels = panel.panel_channels
            for temp_channel in temp_channels:
                if str(temp_channel.channel_group) == str(group_name):
                    temp_channels_by_group.append(temp_channel)
        return list(set(temp_channels_by_group))

    def get_all_group(self):
        """
        Return all found groups as list.

        Groups are configured on the zeptrion app
        """
        groups = []
        for panel in self._panels.values():
            temp_channels = panel.panel_channels
            for temp_channel in temp_channels:
                groups.append(temp_channel.channel_group)
        return list(set(groups))

    def get_panels_with_smart_button(self):
        """Return all Panels that have smart buttons."""
        panel_with_smt_btn = []
        for panel in self.get_all_panels():
            if panel.has_smart_buttons:
                panel_with_smt_btn.append(panel)
        return panel_with_smt_btn

    def programm_smart_btn(self, prog_elements):  # noqa: D301
        """
        Set the pressed Smart Buttons with the given program.

            :param prog_elements: -- dictornary with the following parameter
                :prog_elements['prog_req_type']
                    --> Type for the Webservice to be called
                    --> ex. POST/GET/PUT/DELETE
                :prog_elements['prog_url']
                    --> Url of the Webservice to be called
                :prog_elements['prog_path']
                    --> Path
                :prog_elements['prog_typ']
                    --> Type of the Webservice to be called
                    --> ex. application/json
                :prog_elements['prog_header_field']
                    --> individual HTTP header field
                    --> ex. 'SOAPACTION:http://test/foo#MyMessage\r\n'
                :prog_elements['prog_port']
                    --> Port of the Webservice to be called
                :prog_elements['prog_body']
                    --> Body of the Webservice to be called
        """
        import asyncio
        program_mode = [
            panel.programm_btn(prog_elements)
            for panel in self.get_panels_with_smart_button()
        ]
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(asyncio.gather(*program_mode))
        return result
