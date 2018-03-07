from .ZeptrionAirChannel import ZeptrionAirChannel
class ZeptrionAirPanel:
    """
    ZeptrionAirPanel is the panel that can have up to 8 channels (Switches)
    """ 
    def __init__(self, service_info, service_name, service_type, state_change):
        import socket
        self.service_info = service_info
        self.service_name = service_name
        self.service_type = service_type
        self.state_change = state_change
        self.service_ip = socket.inet_ntoa(self.service_info.address)
        self.service_port = self.service_info.port
        self.service_weight = self.service_info.weight
        self.service_priority = self.service_info.priority
        self.service_server = self.service_info.server
        self.service_properties = self.service_info.properties
        self.service_url = "http://" + str(self.service_ip) + ":" + str(self.service_port)
        self.service_channels = []
        self.__readServiceChannels__()

    def __repr__(self):
        returnSTR = "Service Name: " + self.service_name + '\n'
        returnSTR += "\tService URL: " + self.service_url + '\n'
        for channel in self.service_channels:
            returnSTR += "\t\tService URL: " + channel.channel_id
            returnSTR += "\tService Name: " + channel.channel_name  + '\n'
        returnSTR += '\n'
        return returnSTR
    
    def __readServiceChannels__(self):
        import requests
        import xml.etree.ElementTree as ET
        device_Info_Response = requests.get(self.service_url + "/zrap/chdes")
        if device_Info_Response.status_code == 200:
            root = ET.fromstring(device_Info_Response.text)
            # get Channel Informations
            for channel_XML in root:
                temp_channel = ZeptrionAirChannel(channel_XML, self.service_ip, self.service_port, self.service_url, self.service_name, self.service_type)
                self.service_channels.append(temp_channel)

    def getDeviceRSSI(self):
        """ 
        This service returns the current RSSI (Received Signal Strength Indication) of a device. 
        Checking the RSSI may help to fix connection problems! 
        If the RSSI is below about -75 dBm then the connection may become unreliable 
        and whenever it drops for too long the device will reboot to find a better connection.
        """ 
        import requests
        import xml.etree.ElementTree as ET
        device_Info_Response = requests.get(self.service_url + "/zrap/rssi")
        if device_Info_Response.status_code == 200:
            root = ET.fromstring(device_Info_Response.text)
            return root[0].text
        return 0