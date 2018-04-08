"""This is a Sample how to use the zeptrion Air Api."""

from zeptrionAirApi import ZeptrionAirHub

# Initialize the ZeptrionAIrHub and browse for 5sec
hub = ZeptrionAirHub(3)
# returns all found panels
allZeptrionPanels = hub.get_all_panels()
# returns all found channels
allZeptrionChannels = hub.get_all_channels()
# returns all found channels that are Light switches
allLightChannels = hub.get_all_light_channels()
# returns all groups, that have been defined on the zeptrion app
allGroups = hub.get_all_group()
for group in allGroups:
    output_to_return = "Channels in Group: " + str(group)
    # returns all channles that are defined for that group
    hub.get_all_channels_by_group(group)

# returns all found channels that are Light switches --> Category 1
channels = hub.get_all_channels_by_cat(1)
# pick the first light
channel = channels[0]
# toggle the light
channel.toggle_light()
# turn the light on
channel.turn_on_light()
# turn the light off
channel.turn_off_light()
