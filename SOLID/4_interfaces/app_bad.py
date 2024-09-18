from abc import ABC

class Document(ABC):
    @classmethod
    def load(self): pass

    @classmethod
    def view(self): pass

    @classmethod
    def format(self): pass

    @classmethod
    def calculate(self): pass

class PDF(Document):
    def load(self): pass

    def view(self): pass

    def format(self): pass # Importação obrigatoria que não sera utilizada

    def calculate(self): pass # Importação obrigatoria que não sera utilizada

class TxT(Document):
    def load(self): pass

    def view(self): pass

    def format(self): pass # Importação obrigatoria que não sera utilizada

    def calculate(self): pass # Importação obrigatoria que não sera utilizada

class Excel(Document):
    def load(self): pass

    def view(self): pass

    def format(self): pass 

    def calculate(self): pass 