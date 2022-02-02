import sys
# Used to import sibling modules
sys.path.append("..")

from agents.interface import AbstractAgent
from interface import AbstractTestCase
from environment.conversation import Dialog, Message


init_message1 = 'Hello! Welcome to your interview. My name is Emely and I will be interviewing you today.'


class NormalConversation(AbstractTestCase):

    def __init__(self, 
        test_agent: AbstractAgent, 
        helper_agent: AbstractAgent, 
        nbr_dialogs: int,
        dialog_length: int = 10
    ):

        super().__init__(test_agent, helper_agent, nbr_dialogs)
        self.dialog_length = dialog_length


    def create_dialog(self) -> Dialog:

        dialog = self._setup_dialog()

        # Simply let both agents talk back and forth
        for _ in range(self.dialog_length):
            
            dialog = self.both_agents_reply(dialog)

        return dialog


        
    def both_agents_reply(self, dialog: Dialog) -> Dialog:
        """Can be used to generate one conversation turn between the two agents

        Args:
            test_agent (AbstractAgent): [description]
            helper_agent (AbstractAgent): [description]
            dialog (Dialog): [description]

        Returns:
            Dialog: [description]
        """

        # Test agent starts
        if dialog.whos_turn == 'test_agent':

            message = self.test_agent.reply(dialog)
            dialog.add_message(message)

            message = self.helper_agent.reply(dialog)
            dialog.add_message(message)

        # Helper agent starts
        else:

            message = self.helper_agent.reply(dialog)
            dialog.add_message(message)

            message = self.test_agent.reply(dialog)
            dialog.add_message(message)

        return dialog


    def _setup_dialog(self) -> Dialog:

        dialog = Dialog(label='NormalTest', who_starts='test_agent')
        message = Message(text=init_message1, agent_id='test_agent')
        dialog.add_message(message)

        return dialog

    
    def analyse(self):
        "No specific test for this"
        pass


    




    # def test_agent(self, insert_message) -> Dialog:

    #     if dialog.who_starts == 'test_agent':
    #         message = test_agent.reply(dialog)
    #         dialog.add_message(message)

    #         message = Message(text=insert_message)
    #         dialog.add_message(message)

    #     else:
    #         message = Message(text=insert_message)
    #         dialog.add_message(message)

    #         message = test_agent.reply(dialog)
    #         dialog.add_message(message)

    #     return
