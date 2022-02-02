import sys
# Used to import sibling modules
sys.path.append("..")

import abc
from typing import List, Dict
from config import valid_agents
from environment.conversation import Dialog, Message


class AbstractAgent(abc.ABC): 
    """Abstract base class that defines interface for an agent """

    def __init__(self, agent_id:str):
        if agent_id not in valid_agents:
            raise ValueError(f'agent_id must be on in {valid_agents}')

        self.agent_id = agent_id


    @abc.abstractmethod
    def initialize(self):
        "Start local server or otherwise initialize the agent so it's ready for testing"
        pass
    
        

    @abc.abstractmethod
    def _act(self, dialog) -> Message:
        " Define how to get a reply from the agent"
        pass


    def reply(self, dialog) -> Message:
        """Helper

        Args:
            dialog ([type]): [description]

        Returns:
            Message: [description]
        """

        assert dialog.whose_turn == self.agent_id
        return self._act(dialog)


