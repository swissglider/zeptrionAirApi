"""This is the test for Smart Button."""

from zeptrionAirApi import ZeptrionAirHub
import json

hub = ZeptrionAirHub(3)  # Initialize the ZeptrionAIrHub and browse for 5sec
allZeptrionPanels = hub.get_all_panels()  # returns all found panels
# smartBtns = hub.get_all_smart_buttons() # returns all found smart buttons
# hub.set_all_smart_buttons_to_program_mode()

prog_elements = {}
prog_elements['prog_req_type'] = 'POST'
prog_elements['prog_url'] = '192.168.86.167'
prog_elements['prog_path'] = '/test'
prog_elements['prog_typ'] = 'application/json'
prog_elements['prog_header_field'] = ''
prog_elements['prog_port'] = '1880'
body = {}
body['state'] = 20
body['attributes'] = {}
body['attributes']['unit_of_measurement'] = '°C'
body['attributes']['friendly_name'] = 'Bathroom Temperature'
prog_elements['prog_body'] = json.dumps(body)

# result = hub.programm_smart_btn(prog_elements)
# print(result)
result = hub.get_panels_with_smart_button()
print(result)
