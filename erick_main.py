from erick_pesos import Cursos, Linguagem, Linguas, SoftSkills, EstiloDeTrabalho
from erick_class import Candidato
from erick_repo import Repositorio

repo = Repositorio()



def procurando_cursos():                    
    curso_escolhido = input('Digite seu curso: ').lower()           #USUARIO DIGITA O CURSO ATUAL 
    if curso_escolhido in Cursos:                                   #SE O CURSO ESTIVER NO PARAMETRO DESEJADO
        peso = Cursos[curso_escolhido]                              #PESO = PESO ESTIPULADO EM ERICK_PESOS
    else:                                                           #SE NAO PESO SERA 0
        peso = 0

    return peso

def procurando_linguagem():
    Linguagem_escolhido = input('Digite sua Linguagem: ').lower()
    if Linguagem_escolhido in Linguagem:
        peso = Linguagem[Linguagem_escolhido]
    else:
        peso = 0

    return peso

def procurando_Linguas():
    Linguas_escolhido = input('Digite seu idioma secundario: ').lower()
    if Linguas_escolhido in Linguas:
        peso = Linguas[Linguas_escolhido]
    else:
        peso = 0

    return peso

def procurando_SoftSkills():
    SoftSkills_escolhido = input('Digite sua principal soft skill: ').lower()
    if SoftSkills_escolhido in SoftSkills:
        peso = SoftSkills[SoftSkills_escolhido]
    else:
        peso = 0

    return peso

def procurando_EstiloTrabalho():
    EstiloDeTrabalho_escolhido = input('Digite seu Estilo De Trabalho desjado: ').lower()
    if EstiloDeTrabalho_escolhido in EstiloDeTrabalho:
        peso = EstiloDeTrabalho[EstiloDeTrabalho_escolhido]
    else:
        peso = 0

    return peso

def main():                                             
    nome = input('seu nome: ')
    Cursos = procurando_cursos()
    peso_cursos = 3                                                                                 #PESO ESTIPULADO PELO GRUPO PARA O ARGUMENTO
    Linguas = procurando_Linguas()
    peso_linguas = 4
    Linguagem = procurando_linguagem()
    peso_linguagem = 8
    SoftSkills = procurando_SoftSkills()
    peso_softskill = 7
    EstiloDeTrabalho = procurando_EstiloTrabalho()
    peso_estilodetrabalho = 6
    nota = (Cursos*peso_cursos + Linguas*peso_linguas + Linguagem*peso_linguagem + 
            SoftSkills*peso_softskill+ EstiloDeTrabalho*peso_estilodetrabalho)/28                   #REALIZA O CALCULO PARA A "NOTA" DO CANDIDATO
    nota = round(nota,1)
    candidato = Candidato(nome, Cursos, Linguas, Linguagem, SoftSkills, EstiloDeTrabalho, nota)     #ADICIONA AS INFORMAÇÕES NA CLASSE
    convertendo_candidato = candidato.informacoes()
    repo.criandoCandidato(convertendo_candidato)                                                    #ADICIONA AS INFORMAÇÕES DO USUÁRIO NO BANCO DE DADOS
    print('deu bom')

main()
