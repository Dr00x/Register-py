from os import close, path, system
import os
from random import randint as rd
import webbrowser

while True:
    def cadastro():
        name = str(input('Insira seu nome\n>:'))
        yold = str(input('Insira sua idade\n>:'))
        country = str(input('Insira seu pais\n>:'))
        
        inf = ['nome: '+str(name),'anos: '+str(yold),'pais: '+str(country)]

        if os.path.exists(f'{os.path.dirname(os.path.realpath(__file__))}/cadastro.txt'):
            with open(f'{os.path.dirname(os.path.realpath(__file__))}/cadastro{rd(0,999)}.txt','w') as rfile:
                for i in inf:
                    rfile.writelines(i + '\n')
                rfile.close()
        else:
            with open(f'{os.path.dirname(os.path.realpath(__file__))}/cadastro.txt','w') as rfile:
                for i in inf:
                    rfile.writelines(i + '\n')
                rfile.close()

    def vercadastro():
        webbrowser.open('file:///' + os.getcwd() +'/register')

    def menu(choices):
        range = 0
        list(choices)
        print("="*10,"menu","="*10)
        for i in choices:
            range = range + 1
            print(f"#"+i,range)
        print("="*26)
        #----------------------------------
        global registerinput
        registerinput = int(input('>:'))

        if registerinput == 1:
            cadastro()
        
        if registerinput == 3:
            exit()

        if registerinput == 2:
            vercadastro()
        

    menu(['Cadastro','Ver-cadastros','Sair'])
    system("clear")
