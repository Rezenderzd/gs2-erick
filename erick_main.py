from erick_pesos import Cursos, Linguagem, Linguas, SoftSkills, EstiloDeTrabalho
from erick_class import Candidato
from erick_repo import Repositorio

repo = Repositorio()


def menu():
    condicao = True
    while condicao:
        print("1 Cadastrar o usuário")
        print("2 Exibir ranking")
        print("0 Sair do programa")
        escolha = int(input("Escolha o que deseja: "))
        if escolha==1:
            main()
        elif escolha == 2:
            ver_ranking()
        elif escolha == 0:
            print("Fechando programa")
            condicao = False
        else:
            print("Escolha uma opcao valida")
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
    EstiloDeTrabalho_escolhido = input('Digite seu estilo de trabalho desjado(presencial/hibrido/remoto): ').lower()
    if EstiloDeTrabalho_escolhido in EstiloDeTrabalho:
        peso = EstiloDeTrabalho[EstiloDeTrabalho_escolhido]
    else:
        peso = 0

    return peso

def ver_ranking():
    lista_candidatos = repo.candidats_db()
    if not lista_candidatos:
        print("Nenhum candidato cadastrado")
        return
    lista_candidatos.sort(key=lambda c: c['notafinal'], reverse=True)

    print(f"\n## | {'Nome':<20} | {'Nota':<5}")
    print("-" * 35)
    for i, usuario in enumerate(lista_candidatos):
        print(f"{i+1:02d} | {usuario['nome']:<20} | {usuario['notafinal']:<5}")
    print("-" * 35)

def main():                                          
    nome = input('Seu nome: ').strip().lower()
    lista_usuarios = repo.candidats_db()

    for u in lista_usuarios:
        if u["nome"].strip().lower() == nome:
            print('Este nome já está sendo utilizado em outro cadastro')
            return menu()


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
    escolha = input('Usuário cadastrado. Ver ranking?(s/n)')
    if escolha=='s':
        ver_ranking()
    else:
        menu()

menu()
