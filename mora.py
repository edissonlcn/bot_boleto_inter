from datetime import datetime


class Mora:
    codigoMora = ""
    taxa = 0
    valor = 0
    data = ""

    def __init__(self, codigoMora, taxa, valor, data):
        self.codigoMora = codigoMora
        self.taxa = taxa
        self.valor = valor
        self.data = '' if str(data) == 'NaT' else data.strftime("%Y-%m-%d")
