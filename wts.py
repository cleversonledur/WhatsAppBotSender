# -*- coding: utf-8 -*-
# filename          : wts.py
# description       : Send bulk whatsapp messages to a list
# author            : Cleverson Lopes Ledur
# email             : cleversonledur@gmail.com
# date              : 20200505
# version           : 0.1
# usage             : python wts.py
# notes             : Change phone numbers and message before sending. 
# license           : MIT
# py version        : 2.7.13
#==============================================================================

from selenium import webdriver

import time

class WhatsappBot:
    def __init__(self):

        #REPLACE MESSAGE
        self.mensagem = "Hi, how are you?"
        
        #REPLACE PHONE NUMBERS HERE
        self.contatos = ["555100000000"]
        
        
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path = './chromedriver')

    def SendMessages(self):

        linkWhatsAppCheck = 'https://web.whatsapp.com/'
        self.driver.get(linkWhatsAppCheck)
        time.sleep(20)
            
        for contato in self.contatos:
            try:
                link = 'https://web.whatsapp.com/send?phone='+ contato + '&text=' + self.mensagem
                self.driver.get(link)
                time.sleep(15)
                chat_box = self.driver.find_element_by_class_name('_1U1xa')
                chat_box.click()
                time.sleep(5)
            except:
                print("Something went wrong: " + contato)
            

bot = WhatsappBot();
bot.SendMessages();