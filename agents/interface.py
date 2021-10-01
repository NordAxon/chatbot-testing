import sys
# Used to import sibling modules
sys.path.append("..")

import abc
from typing import List, Dict
from config import valid_agents
from environment.conversation import Dialog, Message


class AbstractAgent(abc.ABC): 
    """Abstract base class that defines interface for an agent """

    def __init__(self, agent_nr:str, starts:bool):
        if agent_nr not in valid_agents:
            raise ValueError(f'agent_nr must be on in {valid_agents}')

        self.agent_nr = agent_nr
        self.dialog = Dialog(agent_nr)
        self.ready_to_act = starts == True


    @abc.abstractmethod
    def initialize(self):
        "Start local server or otherwise initialize the agent so it's ready for testing"
    

    def observe(self, message: Message):
        " Add a message from another agent to the dialog"
        assert not message.belongs_to(self.agent_nr)

        #TODO: Add to dialog
        self.ready_to_act = True
        


    def self_observe(self):
        " Add its own message to the dialog. Should be called at the end of self.act() "
        #TODO: Assert right turn
        #TODO: Add to dialog

        self.ready_to_act = False
        

    @abc.abstractmethod
    def act(self) -> Message:
        " Define how to get a reply from the agent"
        pass
