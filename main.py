#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import os
from CAGR.Scripts.arquivo import inconsistencias
from CAGR.Scripts.WebScraping import *
from PAAD.Scripts.WebScrapingPaad import *

class Application: 
    counter = 0
    def __init__(self, master=None):
        """========================== INTERFACE CAGR ============================="""
        self.fonte =("Verdana", "8")
        
        """titulo"""
        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.grid(row=0,column=0)
        
        """escolhe Professor ou Aluno"""
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.grid(row=1,column=0)
        
        """usuario"""
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 10    
        self.container2.grid(row=2,column=0)
        
        """senha"""
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 10
        self.container3.grid(row=3,column=0)
        
        """informar o semestre"""
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.grid(row=4,column=0)
        
        """informar o campus"""
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.grid(row=5,column=0)
        
        """botao fazer scrap"""
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 10
        self.container6.grid(row=6,column=0)
        
        self.titulo1 = Label(self.container1, text="CAGR")
        self.titulo1["font"] = ("Calibri", "12", "bold")
        self.titulo1.pack()
        
        self.lblmodo = Label(self.container7, text="Modo",
                                 font=self.fonte, width=10)
        self.lblmodo.pack(side=LEFT)
        
        self.combo2 = ttk.Combobox(self.container7)
        self.combo2['values'] = ("Professor","Aluno")
        self.combo2["width"] = 20
        self.combo2.current(0)
        self.combo2.pack()
        
        self.lblusuario= Label(self.container2, text="Matrícula:", 
        font=self.fonte, width=10)
        self.lblusuario.pack(side=LEFT)
     
        self.txtusuario = Entry(self.container2)
        self.txtusuario["width"] = 25
        self.txtusuario["font"] = self.fonte
        self.txtusuario.pack(side=LEFT)
     
        self.lblsenha= Label(self.container3, text="Senha:", 
        font=self.fonte, width=10)
        self.lblsenha.pack(side=LEFT)
     
        self.txtsenha = Entry(self.container3)
        self.txtsenha["width"] = 25
        self.txtsenha["show"] = "*"
        self.txtsenha["font"] = self.fonte
        self.txtsenha.pack(side=LEFT)
        
        self.lblsemestre1 = Label(self.container4, text="Semestre:",
                                 font=self.fonte, width=10)
        self.lblsemestre1.pack(side=LEFT)
        
        self.txtsemestre1 = Entry(self.container4)
        self.txtsemestre1["width"] = 25
        self.txtsemestre1["font"] = self.fonte
        self.txtsemestre1.pack(side=LEFT)
        
        self.lblcampus = Label(self.container5, text="Campus:",
                                 font=self.fonte, width=10)
        self.lblcampus.pack(side=LEFT)
        
        self.combo = ttk.Combobox(self.container5)
        self.combo['values'] = ("EaD","FLO","JOI","CBS","ARA","BLN")
        self.combo["width"] = 20
        self.combo.current(2)
        self.combo.pack()
        
        self.bntInsert1 = Button(self.container6, text="Fazer Scrap",
                                font=self.fonte, width=12)
        self.bntInsert1["command"] = self.ScrapingCagr
        self.bntInsert1.pack(side=LEFT)
        
        self.separator = ttk.Separator(root,orient=VERTICAL)
        self.separator.grid(row=0,rowspan=13,column=1,sticky="wns")
        
        """==================================== INTERFACE PAAD =================================="""
        
        """titulo"""
        self.container8 = Frame(master)
        self.container8["pady"] = 10
        self.container8.grid(row=0,column=2)
        
        """informar o semestre"""
        self.container9 = Frame(master)
        self.container9["padx"] = 20
        self.container9["pady"] = 5
        self.container9.grid(row=1,column=2)
        
        """botao fazer scrap"""
        self.container10 = Frame(master)
        self.container10["padx"] = 10
        self.container10["pady"] = 5
        self.container10.grid(row=2,column=2)
        
        self.titulo2 = Label(self.container8, text="PAAD")
        self.titulo2["font"] = ("Calibri", "12", "bold")
        self.titulo2.pack()
        
        self.lblsemestre2 = Label(self.container9, text="Semestre:",
                                 font=self.fonte, width=10)
        self.lblsemestre2.pack(side=LEFT)
        
        self.txtsemestre2 = Entry(self.container9)
        self.txtsemestre2["width"] = 25
        self.txtsemestre2["font"] = self.fonte
        self.txtsemestre2.pack(side=LEFT)
        
        self.bntInsert2 = Button(self.container10, text="Fazer Scrap",
                                font=self.fonte, width=12)
        self.bntInsert2["command"] = self.ScrapingPaad
        self.bntInsert2.pack(side=LEFT)
        
    def ScrapingCagr(self):
        print("Web Scraping CAGR")
        
        matricula = self.txtusuario.get()
        senha = self.txtsenha.get()
        semestre = self.txtsemestre1.get()
        
        if(self.combo.get() == "EaD"):
            value = 0
        elif(self.combo.get() == "FLO"):
            value = 1
        elif(self.combo.get() == "JOI"):
            value = 2
        elif(self.combo.get() == "CBS"):
            value = 3
        elif(self.combo.get() == "ARA"):
            value = 4
        elif(self.combo.get() == "BLN"):
            value = 5
        
        options = Options() #nao abre fisicamente o navegador
        options.add_argument("--headless")
        
        tempo = 1
        
        print('Abrindo o Firefox...')
        
        print('Semestre: {}'.format(semestre))

        browser = webdriver.Firefox(executable_path='CAGR/geckodriver-v0.26.0-linux64/geckodriver') #abre o Firefox
        
        if(self.combo2.get() == "Professor"):  #Professor
            modo = 1
            browser.get('https://cagr.sistemas.ufsc.br/modules/professor/cadastroTurmas/') #abre o site do CAGR Cadastro de Turmas
        elif(self.combo2.get() == "Aluno"):  #Aluno
            modo = 2
            browser.get('https://cagr.sistemas.ufsc.br/modules/aluno/cadastroTurmas/') #abre o site do CAGR Cadastro de Turmas
        
        print('Fazendo login...')
        
        inputElement = browser.find_element_by_name("username").send_keys(matricula) #digita a matricula
        inputElement2 = browser.find_element_by_name("password").send_keys(senha) #digita a senha
        login = browser.find_element_by_name("submit").click() #faz login
        
        WebDriverWait(browser,10)
        
        select = browser.find_element_by_id("formBusca:selectCampus") #procura os campi
        time.sleep(tempo)
        select.find_element_by_xpath("//option[@value='{}']".format(value)).click() #clica em UFSC/JOI
        time.sleep(tempo)
        
        select = browser.find_element_by_id("formBusca:selectSemestre") #procura os semestres
        time.sleep(tempo)
        select.find_element_by_xpath("//option[@value='{}']".format(semestre)).click() #clica no semestre escolhido
        time.sleep(tempo)
        browser.find_element_by_xpath("//input[@value='Buscar']").click() #clica em Buscar
        time.sleep(tempo)
        
        file = abre_arquivoCagr(semestre)
        writer = escreve_arquivoCagr(file,semestre)
        page = 1
        
        next_page_atual = "."
        next_page_anterior = ""
        
        #varre ate a ultima pagina
        while(next_page_anterior != next_page_atual):
            print('Fazendo scraping da pagina {}...'.format(page))
            time.sleep(tempo)
            paginaCagr(browser,writer,semestre,modo)
            page += 1
            next_page_anterior = next_page_atual
            next_page_atual = browser.find_element_by_xpath("//*[@id='formBusca:dataScroller1_table']/tbody/tr/td[15]") #clica pra proxima pagina enquanto tiver o botao Next
            next_page_atual.click()
            time.sleep(tempo)
            if(next_page_atual == browser.find_element_by_xpath("/html/body/div[4]/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td[2]/span/table/tbody/tr[2]/td/table/tbody/tr/td/span/form/div[2]/span/div[1]/table/tbody/tr/td[15]")): #botao next da pagina atual igual ao da proxima(loop)
                break
                
        time.sleep(tempo)
        
        fecha_arquivo(file) #fecha o arquivo csv
        
        time.sleep(tempo)
        
        print('Fechando o Firefox...')
        
        browser.quit() #fecha o navegador
        
    def ScrapingPaad(self):
        print("Web Scraping PAAD")

        semestre = self.txtsemestre2.get()
        
        options = Options() #nao abre fisicamente o navegador
        options.add_argument("--headless")
        
        tempo = 1
        
        print('Abrindo o Firefox...')
        
        print(semestre)
        
        browser = webdriver.Firefox(executable_path='CAGR/geckodriver-v0.26.0-linux64/geckodriver') #abre o Firefox
        browser.get('https://paad.sistemas.ufsc.br/') #abre o site do CAGR Cadastro de Turmas
        
        WebDriverWait(browser,10)
        
        select = browser.find_element_by_id("j_id11") #CONSULTA
        select.find_element_by_xpath("/html/body/table[1]/tbody/tr[2]/td/form/table/tbody/tr/td[2]/a[2]").click()
        
        time.sleep(tempo)
        
        select = browser.find_element_by_xpath("//*[contains(text(), 'DEPARTAMENTO DE ENGENHARIAS DA MOBILIDADE / DEM/CTJOI - DEM/CTJOI')]") #CTJ
        select.click()
        
        time.sleep(tempo)
        
        """=============================== ABERTURA DOS ARQUIVOS E WRITERS ==========================================="""
        
        file = abre_arquivo(semestre)
        writer = escreve_arquivo(file,semestre)
        
        file2 = abre_arquivo_ensino(semestre)
        writer2 = escreve_arquivo_ensino(file2,semestre)
        
        file3 = abre_arquivo_pesquisa(semestre)
        writer3 = escreve_arquivo_pesquisa_e_extensao(file3,semestre)
        
        file4 = abre_arquivo_extensao(semestre)
        writer4 = escreve_arquivo_pesquisa_e_extensao(file4,semestre)
        
        file5 = abre_arquivo_orientacoes(semestre)
        writer5 = escreve_arquivo_orientacoes(file5,semestre)
        
        file6 = abre_arquivo_administracao(semestre)
        writer6 = escreve_arquivo_administracao(file6,semestre)
        
        file7 = abre_arquivo_observacao(semestre)
        writer7 = escreve_arquivo_observacao(file7,semestre)
        
        file8 = abre_arquivo_atendimento(semestre)
        writer8 = escreve_arquivo_atendimento(file8,semestre)
        
        fileFAT = abre_arquivo_inconsistenciasFAT(semestre)
        writerFAT = escreve_arquivo_inconsistenciasFAT(fileFAT,semestre)
        
        fileHAT = abre_arquivo_inconsistenciasHAT(semestre)
        writerHAT = escreve_arquivo_inconsistenciasHAT(fileHAT,semestre)
        
        fileCH = abre_arquivo_inconsistenciasCH(semestre)
        writerCH = escreve_arquivo_inconsistenciasCH(fileCH,semestre)
        
        fileATENDIMENTO = abre_arquivo_inconsistenciasATENDIMENTO(semestre)
        writerATENDIMENTO = escreve_arquivo_inconsistenciasATENDIMENTO(fileATENDIMENTO,semestre)
        
        """============ SELECIONA O SEMESTRE E CHAMA A FUNCAO QUE REALIZA O SCRAPING ================================="""
        
        if(semestre == '20161'):
            value = 16
        else:
            aux = int(semestre) - 20161  #Ex.: 21
            digito1 = aux/10             #2
            digito2 = aux % 10            #1
            value = int(16 + (2*digito1 + digito2))  #16 + [2*ano (2 semestres/ano) + semestre]

        browser.find_element_by_xpath("//option[@value='{}']".format(value)).click()
        time.sleep(tempo)
        
        pagina(browser,tempo,writer,writer2,writer3,writer4,writer5,writer6,writer7,writer8,writerFAT,writerHAT,writerCH,writerATENDIMENTO)
        pagina_substitutos(browser,tempo,writer,writer2,writer3,writer4,writer5,writer6,writer7,writer8,writerFAT,writerHAT,writerCH,writerATENDIMENTO)
        
        time.sleep(tempo)
        
        """=============================== FECHANDO OS ARQUIVOS ==========================================="""
        
        fecha_arquivo(file)
        fecha_arquivo(file2)
        fecha_arquivo(file3)
        fecha_arquivo(file4)
        fecha_arquivo(file5)
        fecha_arquivo(file6)
        fecha_arquivo(file7)
        fecha_arquivo(file8)
        fecha_arquivo(fileFAT)
        fecha_arquivo(fileHAT)
        fecha_arquivo(fileCH)
        fecha_arquivo(fileATENDIMENTO)
        
        print("Fechando o Firefox...")
        
        browser.quit()
        
root = Tk()
root.title("Web Scraping")
root.geometry('600x300')
root.resizable(0,0)

menubar = Menu(root)
filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="Inconsistências CAGR",command=inconsistencias)
filemenu.add_separator()
filemenu.add_command(label="Sair",command=root.quit)
menubar.add_cascade(label="Arquivo",menu=filemenu)

root.config(menu=menubar)
Application(root)
root.mainloop()