class Mensagem:
    linha1 = ""
    linha2 = ""
    linha3 = ""
    linha4 = ""
    linha5 = ""

    def __init__(self, linha1, linha2, linha3, linha4, linha5):
        self.linha1 = linha1
        self.linha2 = '' if str(linha2) == 'nan' else linha2
        self.linha3 = '' if str(linha3) == 'nan' else linha3
        self.linha4 = '' if str(linha4) == 'nan' else linha4
        self.linha5 = '' if str(linha5) == 'nan' else linha5
