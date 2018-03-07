class ZeptrionAirChannel:
    def __init__(self, channel_XML, service_ip, service_port, service_url, device_name, device_type,):
        self.channel_id = channel_XML.tag
        self.channel_name = channel_XML[0].text
        self.channel_group = channel_XML[1].text
        self.channel_icon = channel_XML[2].text
        self.channel_type = channel_XML[3].text
        self.channel_cat = channel_XML[4].text
        self.channel_ip = service_ip
        self.channel_port = service_port
        self.channel_url = service_url
        self.channel_device_name = device_name
        self.channel_device_type = device_type
    '''
    Cat:
        -1: Not configured
         1: Light
         5: Storen auf/ab
    '''

    def __repr__(self):
        return_str =  "ID: " + str(self.channel_id) + '\n'
        return_str += "\tName: " + str(self.channel_name) + '\n'
        return_str += "\tGroup: " + str(self.channel_group) + '\n'
        return_str += "\tIcon: " + str(self.channel_icon) + '\n'
        return_str += "\tType: " + str(self.channel_type) + '\n'
        return_str += "\tCat: " + str(self.channel_cat) + '\n'
        return_str += "\tIP: " + str(self.channel_ip) + '\n'
        return_str += "\tState: " + str(self.update()) + '\n'
        return_str += '\n'
        return return_str 

    def update(self):
        """
        Updates the real status of the channel switch
        """ 
        import requests
        import xml.etree.ElementTree as ET
        device_Info_Response = requests.get(self.channel_url + "/zrap/chscan/" + self.channel_id)
        if device_Info_Response.status_code == 200:
            root = ET.fromstring(device_Info_Response.text)
            if root[0][0].text == '100':
                return True
            else :
                return False

    def turn_on_light(self):
        """
        Turns the real light switch off
        """ 
        self.__control_light("cmd=on")

    def turn_off_light(self):
        """
        Turns the real light switch off
        """ 
        self.__control_light("cmd=off")
       
    def toggle_light(self):
        """
        Toggles the real light switch
        """
        self.__control_light("cmd=toggle")
    
    def __control_light(self, payload):
        if str(self.channel_cat) == '1':
            import requests
            requests.post(self.channel_url + "/zrap/chctrl/" + self.channel_id, data=payload)
            self.state = self.update()