#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import os
from tkinter import *
from tkinter import ttk

"""=========================== DEFINIÇÃO DE FUNÇÕES =================================================="""

"""
Fecha o arquivo passado como parametro
"""
def fecha_arquivo(file):
    file.close()
    
"""
Abre arquivo em forma de escrita com o semestre passado como parametro, para a pasta formatada
"""
def abre_arquivo_formatado(semestre):
    if os.path.isdir("CAGR/Output/{}/Formatado".format(semestre,semestre)): #diretório já existe
        pass
    else:
        os.mkdir("CAGR/Output/{}/Formatado".format(semestre,semestre))     #se não existe, cria diretório
        
    file = open("CAGR/Output/{}/Formatado/CAGR_formatado_{}.csv".format(semestre,semestre),"w",encoding='utf8')
    return file 
    
"""
Abre arquivo em forma de escrita com o semestre passado como parametro. Lista de inconsistencias
"""
def abre_arquivo_INCONSISTENCIA(semestre):
    if os.path.isdir("CAGR/Output/{}/Formatado".format(semestre,semestre)): #diretório já existe
        pass
    else:
        os.mkdir("CAGR/Output/{}/Formatado".format(semestre,semestre))     #se não existe, cria diretório
        
    file = open("CAGR/Output/{}/Formatado/CAGR_INCONSISTENCIAS_{}.csv".format(semestre,semestre),"w",encoding='utf8')
    return file

"""
Abre file em modo de leitura e le a coluna passada como parametro
"""
def le_arquivo(file,coluna):
    with open(file,'r') as stream:
        reader = csv.DictReader(stream)
        for row in reader:
            yield row[coluna]

"""
Cria um writer pra registrar no arquivo
"""
def escreve_arquivo(file,semestre):
    writer = csv.writer(file) #escritor do arquivo
    writer.writerow(["DISCIPLINAS","PROFESSORES","HORARIOS","TURMAS","VAGAS OCUPADAS", semestre]) #gera colunas no arquivo csv
    return writer

def escreve_arquivo_INCONSISTENCIA(file,semestre):
    writer = csv.writer(file)
    writer.writerow(["Siglas","Professor","Justificativas","Horario","Agrupamentos","VagasOcupadasNaTurma","VagasOcupadasAgrupamento","Justificativas"])
    return writer

"""======================================================================================================="""
"""======================================== MAIN ========================================================="""
"""======================================================================================================="""

class Application: 
    def __init__(self, master=None):
        self.fonte =("Verdana", "8")
        
        """titulo"""
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        
        """Informar o semestre"""
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        
        """botao gerar inconsistencias"""
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 10
        self.container3.pack()
        
        self.titulo = Label(self.container1, text="Inconsistências CAGR")
        self.titulo["font"] = ("Calibri", "12", "bold")
        self.titulo.pack()
        
        self.lblsemestre = Label(self.container2, text="Semestre:",
                                 font=self.fonte, width=10)
        self.lblsemestre.pack(side=LEFT)
        
        self.txtsemestre = Entry(self.container2)
        self.txtsemestre["width"] = 25
        self.txtsemestre["font"] = self.fonte
        self.txtsemestre.pack(side=LEFT)
        
        self.bntInsert = Button(self.container3, text="Gerar Inconsistências",
                                font=self.fonte, width=25)
        self.bntInsert["command"] = self.Gerar_Inconsistencias
        self.bntInsert.pack(side=LEFT)
        
        self.sair = Button(self.container3)
        self.sair["text"] = "Sair"
        self.sair["font"] = self.fonte
        self.sair["width"] = 5

    def Gerar_Inconsistencias(self):
        """================================ DECLARAÇÃO DE VARIÁVEIS =============================================="""
        semestre = self.txtsemestre.get()
        materia = []
        disciplina = [] #inicializa uma lista
        professor = []
        horario = []
        turmas = []
        vagas_ofertadas = []
        vagas_ocupadas = []
        alunos_especiais = []
        saldo_vagas = []
        
        if os.path.isdir("CAGR/Output/{}".format(semestre)):
            pass
        else:
            print("Fazer Scraping do semestre antes de gerar inconsistências")
            return
        
        """================================ LEITURA DO ARQUIVO ==================================================="""
        
        #Le a coluna de DISCIPLINAS do arquivo
        for i in le_arquivo("CAGR/Output/{}/CAGR_{}.csv".format(semestre,semestre),"Matérias"):
            materia.append(i) #adiciona os elementos na lista
        
        #Le a coluna de DISCIPLINAS do arquivo
        for i in le_arquivo("CAGR/Output/{}/CAGR_{}.csv".format(semestre,semestre),'Disciplinas'):
            disciplina.append(i) #adiciona os elementos na lista
            
        #Le a coluna de PROFESSORES do arquivo
        for i in le_arquivo("CAGR/Output/{}/CAGR_{}.csv".format(semestre,semestre),'Professores'):
            professor.append(i)
            
        #Le a coluna HORARIOS do arquivo
        for i in le_arquivo("CAGR/Output/{}/CAGR_{}.csv".format(semestre,semestre),'Horários'):
            horario.append(i) 
        
        #Le a coluna TURMAS do arquivo  
        for i in le_arquivo("CAGR/Output/{}/CAGR_{}.csv".format(semestre,semestre),'Turmas'):
            turmas.append(i)
        
        #Le a coluna de VAGAS OFERTADAS do arquivo
        for i in le_arquivo("CAGR/Output/{}/CAGR_{}.csv".format(semestre,semestre),'Vagas Ofertadas'):
            vagas_ofertadas.append(i)
        vagas_ofertadas = list(map(int,vagas_ofertadas)) #transforma a lista em uma lista de int
        
        #Le a coluna VAGAS OCUPADAS do arquivo
        for i in le_arquivo("CAGR/Output/{}/CAGR_{}.csv".format(semestre,semestre),"Vagas Ocupadas"):
            vagas_ocupadas.append(i)
        vagas_ocupadas = list(map(int,vagas_ocupadas))
        
        #Le a coluna ALUNOS ESPECIAIS do arquivo
        for i in le_arquivo("CAGR/Output/{}/CAGR_{}.csv".format(semestre,semestre),"Alunos Especiais"):
            alunos_especiais.append(i)
        alunos_especiais = list(map(int,alunos_especiais))
        
        #Le a coluna SALDO VAGAS do arquivo
        for i in le_arquivo("CAGR/Output/{}/CAGR_{}.csv".format(semestre,semestre),"Saldo Vagas"):
            saldo_vagas.append(i)
        for i in range(len(saldo_vagas)):  #converte os elementos da lista para inteiro, turmas LOTADAS representadas pelo inteiro 10000
            if saldo_vagas[i] == "LOTADA":
                saldo_vagas[i] = int(10000)
            else:
                saldo_vagas[i] = int(saldo_vagas[i])
                
        """================================ AJUSTES E CRIAÇÃO DO ARQUIVO =============================================="""
        
        file_INCONSISTENCIA = abre_arquivo_INCONSISTENCIA(semestre)
        writer_INCONSISTENCIA = escreve_arquivo_INCONSISTENCIA(file_INCONSISTENCIA,semestre)
        
        tam = len(disciplina) #tamanho das listas disciplina, professor e horario sao iguais
        
        for s in range(tam):
            #materia[s] -> tem o formato: Física III *ENGENHARIA NAVAL [Campus Joinville]
            materia[s] = materia[s].replace('[Campus Joinville]','')#substitui a parte final da string por vazio
            materia[s] = (materia[s].split('*'))[1] #para remover a parte inicial e pegar só o curso
        
        """==================================== AGRUPANDO TURMAS =================================================="""
        
        armazena = [] #turmas agrupadas
        
        tudo = list(zip(materia,disciplina,professor,horario,turmas,vagas_ocupadas)) #cria um dicionario associando tudo com materia, disciplina, professor, horario, turmas e vagas_ocupadas
        for i in range(len(tudo)): #tudo mesmo tamanho que tam
            if(vagas_ocupadas[i] < 12):
                #Agrupa turmas de mesma disciplina, mesmo professor e mesmo horario
                junto = list(filter(lambda d : tudo[d][1] == disciplina[i] and tudo[d][2] == professor[i] and tudo[d][3] == horario[i], range(len(tudo))))
                if(len(junto) != 1): #mais de uma turma, agrupar
                    armazena.append(junto)
        
        """=========================== RETIRANDO ELEMENTOS REPETIDOS =================================================="""
        i = 0
        j = 0
        tam_armazena = len(armazena)
        while(i < tam_armazena):
            try:
                while(j < tam_armazena):
                    try:
                        if(i != j): #para não checar o elemento com ele mesmo
                            if(armazena[i] == armazena[j]): #elementos iguais
                                armazena.pop(j) #retira o elemento
                                if(j < i): #se estiver para tras na lista, volta uma posicao no i
                                    i -= 1
                                j -= 1 #retirou um elemento, volta uma posicao
                        j += 1
                    except IndexError:
                        break
                i += 1
                j = 0
            except IndexError:
                break
        
        
        """================================ VÁRIAVEIS PARA ESCRITA DO ARQUIVO =========================================="""
        siglas = [] #lista
        professores = []
        horarios = []
        turmas = {} #dicionario
        turmas_oficial = ""
        vagas = {}
        vagas_oficial = ""
        vagas_total = 0
        cursos = {}
        cursos_oficial = ""
        materia = ""
        
        
        """ OBS.:
        print(armazena) #todas as posicoes onde tem agrupamento, lista de uma lista
        print(armazena[0]) #lista com as posicoes agrupadas
        print(armazena[0][0]) #posicao de um agrupamento
        print(tudo[armazena[0][0]]) #todas informacoes sobre a turma
        print(tudo[armazena[0][0]][0]) #curso
        print(tudo[armazena[0][0]][1]) #sigla
        print(tudo[armazena[0][0]][2]) #professor
        print(tudo[armazena[0][0]][3]) #horario
        print(tudo[armazena[0][0]][4]) #turma
        print(tudo[armazena[0][0]][5]) #numero de vagas
        """
        
        """================================ ESCRITA NO ARQUIVO =============================================="""
        for i in range(len(armazena)):
            siglas.append(tudo[armazena[i][0]][1])
            professores.append(tudo[armazena[i][0]][2])
            horarios.append(tudo[armazena[i][0]][3])
            for j in range(len(armazena[i])):
                """----------------- turmas ---------------------"""
                turmas[i] = armazena[i]
                if(turmas_oficial == ""):
                    turmas_oficial += tudo[turmas[i][j]][4]
                else:
                    turmas_oficial += ", " + tudo[turmas[i][j]][4]
                """------------------ vagas -----------------------"""
                vagas[i] = armazena[i]
                vagas_total += tudo[vagas[i][j]][5]
                if(vagas_oficial == ""):
                    vagas_oficial += str(tudo[vagas[i][j]][5])
                else:
                    vagas_oficial += ", " + str(tudo[vagas[i][j]][5])
                """-------------------- cursos ----------------------"""
                cursos[i] = armazena[i]
                if(cursos_oficial == ""):
                    cursos_oficial += tudo[cursos[i][j]][0]
                else:
                    cursos_oficial += ", " + tudo[cursos[i][j]][0]
                    
            materia = ("A disciplina é ofertada para {} cursos de graduação: ".format(len(armazena[i])) + cursos_oficial + ". Pelo fato de ser uma disciplina compartilhada entre {} cursos e por haver alunos regulares na fase, ela deve ser ofertada pois, somando as diferentes turmas, o  número de matriculados é igual a ".format(len(armazena[i])) + str(vagas_total))
            #escreve no arquivo
            writer_INCONSISTENCIA.writerow([siglas[i],professores[i],materia,horarios[i],turmas_oficial,vagas_oficial,vagas_total])
            #zera as variaveis
            turmas_oficial = ""
            vagas_oficial = ""
            cursos_oficial = ""
            vagas_total = 0
        
        fecha_arquivo(file_INCONSISTENCIA)
        
        print("Inconsistências registradas")
 
def inconsistencias():
    root = Tk()
    root.title("Inconsistências")
    root.geometry('600x300')
    menubar = Menu(root)
    
    root.config(menu=menubar)
    Application(root)
    root.mainloop()