class Multa:
    codigoMulta = ""
    taxa = 0
    valor = 0
    data = ""

    def __init__(self, codigoMulta, taxa, valor, data):
        self.codigoMulta = codigoMulta
        self.taxa = taxa
        self.valor = valor
        self.data = '' if str(data) == 'NaT' else data._date_repr
