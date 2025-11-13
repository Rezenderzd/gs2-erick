class Candidato:                                                                                    #SALVA AS INFORMAÇÕES DOS CANDIDATOS
    def __init__(self, nome, cursos, linguas, linguagens,softskills, estilodetrabalho, notaFinal):
        self.nome =nome
        self.cursos = cursos
        self.linguas = linguas
        self.linguagens = linguagens
        self.softskills = softskills
        self.estilodetrabalho = estilodetrabalho
        self.notaFinal = notaFinal
    
    def informacoes(self):
        return{
            'nome':self.nome,
            'cursos':self.cursos,
            'linguas':self.linguas,
            'linguagens':self.linguagens,
            'softskills':self.softskills,
            'estilodetrabalho': self.estilodetrabalho,
            'notafinal' : self.notaFinal}