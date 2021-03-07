#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from form.logo import *
from selenium import webdriver
from colorama import Back, Fore, init
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
from time import sleep
from random import randint

#iniciamos los colores
init()

url = " "
contador = 1

#Verificamos si existe el driver
def verificar():
    if os.path.isfile("/usr/bin/geckodriver") == True:
        print("{0}[ {1}+ {0}] {2} El archivo Si Existe {3} EJECUTANDO SCRIPT {4}".format(Fore.BLUE, Fore.GREEN, Fore.CYAN, Fore.GREEN, Fore.RESET ))
        Carga()
    else:
        print("{0} [ {1} X {0} ] {2} El archivo no existe, {3} Comenzando DESCARGA.... {4}".format(Fore.BLUE, Fore.RED, Fore.RED, Fore.WHITE, Fore.RESET))
        Carga()
        os.system("wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz")
        os.system("sudo sh -c 'tar -x geckodriver -zf geckodriver-v0.26.0-linux64.tar.gz -O > /usr/bin/geckodriver'")
        os.system("sudo chmod +x /usr/bin/geckodriver")
        os.system("rm geckodriver-v0.26.0-linux64.tar.gz")
        print("{} [ {} + {} ] {} DRIVER DESCARGADO ...... {}".format(Fore.BLUE, Fore.GREEN, Fore.BLUE, Fore.WHITE, Fore.RESET))

#Da la bienvenida y pide el URL
def Bienvenida():
    MenuInicial()
    verificar()
    global url
    url = input("{0}[{1}@{0}] {2} Coloca el Link de la publicacion: {3}".format(Fore.CYAN, Fore.RED, Fore.WHITE, Fore.RESET))
    print("El URL que has colocado es: " + url)

#guardamos los comentarios
def comentarios():
    try:
        archivo = open("Comentarios.txt", "w")
        global contador
        while True:
            try:
                fichero = open('cuentas.txt', 'r')
                cuenta = len(fichero.readlines())
                fichero.close()
                #print("El fichero cuentas tiene: " + str(cuenta))
                if contador <= cuenta:

                    comentario = input(
                        "{0}[{1}@{0}] {2} Coloca el comentario #{3}: {4}".format(Fore.CYAN, Fore.RED, Fore.WHITE,
                                                                                 contador, Fore.RESET))
                    contador = contador + 1
                    print(comentario)
                    archivo.write(comentario + "\n")



                else:
                    break



            except FileNotFoundError:
                print("{0}[ {1}X {0}] {1} El ARCHIVO cuentas no existe {2} ".format(Fore.CYAN, Fore.RED, Fore.RESET))
                exit()

        archivo.close()
    except FileNotFoundError:
        print("{0}[ {1}X {0}] {1} El ARCHIVO cuentas no existe {2} ".format(Fore.CYAN, Fore.RED, Fore.RESET))
        exit()







def main():
    Bienvenida()
    comentarios()
    LogoTwo()
    print("{0}[{1}@{0}] {2} Comenzando proceso de comentario en la publicacion {3}".format(Fore.CYAN, Fore.RED, Fore.WHITE, Fore.RESET))

    try:
        fichero = open('cuentas.txt', 'r')
        for i, linea in enumerate(fichero):
            linea = linea.split(" ")
            correo = linea[0]
            contra = linea[1]
            #print(correo)
            #print(contra)
            try:
                f = open("Comentarios.txt", "r")
                for num, coment in enumerate(f):
                    if num == i:
                        #print(coment)
                        print(Fore.WHITE + "El numero es", i, Fore.RESET)
                        print("{} [ {} + {} ] {} Correo: ".format(Fore.BLUE, Fore.GREEN, Fore.BLUE, Fore.WHITE, ),"{}".format(Fore.BLUE), correo)
                        print("{} [ {} + {} ] {} Contraseña: **********".format(Fore.BLUE, Fore.GREEN, Fore.BLUE, Fore.WHITE, ))
                        print("{} [ {} + {} ] {} Contraseña: ".format(Fore.BLUE, Fore.GREEN, Fore.BLUE, Fore.WHITE, ),"{}".format(Fore.BLUE), contra)
                        print("{} [ {} + {} ] {} Comentario: ".format(Fore.BLUE, Fore.GREEN, Fore.BLUE, Fore.WHITE, ),"{}".format(Fore.BLUE), coment)
                        driver = webdriver.Firefox(executable_path="geckodriver")
                        driver.get('https://m.facebook.com')
                        alert = Alert(driver)
                        # alert.accept()
                        alert.dismiss()
                        Carga()
                        sleep(randint(6,10))
                        email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@id="m_login_email"]')))
                        email.send_keys(str(correo))
                        passcon = driver.find_element(By.XPATH, '//input[@name="pass"]')
                        passcon.send_keys(str(contra))
                        cli = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/table/tbody/tr/td/div[2]/div[2]/form/ul/li[3]/input')
                        sleep(randint(6, 10))
                        cli.click()
                        Carga()
                        sleep(randint(6, 10))
                        driver.get(url)
                        sleep(randint(6,10))
                        comentando = driver.find_element_by_xpath('//*[@id="composerInput"]')
                        comentando.send_keys(str(coment))
                        sleep(randint(6, 10))
                        cli = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[1]/div[2]/div/div[4]/form[1]/table/tbody/tr/td[2]/div/input")
                        cli.click()
                        sleep(randint(6, 10))
                        like = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[1]/div[2]/div/div[1]/table/tbody/tr/td[1]/a/span')
                        like.click()
                        sleep(randint(6, 10))
                        compartir = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[1]/div[2]/div/div[1]/table/tbody/tr/td[3]/a/span')
                        compartir.click()
                        sleep(randint(6, 10))
                        compartir_2 = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/table/tbody/tr/td/div/form/input[18]')
                        compartir_2.click()
                        sleep(randint(6, 10))
                        Carga()
                        driver.close()
                        sleep(randint(10, 15))
                f.close()


            except FileNotFoundError:
                print("{0}[ {1}X {0}] {1} El ARCHIVO cuentas no existe {2} ".format(Fore.CYAN, Fore.RED, Fore.RESET))
                exit()

        f.close()
        os.system('rm Comentarios.txt')
        print("{0}[{1}@{0}] {2}El url que fue comentado fue: ".format(Fore.CYAN, Fore.RED, Fore.WHITE) + str(url))




    except FileNotFoundError:
        print("{0}[ {1}X {0}] {1} El ARCHIVO cuentas no existe {2} ".format(Fore.CYAN, Fore.RED, Fore.RESET))
        exit()



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        os.system('rm Comentarios.txt')
        exit()
