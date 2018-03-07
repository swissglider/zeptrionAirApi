## ZeptrionAir

This are the Classes to use the Zeptrion Air Lights etc. Zeptrion Air is
a product from Feller. Zeptrion Air Panel are switches for Light, Blinds
etc. A panel can have up to 8 switches. Each of this switches are called
Channels.

### 1) ZeptrionAir Hub

The ZeptrionAir Hub handles all the ZeptrionAir Panel. The Hub is
searching (browse) the panels with mDNS (zeroconf). If panels are found
with mDNS the Hub is requesting the panels for all additional needed
informations

### 2) ZeptrionAirPanel

ZeptrionAirPanel is the panel that can have up to 8 channels (Switches)

### 3) ZeptrionAirChannel

The ZeptrionAirChannel is on of the channel that are hold on a Panel A
Channel is Switch for example for a Light or Blinds etc. With the
ZeptrionAirChannel Class you can read the status and control the device

### Sample to use it:

``` python
from zeptrionAirApi import ZeptrionAirHub

hub = ZeptrionAirHub(5) #Initialize the ZeptrionAIrHub and browse for 5sec
allZeptrionPanels = hub.getAllPanels() #returns all found panels
allZeptrionChannels = hub.getAllChannels() #returns all found channels
allLightChannels = hub.getAllLightChannels() #returns all found channels that are Light switches
allGroups = hub.getAllGroup() #returns all groups, that have been defined on the zeptrion app
for group in allGroups:
    print("Channels in Group: " + str(group))
    print(hub.getAllChannelsByGroup(group)) #returns all channles that are defined for that group
```
