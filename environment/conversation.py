import sys
# Used to import sibling modules
sys.path.append("..")

from config import valid_agents
from typing import List, Dict
import warnings

class Message:
    

    def __init__(self, text:str, agent_id:str):
        if agent_id not in valid_agents:
            raise ValueError(f'agent_id must be on in {valid_agents}')

        self.agent_id = agent_id
        self.text = text


    def belongs_to(self, agent_id):
        return agent_id == self.agent_id


class Dialog:
    """Simple dialog object for keeping track of a dialog """


    def __init__(self,
        label:str,
        who_starts: str = 'test_agent'
        ):
        
        if who_starts not in valid_agents:
            raise ValueError(f'who_starts must be on in {valid_agents}')

        self.messages = []  # List of messages
        self.label = label

        self.who_starts = who_starts # test_agent or helper_agent
        self.whos_turn = who_starts 

        self.metrics = {}

    
    def get_message_list(self) -> List[str]:
        """Returns a list of the messages """
        return [message.text for message in self.messages]


    def add_message(self, message: Message):
        """Adds message to self.dialog if it comes from the right agent

        Args:
            message (Message): Contains message and name of agent
        """
        assert message.belongs_to(self.whos_turn)
        self.messages.append(message)
        self._switch_expected_turn()


    def _switch_expected_turn(self):
        "Switches agent expected to act"
        if self.whos_turn == 'test_agent':
            self.whos_turn = 'helper_agent'
        else:
            self.whos_turn = 'test_agent'


    def __len__(self):
        return len(self.messages)
        

    def add_metrics(self, metrics: Dict):
        "Adds metrics to self.metrics"

        old_keys = self.metrics.keys()
        if any([new_key in old_keys for new_key in metrics.keys()]):
            warnings.warn('Found identical keys in metrics')
            raise NotImplementedError("Implement something that handles this case") #TODO
        else:
            self.metrics.update(metrics)
