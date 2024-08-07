from library_wrapper.wrapper import Wrapper

class TrieNetwork():
    def __init__(self, library, input_size, hidden_size, output_size):
        self.wrapper = Wrapper(library=library, input_size=input_size, hidden_size=hidden_size, output_size=output_size)

    def default_model(self):
        return self.wrapper.init_default_model()
    
    def get_criterion(self):
        return self.wrapper.get_criterion()
    
    def collect_inputs(self, inputs):
        return self.wrapper.model(inputs)
    
    def library(self):
        return self.wrapper.library