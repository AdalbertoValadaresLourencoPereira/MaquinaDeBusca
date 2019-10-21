class imagem:


    imagens = []

    def __init__(self, nome, porcentagem ):
        self.nome = nome
        self.porcentagem = porcentagem

    def adicionaImagem(nomeImagem, porcentagemDeSemelhanca):

        imagem.nome = nomeImagem
        imagem.porcentagem = porcentagemDeSemelhanca

    def get_nome(self):
        return self._nome

    def get_porcentagem(self):
        return self._porcentagem
