"""
Support for ZeptrionAirPannel.

For more details about this Class, please refer to the documentation at
https://github.com/swissglider/zeptrionAirApi
"""
from .zeptrion_air_channel import ZeptrionAirChannel


class ZeptrionAirPanel:
    """
    Support for ZeptrionAirPanel.

    For more details about this Class, please refer to the documentation at
    https://github.com/swissglider/zeptrionAirApi
    """

    def __init__(self, panel_info, panel_name, panel_type):
        """Init the ZeptrionAirPanel."""
        import socket
        self._panel_name = panel_name
        self._panel_type = panel_type
        self._panel_ip = socket.inet_ntoa(panel_info.address)
        self._panel_port = panel_info.port
        url = "http://" + str(self.panel_ip)
        url += ":" + str(self.panel_port)
        self._panel_url = url
        self._panel_channels = []
        self.__read_panel_channels__()
        self._has_smart_buttons = False
        self.__read_smart_buttons__()

    @property
    def panel_name(self):
        """Return the Name from the panel."""
        return self._panel_name

    @property
    def panel_type(self):
        """Return the Type from the panel."""
        return self._panel_type

    @property
    def panel_ip(self):
        """Return the IP from the panel."""
        return self._panel_ip

    @property
    def panel_port(self):
        """Return the Port from the panel."""
        return self._panel_port

    @property
    def panel_url(self):
        """Return the URL from the panel."""
        return self._panel_url

    @property
    def panel_channels(self):
        """Return the Channels from the panel as List."""
        return self._panel_channels

    @property
    def has_smart_buttons(self):
        """Return the Smart Buttons from the panel as List."""
        return self._has_smart_buttons

    def __repr__(self):
        """Return a String representing the ZeptrionAirPanel."""
        return_string = "Panel Name: " + self.panel_name + '\n'
        return_string += "\tPanel URL: " + self.panel_url + '\n'
        for channel in self.panel_channels:
            return_string += "\t\tPanel URL: " + channel.channel_id
            return_string += "\tPanel Name: " + channel.channel_name + '\n'
        return_string += '\n'
        return return_string

    def __read_panel_channels__(self):
        """Read all the channels that panels has from the device."""
        import requests
        import xml.etree.ElementTree as ET
        device_info_response = requests.get(self.panel_url + "/zrap/chdes")
        if device_info_response.status_code == 200:
            root = ET.fromstring(device_info_response.text)
            # get Channel Informations
            for channel_xml in root:
                channel_info = {}
                channel_info['channel_id'] = channel_xml.tag
                channel_info['channel_name'] = channel_xml[0].text
                channel_info['channel_group'] = channel_xml[1].text
                channel_info['channel_icon'] = channel_xml[2].text
                channel_info['channel_type'] = channel_xml[3].text
                channel_info['channel_cat'] = channel_xml[4].text
                temp_channel = ZeptrionAirChannel(channel_info, self)
                self.panel_channels.append(temp_channel)

    def get_device_rssi(self):
        """
        Return the RSSSI from that panel.

        RSSI = (Received Signal Strength Indication)
        Checking the RSSI may help to fix connection problems!
        If the RSSI is below about -75 dBm
        then the connection may become unreliable
        and whenever it drops for too long the device
        will reboot to find a better connection.
        """
        import requests
        import xml.etree.ElementTree as ET
        device_info_response = requests.get(self.panel_url + "/zrap/rssi")
        if device_info_response.status_code == 200:
            root = ET.fromstring(device_info_response.text)
            return root[0].text
        return ''  # pragma: no cover

    def __read_smart_buttons__(self):
        """Return the Smart Buttons that panel has."""
        import requests
        import json
        device_info_response = requests.get(
            self.panel_url + "/zapi/smartfront/id")

        if device_info_response.status_code == 200:
            # button_info = json.loads(device_info_response.text)

            device_led_response = requests.get(
                self.panel_url + "/zapi/smartfront/led")
            if device_led_response.status_code == 200:
                buttons = json.loads(device_led_response.text)
                for button in buttons:
                    if(button):
                        self._has_smart_buttons = True
                        return

    async def programm_btn(self, prog_elements):  # noqa: D301
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
                    --> ex. "SOAPACTION:http://test/foo#MyMessage\r\n"
                :prog_elements['prog_port']
                    --> Port of the Webservice to be called
                :prog_elements['prog_body']
                    --> Body of the Webservice to be called
        """
        import aiohttp
        import requests
        import json
        url = self.panel_url + "/zapi/smartbt/prgm"
        payload = {'on': True}
        headers = {'content-type': 'application/json'}
        requests.post(url, data=json.dumps(payload), headers=headers)
        url = self.panel_url + "/zapi/smartbt/prgn"
        prgn_response = requests.get(url)
        if prgn_response.text and prgn_response.status_code == 200:
            result = json.loads(prgn_response.text)
            if result['prg']:
                async with aiohttp.ClientSession() as session:
                    url = self.panel_url + "/zapi/smartbt/prgs"
                    payload = [{
                        'req': prog_elements['prog_req_type'],
                        'loc': prog_elements['prog_url'],
                        'pth': prog_elements['prog_path'],
                        'typ': prog_elements['prog_typ'],
                        'hdr': prog_elements['prog_header_field'],
                        'prt': prog_elements['prog_port'],
                        'bdy': prog_elements['prog_body']
                    }]
                    headers = {'content-type': 'application/json'}
                    async with session.post(
                        url,
                        data=json.dumps(payload),
                        headers=headers
                    ) as response:
                        await response.text()
                        if response.status == 200:
                            return {
                                'changed': True,
                                'tried to change': False,
                                'status_code': response.status,
                                'text': response.text(),
                                'response': response
                            }
                        return {
                            'changed': False,
                            'tried to change': True,
                            'status_code': response.status,
                            'text': response.text(),
                            'response': response
                        }  # pragma: no cover
        else:
            return {
                'changed': False,
                'tried to change': True,
                'status_code': prgn_response.status_code,
                'text': prgn_response.text,
                'response': prgn_response
            }  # pragma: no cover
