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
Função que faz o scraping da pagina, das seguintes seções:
    - Página principal
    - Ensino
    - Atendimento
    - Pesquisa
    - Extensão
    - Orientações
    - Administração
    - Observações
Verifica possíveis inconsistências de:
    - FAT (FAT < 1.0 ou FAT > 2.5)
    - HAT (HAT < 8.0)
    - Carga Horária Total (CH diferente de 40 horas)
Gera arquivos CSV's com as informações extraídas da página e arquivos com as inconsistências de FAT, HAT e CH.
PARÂMETROS:
    - Browser
    - Tempo de espera para o navegador carregar
    - Escritores dos respectivos arquivos
>>>>>>> PARA PROFESSORES SUBSTITUTOS <<<<<<<<<<<<<
"""
def pagina_substitutos(browser,tempo,writer,writer2,writer3,writer4,writer5,writer6,writer7,writer8,writerFAT,writerHAT,writerCH,writerATENDIMENTO):
    if(entrada == "n"):
        print("Não sobrescrevendo...")
        return
    
    for i in range(100):    
        time.sleep(tempo)
        
        """======================================= PAGINA PRINCIPAL ================================================="""
        
        try:
            professores = browser.find_element_by_id("allDocForm:docentesSubsTable:{}:j_id309".format(i)) #id das materias
        except NoSuchElementException: #para quando nao acha mais linha
            break
        
        print(professores.text)  
        professor = professores.text #salva em variável para não perder o dado
        
        regimes = browser.find_element_by_id("allDocForm:docentesSubsTable:{}:j_id318".format(i)) #id dos regimes
        print(regimes.text)
        
        HAG = browser.find_element_by_id("allDocForm:docentesSubsTable:{}:j_id325".format(i)) #id horas-aula graduacao
        print(HAG.text)
        
        HAP = browser.find_element_by_id("allDocForm:docentesSubsTable:{}:j_id329".format(i)) #id horas-aula pos-graduacao
        print(HAP.text)
        
        HAT = browser.find_element_by_id("allDocForm:docentesSubsTable:{}:j_id333".format(i)) #id horas-aula total
        print(HAT.text)
        HAT_T = float(HAT.text.replace(',','.'))        
        
        FAT = browser.find_element_by_id("allDocForm:docentesSubsTable:{}:j_id337".format(i)) #id do fator
        print(FAT.text)
        try:
            FAT_T = float(FAT.text.replace(',','.')) #replace, troca a virgula por ponto para converter pra float
        except ValueError:
            FAT_T = 0.0
        
        TOT = browser.find_element_by_id("allDocForm:docentesSubsTable:{}:j_id341".format(i)) #id total
        print(TOT.text)
        
        orientacoes = browser.find_element_by_id("allDocForm:docentesSubsTable:{}:j_id345".format(i)) #id orientacoes
        print(orientacoes.text)
        
        pesquisa = browser.find_element_by_id("allDocForm:docentesSubsTable:{}:j_id349".format(i)) #id pesquisa
        print(pesquisa.text)
        
        extensao = browser.find_element_by_id("allDocForm:docentesSubsTable:{}:j_id353".format(i)) #id extensao
        print(extensao.text)
        
        FOR = browser.find_element_by_id("allDocForm:docentesSubsTable:{}:j_id357".format(i)) #id afast. p/ formacao
        print(FOR.text)
        
        adm = browser.find_element_by_id("allDocForm:docentesSubsTable:{}:j_id361".format(i)) #id administracao
        print(adm.text)
        
        total = browser.find_element_by_id("allDocForm:docentesSubsTable:{}:j_id365".format(i)) #id total
        print(total.text)
        total_T = float(total.text.replace(',','.'))
        
        turmas = browser.find_element_by_id("allDocForm:docentesSubsTable:{}:j_id368".format(i)) #id turmas
        print(turmas.text)
        
        writer.writerow([professores.text,regimes.text,HAG.text,HAP.text,HAT.text,
                         FAT.text,TOT.text,orientacoes.text,pesquisa.text,extensao.text,
                        FOR.text,adm.text,total.text,turmas.text])
        
        time.sleep(tempo)
        browser.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/form[2]/table[2]/tbody/tr[{}]/td[1]/a".format(i+1)).click() #clica nos professores

        
        """=================================== ENSINO ================================================================"""
        
        time.sleep(tempo)
        print(" ")
        print("ENSINO: ")
        
        for i in range(10):
            try:
                codigo = browser.find_element_by_id("discForm:j_id138:{}:j_id140".format(i))
                print(codigo.text)
            except NoSuchElementException:
                break
            
            disciplina = browser.find_element_by_id("discForm:j_id138:{}:j_id143".format(i))
            print(disciplina.text)
            
            turma = browser.find_element_by_id("discForm:j_id138:{}:j_id146".format(i))
            print(turma.text)
            
            periodo = browser.find_element_by_id("discForm:j_id138:{}:j_id149".format(i))
            print(periodo.text)
            
            HA_disciplina = browser.find_element_by_id("discForm:j_id138:{}:j_id152".format(i))
            print(HA_disciplina.text)
            
            HA_docente = browser.find_element_by_id("discForm:j_id138:{}:j_id155".format(i))
            print(HA_docente.text)
            
            CH_PAD = browser.find_element_by_id("discForm:j_id138:{}:j_id158".format(i))
            print(CH_PAD.text)
            
            tipo = browser.find_element_by_id("discForm:j_id138:{}:j_id161".format(i))
            print(tipo.text)
            
            atividade = browser.find_element_by_id("discForm:j_id138:{}:j_id164".format(i))
            print(atividade.text)
                
            #escreve no arquivo de ENSINO
            writer2.writerow([professor,codigo.text,disciplina.text,turma.text,periodo.text,
                              HA_disciplina.text,HA_docente.text,CH_PAD.text,tipo.text, 
                              atividade.text])
            
        """====================================== ATENDIMENTO ========================================================"""
    
        print(" ")
        print("ATENDIMENTO: ")
        for i in range(10):
            try:
                dia = browser.find_element_by_id("horAtendForm:horAtendTable:{}:j_id186".format(i))
                print(dia.text)
            except NoSuchElementException:
                if(i == 0):
                    dia = ""
                    hora_inicio = ""
                    hora_termino = ""
                    local = ""
                    print("!!!!!!! HORARIO DE ATENDIMENTO INVALIDO !!!!!!")
                    writerATENDIMENTO.writerow([professor])
                    writer8.writerow([professor,dia,hora_inicio,hora_termino,
                                  local])
                break

            hora_inicio = browser.find_element_by_id("horAtendForm:horAtendTable:{}:j_id189".format(i))
            print(hora_inicio.text)

            hora_termino = browser.find_element_by_id("horAtendForm:horAtendTable:{}:j_id192".format(i))
            print(hora_termino.text)

            local = browser.find_element_by_id("horAtendForm:horAtendTable:{}:j_id195".format(i))
            print(local.text)
            
            #Escreve no arquivo de ATENDIMENTO
            writer8.writerow([professor,dia.text,hora_inicio.text,hora_termino.text,
                              local.text])


        browser.find_element_by_id("j_id204_lbl").click()            
        
        """==================================== PESQUISA ============================================================="""
        
        time.sleep(tempo)
        print(" ")
        print("PESQUISA: ")
        
        for i in range(10):
            try:
                titulo = browser.find_element_by_id("pesqForm:pesqTable:{}:j_id206".format(i))
                print(titulo.text)
            except NoSuchElementException:
                break
            
            situacao = browser.find_element_by_id("pesqForm:pesqTable:{}:j_id209".format(i))
            print(situacao.text)
                
            funcao = browser.find_element_by_id("pesqForm:pesqTable:{}:j_id212".format(i))
            print(funcao.text)
            
            inicio = browser.find_element_by_id("pesqForm:pesqTable:{}:j_id215".format(i))
            print(inicio.text)
            
            termino = browser.find_element_by_id("pesqForm:pesqTable:{}:j_id218".format(i))
            print(termino.text)
            
            carga_horaria = browser.find_element_by_id("pesqForm:pesqTable:{}:j_id221".format(i))
            print(carga_horaria.text)
            
            carga_horaria_PAD = browser.find_element_by_id("pesqForm:pesqTable:{}:psqchpad".format(i)).get_attribute('value')
            print(carga_horaria_PAD)
            
            #Escreve no arquivo de PESQUISA
            writer3.writerow([professor,titulo.text,situacao.text,funcao.text,inicio.text,
                              termino.text,carga_horaria.text,carga_horaria_PAD])
            
        browser.find_element_by_id("j_id230_lbl").click()
        
        """====================================== EXTENSAO ==========================================================="""
        
        time.sleep(tempo)
        print(" ")
        print("EXTENSAO: ")
        
        for i in range(10):
            try:
                titulo2 = browser.find_element_by_id("extForm:extTable:{}:j_id232".format(i))
                print(titulo2.text)
            except NoSuchElementException:
                break
            
            situacao2 = browser.find_element_by_id("extForm:extTable:{}:j_id235".format(i))
            print(situacao2.text)
            
            funcao2 = browser.find_element_by_id("extForm:extTable:{}:j_id238".format(i))
            print(funcao2.text)
            
            inicio2 = browser.find_element_by_id("extForm:extTable:{}:j_id241".format(i))
            print(inicio2.text)
            
            termino2 = browser.find_element_by_id("extForm:extTable:{}:j_id244".format(i))
            print(termino2.text)
            
            carga_horaria2 = browser.find_element_by_id("extForm:extTable:{}:j_id247".format(i))
            print(carga_horaria2.text)
            
            carga_horaria2_PAD = browser.find_element_by_id("extForm:extTable:{}:chpad".format(i)).get_attribute('value')
            print(carga_horaria2_PAD)
            
            #Escreve no arquivo de EXTENSAO            
            writer4.writerow([professor,titulo2.text,situacao2.text,funcao2.text,inicio2.text,
                              termino2.text,carga_horaria2.text,carga_horaria2_PAD])
            
        browser.find_element_by_id("j_id256_lbl").click()
        
        """======================================== ORIENTACOES ======================================================="""
        
        time.sleep(tempo)
        print(" ")
        print("ORIENTACOES: ")
        
        for i in range(10):
            try:
                tipo3 = browser.find_element_by_id("orientacoesForm:orientacoesTable:{}:j_id268".format(i))
                print(tipo3.text)
            except NoSuchElementException:
                break
            
            carga_horaria3 = browser.find_element_by_id("orientacoesForm:orientacoesTable:{}:j_id271".format(i))
            print(carga_horaria3.text)
            
            quantidade = browser.find_element_by_id("orientacoesForm:orientacoesTable:{}:oriQuantidade".format(i)).get_attribute('value')
            print(quantidade)
            
            total_CH3 = browser.find_element_by_id("orientacoesForm:orientacoesTable:{}:j_id280".format(i))
            print(total_CH3.text)
            
            carga_horaria3_PAD = browser.find_element_by_id("orientacoesForm:orientacoesTable:{}:oriChpad".format(i)).get_attribute('value')
            print(carga_horaria3_PAD)
            
            #Escreve no arquivo de ORIENTACOES
            writer5.writerow([professor,tipo3.text,carga_horaria3.text,quantidade,
                              total_CH3.text,carga_horaria3_PAD])
            
        browser.find_element_by_id("j_id294_lbl").click()
        
        """========================================== ADMINISTRACAO ==================================================="""
        
        time.sleep(tempo)
        print(" ")
        print("ADMINISTRACAO: ")
        
        for i in range(10):
            try:
                tipo4 = browser.find_element_by_id("administracaoForm:administracaoTable:{}:j_id316".format(i))
                print(tipo4.text)
            except NoSuchElementException:
                break
            
            inicio4 = browser.find_element_by_id("administracaoForm:administracaoTable:{}:j_id320".format(i))
            print(inicio4.text)
            
            termino4 = browser.find_element_by_id("administracaoForm:administracaoTable:{}:j_id323".format(i))
            print(termino4.text)
            
            portaria = browser.find_element_by_id("administracaoForm:administracaoTable:{}:j_id326".format(i))
            print(portaria.text)
            
            carga_horaria4 = browser.find_element_by_id("administracaoForm:administracaoTable:{}:j_id329".format(i))
            print(carga_horaria4.text)
            
            carga_horaria4_PAD = browser.find_element_by_id("administracaoForm:administracaoTable:{}:admChpad".format(i)).get_attribute('value')
            print(carga_horaria4_PAD)
            
            #Escreve no arquivo de ADMINISTRACAO
            writer6.writerow([professor,tipo4.text,inicio4.text,termino4.text,portaria.text,
                              carga_horaria4.text,carga_horaria4_PAD])
            
        browser.find_element_by_id("j_id382_lbl").click()
            
        """======================================== OBSERVACOES ======================================================="""
        
        time.sleep(tempo)
        print(" ")
        print("OBSERVAÇÕES: ")
        
        try:
            observacao = browser.find_element_by_id("observacaoForm:observacao")
            print(observacao.text)
        except NoSuchElementException:
            break
        
        #Escreve no arquivo de OBSERVACOES
        writer7.writerow([professor,observacao.text])
        
        """================================ VERIFICACAO DE INCONSISTENCIAS =========================================="""
        
        """HAT < 8"""
        if(HAT_T < 8.0):
            print('!!!!!!!!!!!!!HAT IRREGULAR!!!!!!!!!!!!')
            if(observacao.text == ""):
                writerHAT.writerow([professor,HAT_T,"A justificar"])
            else:
                writerHAT.writerow([professor,HAT_T,observacao.text])
            
        """FAT < 1 ou FAT > 2.5"""
        if(FAT_T < 1.0 or FAT_T > 2.5): 
            print('!!!!!!!!!!!!!FAT IRREGULAR!!!!!!!!!!!!')
            if(observacao.text == ""):
                writerFAT.writerow([professor,FAT_T,"A justificar"])
            else:
                writerFAT.writerow([professor,FAT_T,observacao.text])
        
        """Carga Horária Total diferente de 40 horas"""
        if(total_T != 40.0):
            print('!!!!!!!!!!!!!CARGA HORARIA TOTAL IRREGULAR!!!!!!!!!!!!')
            if(observacao.text == ""):
                writerCH.writerow([professor,total_T,"A justificar"])
            else:
                writerCH.writerow([professor,total_T,observacao.text])
        """-------------------------------------------------------------------------------"""
        
        
        browser.find_element_by_id("voltarForm:quente").click()
        
        time.sleep(tempo)

"""
Função que faz o scraping da pagina, das seguintes seções:
    - Página principal
    - Ensino
    - Atendimento
    - Pesquisa
    - Extensão
    - Orientações
    - Administração
    - Observações
Verifica possíveis inconsistências de:
    - FAT (FAT < 1.0 ou FAT > 2.5)
    - HAT (HAT < 8.0)
    - Carga Horária Total (CH diferente de 40 horas)
Gera arquivos CSV's com as informações extraídas da página e arquivos com as inconsistências de FAT, HAT e CH.
PARÂMETROS:
    - Browser
    - Tempo de espera para o navegador carregar
    - Escritores dos respectivos arquivos
"""
def pagina(browser,tempo,writer,writer2,writer3,writer4,writer5,writer6,writer7,writer8,writerFAT,writerHAT,writerCH,writerATENDIMENTO):
    if(entrada == "n"):
        print("Não sobrescrevendo...")
        return
    
    for i in range(100):    
        time.sleep(tempo)
        
        """======================================= PAGINA PRINCIPAL ================================================="""
        
        try:
            professores = browser.find_element_by_id("allDocForm:docentesQuadroTable:{}:j_id188".format(i)) #id das materias
        except NoSuchElementException: #para quando nao acha mais linha
            #print("Acabou!")
            break
        
        print(professores.text)  
        professor = professores.text #salva em variável para não perder o dado
        
        regimes = browser.find_element_by_id("allDocForm:docentesQuadroTable:{}:j_id197".format(i)) #id dos regimes
        print(regimes.text)
        
        HAG = browser.find_element_by_id("allDocForm:docentesQuadroTable:{}:j_id204".format(i)) #id horas-aula graduacao
        print(HAG.text)
        
        HAP = browser.find_element_by_id("allDocForm:docentesQuadroTable:{}:j_id208".format(i)) #id horas-aula pos-graduacao
        print(HAP.text)
        
        HAT = browser.find_element_by_id("allDocForm:docentesQuadroTable:{}:j_id212".format(i)) #id horas-aula total
        print(HAT.text)
        HAT_T = float(HAT.text.replace(',','.'))        
        
        FAT = browser.find_element_by_id("allDocForm:docentesQuadroTable:{}:j_id216".format(i)) #id do fator
        print(FAT.text)
        FAT_T = float(FAT.text.replace(',','.')) #replace, troca a virgula por ponto para converter pra float
        
        TOT = browser.find_element_by_id("allDocForm:docentesQuadroTable:{}:j_id220".format(i)) #id total
        print(TOT.text)
        
        orientacoes = browser.find_element_by_id("allDocForm:docentesQuadroTable:{}:j_id224".format(i)) #id orientacoes
        print(orientacoes.text)
        
        pesquisa = browser.find_element_by_id("allDocForm:docentesQuadroTable:{}:j_id228".format(i)) #id pesquisa
        print(pesquisa.text)
        
        extensao = browser.find_element_by_id("allDocForm:docentesQuadroTable:{}:j_id232".format(i)) #id extensao
        print(extensao.text)
        
        FOR = browser.find_element_by_id("allDocForm:docentesQuadroTable:{}:j_id236".format(i)) #id afast. p/ formacao
        print(FOR.text)
        
        adm = browser.find_element_by_id("allDocForm:docentesQuadroTable:{}:j_id240".format(i)) #id administracao
        print(adm.text)
        
        total = browser.find_element_by_id("allDocForm:docentesQuadroTable:{}:j_id244".format(i)) #id total
        print(total.text)
        total_T = float(total.text.replace(',','.'))
        
        turmas = browser.find_element_by_id("allDocForm:docentesQuadroTable:{}:j_id247".format(i)) #id turmas
        print(turmas.text)
        
        writer.writerow([professores.text,regimes.text,HAG.text,HAP.text,HAT.text,
                         FAT.text,TOT.text,orientacoes.text,pesquisa.text,extensao.text,
                        FOR.text,adm.text,total.text,turmas.text])
        
        time.sleep(tempo)
        browser.find_element_by_xpath("/html/body/table[2]/tbody/tr[1]/td[1]/form[2]/table[1]/tbody/tr[{}]/td[1]/a".format(i+1)).click() #clica nos professores
        
        """=================================== ENSINO ================================================================"""
        
        time.sleep(tempo)
        print(" ")
        print("ENSINO: ")
        
        for i in range(10):
            try:
                codigo = browser.find_element_by_id("discForm:j_id138:{}:j_id140".format(i))
                print(codigo.text)
            except NoSuchElementException:
                break
            
            disciplina = browser.find_element_by_id("discForm:j_id138:{}:j_id143".format(i))
            print(disciplina.text)
            
            turma = browser.find_element_by_id("discForm:j_id138:{}:j_id146".format(i))
            print(turma.text)
            
            periodo = browser.find_element_by_id("discForm:j_id138:{}:j_id149".format(i))
            print(periodo.text)
            
            HA_disciplina = browser.find_element_by_id("discForm:j_id138:{}:j_id152".format(i))
            print(HA_disciplina.text)
            
            HA_docente = browser.find_element_by_id("discForm:j_id138:{}:j_id155".format(i))
            print(HA_docente.text)
            
            CH_PAD = browser.find_element_by_id("discForm:j_id138:{}:j_id158".format(i))
            print(CH_PAD.text)
            
            tipo = browser.find_element_by_id("discForm:j_id138:{}:j_id161".format(i))
            print(tipo.text)
            
            atividade = browser.find_element_by_id("discForm:j_id138:{}:j_id164".format(i))
            print(atividade.text)
                
            #escreve no arquivo de ENSINO
            writer2.writerow([professor,codigo.text,disciplina.text,turma.text,periodo.text,
                              HA_disciplina.text,HA_docente.text,CH_PAD.text,tipo.text, 
                              atividade.text])
            
        """====================================== ATENDIMENTO ========================================================"""
    
        print(" ")
        print("ATENDIMENTO: ")
        for i in range(10):
            try:
                dia = browser.find_element_by_id("horAtendForm:horAtendTable:{}:j_id186".format(i))
                print(dia.text)
            except NoSuchElementException:
                if(i == 0):
                    dia = ""
                    hora_inicio = ""
                    hora_termino = ""
                    local = ""
                    print("!!!!!!! HORARIO DE ATENDIMENTO INVALIDO !!!!!!")
                    writerATENDIMENTO.writerow([professor])
                    writer8.writerow([professor,dia,hora_inicio,hora_termino,
                                      local])
                break
            
            hora_inicio = browser.find_element_by_id("horAtendForm:horAtendTable:{}:j_id189".format(i))
            print(hora_inicio.text)
            
            hora_termino = browser.find_element_by_id("horAtendForm:horAtendTable:{}:j_id192".format(i))
            print(hora_termino.text)
            
            local = browser.find_element_by_id("horAtendForm:horAtendTable:{}:j_id195".format(i))
            #local = browser.find_element_by_id("horAtendForm:horAtendTable:{}:j_id202".format(i))
            print(local.text)

            #Escreve no arquivo de ATENDIMENTO
            writer8.writerow([professor,dia.text,hora_inicio.text,hora_termino.text,
                              local.text])


        browser.find_element_by_id("j_id204_lbl").click()            
        
        """==================================== PESQUISA ============================================================="""
        
        time.sleep(tempo)
        print(" ")
        print("PESQUISA: ")
        
        for i in range(10):
            try:
                titulo = browser.find_element_by_id("pesqForm:pesqTable:{}:j_id206".format(i))
                print(titulo.text)
            except NoSuchElementException:
                break
            
            situacao = browser.find_element_by_id("pesqForm:pesqTable:{}:j_id209".format(i))
            print(situacao.text)
                
            funcao = browser.find_element_by_id("pesqForm:pesqTable:{}:j_id212".format(i))
            print(funcao.text)
            
            inicio = browser.find_element_by_id("pesqForm:pesqTable:{}:j_id215".format(i))
            print(inicio.text)
            
            termino = browser.find_element_by_id("pesqForm:pesqTable:{}:j_id218".format(i))
            print(termino.text)
            
            carga_horaria = browser.find_element_by_id("pesqForm:pesqTable:{}:j_id221".format(i))
            print(carga_horaria.text)
            
            carga_horaria_PAD = browser.find_element_by_id("pesqForm:pesqTable:{}:psqchpad".format(i)).get_attribute('value')
            print(carga_horaria_PAD)
            
            #Escreve no arquivo de PESQUISA
            writer3.writerow([professor,titulo.text,situacao.text,funcao.text,inicio.text,
                              termino.text,carga_horaria.text,carga_horaria_PAD])
            
        browser.find_element_by_id("j_id230_lbl").click()
        
        """====================================== EXTENSAO ==========================================================="""
        
        time.sleep(tempo)
        print(" ")
        print("EXTENSAO: ")
        
        for i in range(10):
            try:
                titulo2 = browser.find_element_by_id("extForm:extTable:{}:j_id232".format(i))
                print(titulo2.text)
            except NoSuchElementException:
                break
            
            situacao2 = browser.find_element_by_id("extForm:extTable:{}:j_id235".format(i))
            print(situacao2.text)
            
            funcao2 = browser.find_element_by_id("extForm:extTable:{}:j_id238".format(i))
            print(funcao2.text)
            
            inicio2 = browser.find_element_by_id("extForm:extTable:{}:j_id241".format(i))
            print(inicio2.text)
            
            termino2 = browser.find_element_by_id("extForm:extTable:{}:j_id244".format(i))
            print(termino2.text)
            
            carga_horaria2 = browser.find_element_by_id("extForm:extTable:{}:j_id247".format(i))
            print(carga_horaria2.text)
            
            carga_horaria2_PAD = browser.find_element_by_id("extForm:extTable:{}:chpad".format(i)).get_attribute('value')
            print(carga_horaria2_PAD)
            
            #Escreve no arquivo de EXTENSAO            
            writer4.writerow([professor,titulo2.text,situacao2.text,funcao2.text,inicio2.text,
                              termino2.text,carga_horaria2.text,carga_horaria2_PAD])
            
        browser.find_element_by_id("j_id256_lbl").click()
        
        """======================================== ORIENTACOES ======================================================="""
        
        time.sleep(tempo)
        print(" ")
        print("ORIENTACOES: ")
        
        for i in range(10):
            try:
                tipo3 = browser.find_element_by_id("orientacoesForm:orientacoesTable:{}:j_id268".format(i))
                print(tipo3.text)
            except NoSuchElementException:
                break
            
            carga_horaria3 = browser.find_element_by_id("orientacoesForm:orientacoesTable:{}:j_id271".format(i))
            print(carga_horaria3.text)
            
            quantidade = browser.find_element_by_id("orientacoesForm:orientacoesTable:{}:oriQuantidade".format(i)).get_attribute('value')
            print(quantidade)
            
            total_CH3 = browser.find_element_by_id("orientacoesForm:orientacoesTable:{}:j_id280".format(i))
            print(total_CH3.text)
            
            carga_horaria3_PAD = browser.find_element_by_id("orientacoesForm:orientacoesTable:{}:oriChpad".format(i)).get_attribute('value')
            print(carga_horaria3_PAD)
            
            #Escreve no arquivo de ORIENTACOES
            writer5.writerow([professor,tipo3.text,carga_horaria3.text,quantidade,
                              total_CH3.text,carga_horaria3_PAD])
            
        browser.find_element_by_id("j_id294_lbl").click()
        
        """========================================== ADMINISTRACAO ==================================================="""
        
        time.sleep(tempo)
        print(" ")
        print("ADMINISTRACAO: ")
        
        for i in range(10):
            try:
                tipo4 = browser.find_element_by_id("administracaoForm:administracaoTable:{}:j_id316".format(i))
                print(tipo4.text)
            except NoSuchElementException:
                break
            
            inicio4 = browser.find_element_by_id("administracaoForm:administracaoTable:{}:j_id320".format(i))
            print(inicio4.text)
            
            termino4 = browser.find_element_by_id("administracaoForm:administracaoTable:{}:j_id323".format(i))
            print(termino4.text)
            
            portaria = browser.find_element_by_id("administracaoForm:administracaoTable:{}:j_id326".format(i))
            print(portaria.text)
            
            carga_horaria4 = browser.find_element_by_id("administracaoForm:administracaoTable:{}:j_id329".format(i))
            print(carga_horaria4.text)
            
            carga_horaria4_PAD = browser.find_element_by_id("administracaoForm:administracaoTable:{}:admChpad".format(i)).get_attribute('value')
            print(carga_horaria4_PAD)
            
            #Escreve no arquivo de ADMINISTRACAO
            writer6.writerow([professor,tipo4.text,inicio4.text,termino4.text,portaria.text,
                              carga_horaria4.text,carga_horaria4_PAD])
            
        browser.find_element_by_id("j_id382_lbl").click()
            
        """======================================== OBSERVACOES ======================================================="""
        
        time.sleep(tempo)
        print(" ")
        print("OBSERVAÇÕES: ")
        
        try:
            observacao = browser.find_element_by_id("observacaoForm:observacao")
            print(observacao.text)
        except NoSuchElementException:
            break
        
        #Escreve no arquivo de OBSERVACOES
        writer7.writerow([professor,observacao.text])
        
        """================================ VERIFICACAO DE INCONSISTENCIAS =========================================="""
        
        """HAT < 8"""
        if(HAT_T < 8.0):
            print('!!!!!!!!!!!!!HAT IRREGULAR!!!!!!!!!!!!')
            if(observacao.text == ""):
                writerHAT.writerow([professor,HAT_T,"A justificar"])
            else:
                writerHAT.writerow([professor,HAT_T,observacao.text])
            
        """FAT < 1 ou FAT > 2.5"""
        if(FAT_T < 1.0 or FAT_T > 2.5): 
            print('!!!!!!!!!!!!!FAT IRREGULAR!!!!!!!!!!!!')
            if(observacao.text == ""):
                writerFAT.writerow([professor,FAT_T,"A justificar"])
            else:
                writerFAT.writerow([professor,FAT_T,observacao.text])
        
        """Carga Horária Total diferente de 40 horas"""
        if(total_T != 40.0):
            print('!!!!!!!!!!!!!CARGA HORARIA TOTAL IRREGULAR!!!!!!!!!!!!')
            if(observacao.text == ""):
                writerCH.writerow([professor,total_T,"A justificar"])
            else:
                writerCH.writerow([professor,total_T,observacao.text])
        """-------------------------------------------------------------------------------"""
        
        
        browser.find_element_by_id("voltarForm:quente").click()
        
        time.sleep(tempo)        
        
"""
Abre e retorna um arquivo com o semestre passado como parametro
"""
def abre_arquivo(semestre):
    if os.path.isdir("PAAD/Output/{}".format(semestre)): #diretório já existe
        entrada = str(input("Arquivo já existe, deseja sobrescrever? [s,n] "))
    else:
        os.mkdir("PAAD/Output/{}".format(semestre))     #se não existe, cria diretório
        
    file = open("PAAD/Output/{}/PAAD_{}.csv".format(semestre,semestre),"w",encoding='utf8') #gera um arquivo csv, onde sera gravado as informacoes
    return file
    
def abre_arquivo_ensino(semestre):
    file = open("PAAD/Output/{}/PAAD_{}_ensino.csv".format(semestre,semestre),"w",encoding='utf8') #gera um arquivo csv, onde sera gravado as informacoes
    return file
    
def abre_arquivo_pesquisa(semestre):
    file = open("PAAD/Output/{}/PAAD_{}_pesquisa.csv".format(semestre,semestre),"w",encoding='utf8')
    return file
    
def abre_arquivo_extensao(semestre):
    file = open("PAAD/Output/{}/PAAD_{}_extensao.csv".format(semestre,semestre),"w",encoding='utf8') #gera um arquivo csv, onde sera gravado as informacoes
    return file
    
def abre_arquivo_orientacoes(semestre):
    file = open("PAAD/Output/{}/PAAD_{}_orientacoes.csv".format(semestre,semestre),"w",encoding='utf8') #gera um arquivo csv, onde sera gravado as informacoes
    return file
    
def abre_arquivo_administracao(semestre):
    file = open("PAAD/Output/{}/PAAD_{}_administracao.csv".format(semestre,semestre),"w",encoding='utf8') #gera um arquivo csv, onde sera gravado as informacoes
    return file
    
def abre_arquivo_observacao(semestre):
    file = open("PAAD/Output/{}/PAAD_{}_observacao.csv".format(semestre,semestre),"w",encoding='utf8') #gera um arquivo csv, onde sera gravado as informacoes
    return file

def abre_arquivo_atendimento(semestre):
    file = open("PAAD/Output/{}/PAAD_{}_atendimento.csv".format(semestre,semestre),"w",encoding='utf8') #gera um arquivo csv, onde sera gravado as informacoes
    return file
    
def abre_arquivo_inconsistenciasFAT(semestre):
    if os.path.isdir("PAAD/Inconsistências/{}".format(semestre)): #diretório já existe
        pass
    else:
        os.mkdir("PAAD/Inconsistências/{}".format(semestre))     #se não existe, cria diretório
        
    file = open("PAAD/Inconsistências/{}/PAAD_{}_FAT.csv".format(semestre,semestre),"w",encoding='utf8')
    return file

def abre_arquivo_inconsistenciasHAT(semestre):
    file = open("PAAD/Inconsistências/{}/PAAD_{}_HAT.csv".format(semestre,semestre),"w",encoding='utf8')
    return file

def abre_arquivo_inconsistenciasCH(semestre):
    file = open("PAAD/Inconsistências/{}/PAAD_{}_CARGA_HORARIA.csv".format(semestre,semestre),"w",encoding='utf8')
    return file

def abre_arquivo_inconsistenciasATENDIMENTO(semestre):
    file = open("PAAD/Inconsistências/{}/PAAD_{}_ATENDIMENTO.csv".format(semestre,semestre),"w",encoding='utf8')
    return file

"""
Fecha o arquivo passado como parametro
"""
def fecha_arquivo(file):
    file.close()

"""
Cria um escritor pro arquivo file
"""
def escreve_arquivo(file,semestre):
    writer = csv.writer(file,delimiter='|') #escritor do arquivo
    writer.writerow(["PROFESSOR","REGIME","HAG","HAP","HAT", "FAT","TOT", 
                 "ORIENTAÇÕES", "PESQUISA", "EXTENSÃO", "FOR", "ADM", "TOTAL", "TURMAS", semestre]) #gera colunas no arquivo csv
    return writer

def escreve_arquivo_ensino(file,semestre):
    writer = csv.writer(file,delimiter='|') #escritor do arquivo
    writer.writerow(["PROFESSOR","CODIGO","DISCIPLINA","TURMA","PERIODO","HA DISCiPLINA", "HA DOCENTE","CH PAD", 
                 "TIPO", "ATIVIDADE", semestre]) #gera colunas no arquivo csv
    return writer        

def escreve_arquivo_pesquisa_e_extensao(file,semestre):
    writer = csv.writer(file,delimiter='|') #escritor do arquivo
    writer.writerow(["PROFESSOR","TITULO","SITUACAO","FUNCAO","INICIO","TERMINO", "CARGA HORARIA", "CARGA HORARIA PAD", semestre]) #gera colunas no arquivo csv
    return writer 
    
def escreve_arquivo_orientacoes(file,semestre):
    writer = csv.writer(file,delimiter='|') #escritor do arquivo
    writer.writerow(["PROFESSOR","TIPO","CARGA HORARIA","QUANTIDADE","TOTAL CH","CARGA HORARIA PAD", semestre]) #gera colunas no arquivo csv
    return writer 
    
def escreve_arquivo_administracao(file,semestre):
    writer = csv.writer(file,delimiter='|') #escritor do arquivo
    writer.writerow(["PROFESSOR","TIPO","DATA INICIO","DATA TERMINO", "Nº PORTARIA", "CARGA HORARIA", "CARGA HORARIA PAD", semestre]) #gera colunas no arquivo csv
    return writer 
    
def escreve_arquivo_observacao(file,semestre):
    writer = csv.writer(file,delimiter='|') #escritor do arquivo
    writer.writerow(["PROFESSOR","OBSERVAÇÕES",semestre]) #gera colunas no arquivo csv
    return writer

def escreve_arquivo_atendimento(file,semestre):
    writer = csv.writer(file,delimiter='|') #escritor do arquivo
    writer.writerow(["PROFESSOR","DIA DA SEMANA","HORA INICIO","HORA TERMINO","LOCAL",semestre]) #gera colunas no arquivo csv
    return writer
    
def escreve_arquivo_inconsistenciasFAT(file,semestre):
    writer = csv.writer(file,delimiter='|')
    writer.writerow(["DocentesFAT", "FAT", "OBSERVACAO", semestre])
    return writer

def escreve_arquivo_inconsistenciasHAT(file,semestre):
    writer = csv.writer(file,delimiter='|')
    writer.writerow(["DocentesHAT", "HAT", "OBSERVACAO", semestre])
    return writer

def escreve_arquivo_inconsistenciasCH(file,semestre):
    writer = csv.writer(file,delimiter='|')
    writer.writerow(["DocentesCargaHoraria", "CH", "OBSERVACAO", semestre])
    return writer

def escreve_arquivo_inconsistenciasATENDIMENTO(file,semestre):
    writer = csv.writer(file,delimiter='|')
    writer.writerow(["DocentesAtendimento", semestre])
    return writer