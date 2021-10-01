import abc
from typing import List, Dict
from config import valid_agents
from conversation import Dialog, Message
from agents import AbstractAgent

class TestWorld(abc.ABC):


    def __init__(self, test_agent: AbstractAgent, other_agent: AbstractAgent):
        """ Object used to keep track of agents, dialogs and tests

        Args:
            test_agent (AbstractAgent): test_agent
            other_agent (AbstractAgent): other_agent
        """
        self.report 
        self.dialogs = []
        pass


    @abc.abstractmethod
    def _setup_tests(self):
        "Setup the list of tests from config parameters"
        self.test_case_list = None
        self.dialog_test_list = None


    def run_tests(self):
        # TODO: How do we save the metrics during testing? pandas df? 

        # Execute all of the test cases
        for test in self.test_list:
            dialog = test.run()
            self.dialogs.append(dialog)
            metrics = test.analyse()

        # Do all of the general test
        for test in self.dialog_test_list:
            for dialog in self.dialogs:
                test.analyse(dialog)




