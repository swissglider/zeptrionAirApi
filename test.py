from zeptrionAirApi import ZeptrionAirHub

if __name__ == '__main__':
    hub = ZeptrionAirHub(5)
    #print(hub.getAllPanels())
    lights = hub.getAllLightChannels()
    lights[0].turn_on_light()
    print(lights[0])
    #print(hub.getAllChannels())
    #print(hub.getAllLightChannels())
    #print(hub.getAllGroup())
    #groups = hub.getAllGroup()
    #for group in groups:
    #    print("Channels in Group: " + str(group))
    #    print(hub.getAllChannelsByGroup(group))