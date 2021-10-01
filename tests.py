import abc
from typing import List, Dict
from config import valid_agents
from conversation import Dialog, Message
from agents import AbstractAgent


class AbstractTestCase(abc.ABC):
    """AbstractTestCase defines an interface for tests that construct a specific conversation
    
    E.g. A memory test where a testagent is given certain information and is later asked to remember that inforamtion
    
    """
    

    def __init__(self, test_agent: AbstractAgent, other_agent: AbstractAgent):
        self.test_agent = test_agent
        self.other_agent = other_agent
        self.dialog = Dialog
        self.report = None


    def get_dialog(self):
        return self.dialog.get_dialog()


    @abc.abstractmethod
    def run(self) -> Dialog:
        "Runs testcase"
        pass


    @abc.abstractmethod
    def analyse(self) -> Dict:
        "Performs analysis of outcome"
        pass



class AbstractDialogTest(abc.ABC):
    """A dialogtest is a test that is performed on any given dialog.
    
    E.g. a test where every line is tested for grammatical errors 
    """


    @abc.abstractmethod
    def __init__(self):
        pass


    @abc.abstractmethod
    def analyse(self, dialog: Dialog) -> Dict:
        """Analyses the dialog

        Args:
            dialog (Dialog): Dialog to analyse

        Returns:
            Dict: Dictionary with metrics produced by test
        """
        pass
