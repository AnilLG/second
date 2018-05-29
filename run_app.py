from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-372220181382-370632665792-371109094596-d6a49836b7e9ba22b2ea23535762cb7d', #app verification token
							'xoxb-372220181382-371472459029-781rCwbF5dnVoFRxeHBkJToE', # bot verification token
							'BCnIsRF1pfZsr80ZFW3nwBbc', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))