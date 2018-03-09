=========== 
ZeptrionAir 
===========
This are the Classes to use the Zeptrion Air Lights etc. 
Zeptrion Air is a product from Feller.
Zeptrion Air Panel are switches for Light, Blinds etc.
A panel can have up to 8 switches. 
Each of this switches are called Channels.

1) ZeptrionAir Hub
------------------
The ZeptrionAir Hub handles all the ZeptrionAir Panel.
The Hub is searching (browse) the panels with mDNS (zeroconf).
If panels are found with mDNS the Hub is requesting the panels 
for all additional needed informations

2) ZeptrionAirPanel
-------------------
ZeptrionAirPanel is the panel that can have up to 8 channels (Switches)

3) ZeptrionAirChannel
---------------------
The ZeptrionAirChannel is on of the channel that are hold on a Panel
A Channel is Switch for example for a Light or Blinds etc.
With the ZeptrionAirChannel Class you can read the status
and control the device

Python compatibility
---------------------
Only working with Python 3 and above

Sample to use it:
-----------------
.. code-block:: python

    from zeptrionAirApi import ZeptrionAirHub

    hub = ZeptrionAirHub(3) #Initialize the ZeptrionAIrHub and browse for 5sec
    allZeptrionPanels = hub.get_all_panels() #returns all found panels
    allZeptrionChannels = hub.get_all_channels() #returns all found channels
    allLightChannels = hub.get_all_light_channels() #returns all found channels that are Light switches
    allGroups = hub.get_all_group() #returns all groups, that have been defined on the zeptrion app
    for group in allGroups:
        print("Channels in Group: " + str(group))
        print(hub.get_all_channels_by_group(group)) #returns all channles that are defined for that group

    channels = hub.get_all_channels_by_cat(1) #returns all found channels that are Light switches --> Category 1
    channel = channels[0] #pick the first light
    channel.toggle_light() #toggle the light
    channel.turn_on_light() #turn the light on
    channel.turn_off_light() #turn the light off

..