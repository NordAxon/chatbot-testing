import sys
# Used to import sibling modules
sys.path.append("..")

import abc
from typing import List, Dict
from config import valid_agents
from environment.conversation import Dialog, Message
from agents.interface import AbstractAgent
from config import *

class TestWorld():

    # TODO: Possible to assert that agents are subclasses of AbstractAgent?
    def __init__(self, test_agent: AbstractAgent, helper_agent: AbstractAgent):
        """ Object used to keep track of agents, dialogs and tests

        Args:
            test_agent (AbstractAgent): test_agent
            helper_agent (AbstractAgent): helper_agent
        """
        self.dialogs = []
        self._setup_tests()


    def _setup_tests(self):
        "Setup the list of tests from config parameters"
        self.test_case_list = None
        self.dialog_test_list = None
        raise NotImplementedError()


    def run_tests(self):
        # TODO: How do we save the metrics during testing? pandas df? 
        # TODO: Try, catch the tests in case they fail

        # Execute all of the test cases
        for test in self.test_case_list:
            dialogs = test.run_all()
            self.dialogs.extend(dialogs)

        # Do all of the general test
        for test in self.dialog_test_list:
            for dialog in self.dialogs:
                test.analyse(dialog)

        # Create a report from all dialogs
        # TODO: 
        raise NotImplementedError()
