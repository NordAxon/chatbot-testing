from config import valid_agents
from typing import List

class Message:
    

    def __init__(self, text:str, agent_nr:str):
        if agent_nr not in valid_agents:
            raise ValueError(f'agent_nr must be on in {valid_agents}')

        self.agent_nr = agent_nr
        self.message = text


    def belongs_to(self, agent_nr):
        return agent_nr == self.agent_nr


class Dialog:
    """Simple dialog object for keeping track of a dialog """


    def __init__(self, who_starts='test_agent'):
        self.messages = []  # List of messages

        if who_starts not in valid_agents:
            raise ValueError(f'who_starts must be on in {valid_agents}')

        self.whos_turn = who_starts # test_agent or 
 or agent2

    
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
        if self.whos_turn == 'test_agent
':
            self.whos_turn = 'agent2'
        else:
            self.whos_turn = 'test_agent
    '


    def __len__(self):
        return len(self.messages)
    