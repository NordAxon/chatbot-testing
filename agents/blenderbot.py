from interface import AbstractAgent
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from environment.conversation import Dialog, Message


class BlenderBot(AbstractAgent):

    def __init__(self,
        agent_id:str,
        starts:bool,
        nbr_messages_for_context: int,
        model_name="facebook/blenderbot_small-90M"
        ):
        super().__init__(agent_id, starts)

        self.model_name = model_name
        self.tokenizer = None
        self.model = None
        self.initialize()


    def initialize(self):
        """Loads transformer model and tokenizer
        """
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model_name)

    
    def _get_context_string(self, nbr_messages: int) -> str:
        """Returns a string with the latest nbr_messages separated with newlines. 

        Args:
            nbr_messages (int): number of messages to include

        Returns:
            context (str): dialog history
        """
        messages = self.dialog.get_message_list()
        total_nbr_messages = len(messages)
        context = ''
        for i in range(total_nbr_messages - nbr_messages, total_nbr_messages):
            message = messages[i]
            context = context + message.text + '\n'

        return context


    def _act(self): 
        "Huggingface specific "
        context = self._get_context_string(self.nbr_messages_for_context)
        inputs = self.tokenizer(context, return_tensors='pt')
        output = self.model.generate(**inputs)
        text = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return Message(text=text, agent_id=self.agent_id)
 