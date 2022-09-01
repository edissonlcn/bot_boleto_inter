class Desconto:
    codigoDesconto = ""
    taxa = 0
    valor = 0
    data = ""

    def __init__(self, codigoDesconto, taxa, valor, data):
        self.codigoDesconto = codigoDesconto
        self.taxa = 0 if str(taxa) == 'nan' else taxa
        self.valor = 0 if str(valor) == 'nan' else str(valor)
        self.data = '' if str(data) == 'NaT' or str(
            data) == 'nan' else data._date_repr
