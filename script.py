#importar bibliotecas
from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager() .install())

#aqui definimos los usuarios a los que se les enviara el mensaje, y el mensaje.

user = ['user1', 'user2', 'user3']
message_ = ("esto es un bot y lo estosy testeando")

#aqui crearemos la clase. Estara todo el bot alojado aqui, por lo tanto solo deberemos hacer llamamiento a la clase y esta tendra toda la funcion

class bot:

    def __init__(self, username, password, user, message):
        
        #iniciamos el usuario
        self.username = username

        #iniciamos el password
        self.password =  password

        #inicializar usuario
        self.user = user

        #iniciar mensaje
        self.message = message

        #colocando la url
        self.base_url = 'https://www.instagram.com'

        #haciendo llamado a los drivers de chrome
        self.bot = driver

        #iniciamos la funcion loguin que creamos
        self.loguin()

    def loguin(self):
    
        self.bot.get(self.base_url)

        #introduccion del user para loggear en instagram
        enter_username = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By.NAME, 'username'))
            )

        enter_username.send_keys(self.username)

        #introduccion del password para loggear en instagram
        enter_password = WebDriverWait(self.bot, 20).until(
            expected_conditions.presence_of_element_located((By. NAME, 'password'))
        )

        enter_password.send_keys(self.password)

        #devolucion de contraseña al iniciar sesion en la cuenta
        enter_password.send_keys(Keys.RETURN)
        time.sleep(5)

        #primer pop-up de instagram
        self.bot.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div/div/div/button'
        ).click()
        time.sleep(3)

        #segundo pop-up de instagram
        self.bot.find_element_by_xpath(
            '/html/body/div[4]/div/div/div/div[3]/button[2]'
        ).click()

        time.sleep(5)

        #entrar en "enviar mensaje"
        self.bot.find_element_by_xpath(
            '//a[@class="xWeGp]/*[name()="svg"][@aria-label="direct"]'
        ).click()

        time.sleep(3)

        #aqui haremos click en el boton de escribir
        self.bot.find_element_by_xpath(
            '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/button'
        ).click()

        time.sleep(2)

        '''
        Ahora pasamos a tomar el nombre de usuario de la lista anteriormente 
        presentada.
        '''
        for i in user:

            #enter user
            self.bot.find_element_by_xpath(
                '/html/body/div[4]/div/div/div[2]/div[1]/div/div[2]/input'
            ).send_keys
            time.sleep(2)

            #click en el user
            self.bot.find_element_by_xpath(
                '/html/body/div[4]/div/div/div[2]/div'
            ).click()
            time.sleep(2)

            #proximo boton
            self.bot.find_element_by_xpath(
                '/html/body/div[4]/div/div/div[1]/div/div[2]/div/button'
            ).click()
            time.sleep(2)

            #clickeando area de mensaje
            send = self.bot.find_element_by_xpath(
                '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea'
            )

            #escribir mensaje
            send.send_keys(self.message)
            time.sleep(1)

            #enviar mensaje
            send.send_keys(Keys.RETURN)
            time.sleep(2)

            #clickeamos en el icono del lapiz
            self.bot.find_element_by_xpath(
                '/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button'
            ).click()
            time.sleep(2)

        '''
        Ahora pasaremos el usuario y la contraseña de la cuenta que utilizaremos
        '''

def init():
    #aqui va la cuenta
    bot('user_propio', 'pass_propio', user, message_)
    #cuando el programa termine dira "salida"
    input("SALIDA")

#llamando a la funcion
init()