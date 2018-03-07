from .ZeptrionAirPanel import ZeptrionAirPanel
""" 
ZeptrionAir 
This are the Classes to use the Zeptrion Air Lights etc.

Zeptrion Air is a product from Feller. (http://feller.ch)
Zeptrion Air Panel are switches for Light, Blinds etc.
A panel can have up to 8 switches. 
Each of this switches are called Channels.

So here we have:
1) ZeptrionAir Hub
The ZeptrionAir Hub handles all the ZeptrionAir Panel.
The Hub is searching (browse) the panels with mDNS (zeroconf).
If panels are found with mDNS the Hub is requesting the panels 
for all additional needed informations

2) ZeptrionAirPanel
ZeptrionAirPanel is the panel that can have up to 8 channels (Switches)

3) ZeptrionAirChannel
The ZeptrionAirChannel is on of the channel that are hold on a Panel
A Channel is Switch for example for a Light or Blinds etc.
With the ZeptrionAirChannel Class you can read the status
and control the device

Sample to use it:
https://github.com/swissglider/zeptrionAirApi
"""

import time

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
        self.__service_type__ = '_zapp._tcp.local.'
        self.__panels__ = {}
        self.__new_found_panels__ = {}
        self.browse(browseTime)
    
    def browse(self, browseTime=5):
        """
        browse is searching for new ZeptrionAirPanels over mDNS
        returns new found panels as list
        and adds new found to the panels list
            :param browseTime=5: -- this is the browse time in seconds
        """   
        from zeroconf import ServiceBrowser, Zeroconf
        zeroconf = Zeroconf()
        browser = ServiceBrowser(zeroconf, self.__service_type__, handlers=[self.__on_service_state_change__])
        time.sleep(browseTime)
        browser.cancel()
        zeroconf.close()
        return self.__new_found_panels__.values()

    def __on_service_state_change__(self, zeroconf, service_type, name, state_change):
        info = zeroconf.get_service_info(service_type, name)
        if name not in self.__panels__ :
            tempPanel = ZeptrionAirPanel(info, name, service_type, state_change)
            self.__panels__[name] = tempPanel
            self.__new_found_panels__[name] = tempPanel
    
    def getAllPanels(self):
        """
        returns all found panels as list
        """   
        return self.__panels__.values()
        
    def getAllChannels(self):
        """
        returns all found channels as list
        """ 
        temp_channels = []
        for device in self.__panels__.values():
            temp_channels.extend(device.service_channels)
        return list(set(temp_channels))

    def getAllLightChannels(self):
        """
        returns all found channels representing a light (cat=1) as list
        """ 
        return self.getAllChannelsByCat('1')
    
    def getAllChannelsByCat(self, cat):
        """
        returns all found channels representing the given category as list
            :param cat: -- the category to give back all channels
        """ 
        temp_channels_by_cat = []
        for device in self.__panels__.values():
            temp_channels = device.service_channels
            for temp_channel in temp_channels:
                if str(temp_channel.channel_cat) == str(cat):
                    temp_channels_by_cat.append(temp_channel) 
        return list(set(temp_channels_by_cat))
    
    def getAllChannelsByGroup(self, group_name):
        """
        Returns all the Channels that are configured on the zeptrion app to be in the given group as list
            :param group_name: -- the group to give back all channels
        """   
        temp_channels_by_group = []
        for device in self.__panels__.values():
            temp_channels = device.service_channels
            for temp_channel in temp_channels:
                if str(temp_channel.channel_group) == str(group_name):
                    temp_channels_by_group.append(temp_channel) 
        return list(set(temp_channels_by_group))
    
    def getAllGroup(self):
        """
        returns all found groups as list - Groups are configured on the zeptrion app
        """ 
        groups = []
        for device in self.__panels__.values():
            temp_channels = device.service_channels
            for temp_channel in temp_channels:
                groups.append(temp_channel.channel_group) 
        return list(set(groups))