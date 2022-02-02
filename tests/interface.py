import sys
# Used to import sibling modules
sys.path.append("..")

import abc
from typing import List, Dict
from config import valid_agents
from environment.conversation import Dialog, Message
from agents import AbstractAgent


class AbstractTestCase(abc.ABC):
    """AbstractTestCase defines an interface for tests that construct a specific conversation
    
    E.g. A memory test where a testagent is given certain information and is later asked to remember that inforamtion
    
    """
    

    def __init__(self, 
        test_agent: AbstractAgent, 
        helper_agent: AbstractAgent, 
        nbr_dialogs: int
        ):

        self.test_agent = test_agent
        self.helper_agent = helper_agent
        self.nbr_dialogs = nbr_dialogs

        self.dialogs = []


    def get_dialogs(self):
        "Returns a list of dialogs"
        return self.dialogs

    
    def run_all(self) -> List[Dict]:
        """Runs self.nbr_dialogs tests and analyses them in order

        Returns:
            List[Dict]: metrics as a list of dicts
        """
        for _ in range(self.nbr_dialogs):
            dialog = self.create_dialog()
            self.dialogs.append(dialog)

        for dialog in self.dialogs:
            self.analyse(dialog)
            
        return self.dialogs


    @abc.Abstractmethod
    def create_dialog(self) -> Dialog:
        "Runs testcase"
        pass


    @abc.Abstractmethod
    def analyse(self, dialog: Dialog):
        """Performs analysis of outcome. 
        It should add the analysis metrics to the dialog by using dialog.add_metrics()"""
        pass


class AbstractDialogTest(abc.ABC):
    """A dialogtest is a test that is performed on any given dialog.
    
    E.g. a test where every line is tested for grammatical errors 
    """


    @abc.Abstractmethod
    def __init__(self):
        pass


    def analyse_batch(self, dialogs: List[Dialog]) -> List[Dict]:
        """Analyses the dialog

        Args:
            dialogs (List[Dialog]): List of dialog to analyse

        Returns:
            List[Dict]: List of dictionaries with metrics produced by test
        """

        for dialog in dialogs:
            metrics = self.analyse(dialog)
            dialog.update(metrics)
        
        return dialogs


    @abc.Abstractmethod
    def analyse(dialog: Dialog) -> Dict:
        """Analyses one dialog

        Args:
            dialog (Dialog): dialog to analyse

        Returns:
            Dict: dictonary with metrics from test
        """
        pass
