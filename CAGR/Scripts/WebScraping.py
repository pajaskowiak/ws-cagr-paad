# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
import csv
from selenium.common.exceptions import NoSuchElementException
import os

entrada = ""

"""
Função que faz o scraping da pagina
PARÂMETROS:
    - Browser
    - Escritor do arquivo
    - Semestre selecionado
"""
def paginaCagr(browser, writer,semestre,mode):
    if(entrada == "n"):
        print("Não sobrescrevendo...")
        return
    
    for i in range(100):
        try:
            if(mode == 1):  #Professor
                materias = browser.find_element_by_id("formBusca:dataTable:{}:j_id194".format(i)) #id das materias
            elif(mode == 2): #Aluno
                materias = browser.find_element_by_id("formBusca:dataTable:{}:j_id190".format(i))
        except NoSuchElementException: #para quando nao acha mais linha
            break
        
        if(mode == 1):  #Professor
            disciplinas = browser.find_element_by_id("formBusca:dataTable:{}:j_id188".format(i))
            professores = browser.find_element_by_id("formBusca:dataTable:{}:j_id245".format(i))
            horarios = browser.find_element_by_id("formBusca:dataTable:{}:j_id239".format(i))
            turmas = browser.find_element_by_id("formBusca:dataTable:{}:j_id191".format(i))
            horas_aula = browser.find_element_by_id("formBusca:dataTable:{}:j_id202".format(i))
            vagas_ofertadas = browser.find_element_by_id("formBusca:dataTable:{}:j_id208".format(i))
            vagas_ocupadas = browser.find_element_by_id("formBusca:dataTable:{}:j_id214".format(i))
            alunos_especiais = browser.find_element_by_id("formBusca:dataTable:{}:j_id220".format(i)) 
            saldo_vagas = browser.find_element_by_id("formBusca:dataTable:{}:j_id226".format(i))
            pedidos_sem_vagas = browser.find_element_by_id("formBusca:dataTable:{}:j_id233".format(i))
        
        elif(mode == 2):  #Aluno
            disciplinas = browser.find_element_by_id("formBusca:dataTable:{}:j_id184".format(i)) #id das disciplinas
            professores = browser.find_element_by_id("formBusca:dataTable:{}:j_id241".format(i)) #id dos professores
            horarios = browser.find_element_by_id("formBusca:dataTable:{}:j_id235".format(i)) #id dos horarios
            turmas = browser.find_element_by_id("formBusca:dataTable:{}:j_id187".format(i)) #id das turmas
            horas_aula = browser.find_element_by_id("formBusca:dataTable:{}:j_id198".format(i)) #id das horas/aula
            vagas_ofertadas = browser.find_element_by_id("formBusca:dataTable:{}:j_id204".format(i)) #id das vagas ofertadas
            vagas_ocupadas = browser.find_element_by_id("formBusca:dataTable:{}:j_id210".format(i)) #id das vagas ocupadas
            alunos_especiais = browser.find_element_by_id("formBusca:dataTable:{}:j_id216".format(i)) #id dos alunos especiais
            saldo_vagas = browser.find_element_by_id("formBusca:dataTable:{}:j_id222".format(i)) #id do saldo de vagas
            pedidos_sem_vagas = browser.find_element_by_id("formBusca:dataTable:{}:j_id229".format(i)) #id dos pedidos sem vagas
        
        writer.writerow([materias.text,disciplinas.text,professores.text,horarios.text,
	                    turmas.text,horas_aula.text,vagas_ofertadas.text,
	                    vagas_ocupadas.text,alunos_especiais.text,saldo_vagas.text,
	                    pedidos_sem_vagas.text])

"""
Abre e retorna um arquivo com o semestre passado como parametro
"""
def abre_arquivoCagr(semestre):
    if os.path.isdir("CAGR/Output/{}".format(semestre)): #diretório já existe
        entrada = str(input("Arquivo já existe, deseja sobrescrever? [s,n] "))
    else:
        os.mkdir("CAGR/Output/{}".format(semestre))     #se não existe, cria diretório
        
    file = open("CAGR/Output/{}/CAGR_{}.csv".format(semestre,semestre),"w",encoding='utf8') #gera um arquivo csv, onde sera gravado as informacoes
    return file

"""
Fecha o arquivo passado como parametro
"""
def fecha_arquivo(file):
    file.close()

"""
Cria um escritor pro arquivo file
"""
def escreve_arquivoCagr(file,semestre):
    writer = csv.writer(file) #escritor do arquivo
    writer.writerow(["Matérias","Disciplinas","Professores","Horários","Turmas", "Horas/Aula","Vagas Ofertadas", 
                 "Vagas Ocupadas", "Alunos Especiais", "Saldo Vagas", "Pedidos Sem Vaga", semestre]) #gera colunas no arquivo csv
    return writer
