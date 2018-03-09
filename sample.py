from zeptrionAirApi import ZeptrionAirHub

hub = ZeptrionAirHub(3) #Initialize the ZeptrionAIrHub and browse for 5sec
allZeptrionPanels = hub.get_all_panels() #returns all found panels
allZeptrionChannels = hub.get_all_channels() #returns all found channels
allLightChannels = hub.get_all_light_channels() #returns all found channels that are Light switches
allGroups = hub.get_all_group() #returns all groups, that have been defined on the zeptrion app
for group in allGroups:
    output_to_return = "Channels in Group: " + str(group)
    hub.get_all_channels_by_group(group) #returns all channles that are defined for that group

channels = hub.get_all_channels_by_cat(1) #returns all found channels that are Light switches --> Category 1
channel = channels[0] #pick the first light
channel.toggle_light() #toggle the light
channel.turn_on_light() #turn the light on
channel.turn_off_light() #turn the light off