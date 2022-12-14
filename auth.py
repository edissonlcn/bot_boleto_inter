import requests


class Auth:
    access_token = ""
    token_type = ""
    expires_in = ""
    scope = ""
    client_id = ""
    client_secret = ""
    scope = ""
    grant_type = "client_credentials"
    token_boleto_write = ""
    token_boleto_read = ""

    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

    def generate_token_boleto_write(self, scope):
        request_body = "client_id={0}&client_secret={1}&scope={2}&grant_type={3}".format(
            self.client_id, self.client_secret, scope, self.grant_type)
        cert_file_path = "Inter API_Certificado.crt"
        key_file_path = "Inter API_Chave.key"
        cert = (cert_file_path, key_file_path)
        response = requests.post("https://cdpj.partners.bancointer.com.br/oauth/v2/token",
                                 headers={
                                     "Content-Type": "application/x-www-form-urlencoded"},
                                 data=request_body, cert=cert)
        self.token_boleto_write = response.json().get("access_token")

    def generate_token_boleto_read(self, scope):
        request_body = "client_id={0}&client_secret={1}&scope={2}&grant_type={3}".format(
            self.client_id, self.client_secret, scope, self.grant_type)
        cert_file_path = "Inter API_Certificado.crt"
        key_file_path = "Inter API_Chave.key"
        cert = (cert_file_path, key_file_path)
        response = requests.post("https://cdpj.partners.bancointer.com.br/oauth/v2/token",
                                 headers={
                                     "Content-Type": "application/x-www-form-urlencoded"},
                                 data=request_body, cert=cert)
        self.token_boleto_read = response.json().get("access_token")
