"""CSUAyyy
One command to launch a jupyter notebook server on CSUA! 

Usage:
  csuayyy config
  csuayyy serve
  csua config
  csua serve
"""

import pexpect
from termcolor import colored
import argparse
import json
import os
from pathlib import Path

def alert(msg, clr):
        print(colored(msg, clr))

class Process:
    def __init__(self, initial, debug=False):
        print('>>>', initial)
        self.spawn = pexpect.spawn(initial)
        self.debug = debug

    def read(self):
        allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 \n\t~`!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?"
    
        last = ''
        token = ''
        while last != ' ' and last != '\n':
            last = self.spawn.read(1).decode("utf-8")
            if last.lower() in allowed:
                token += last

        if self.debug:
            print(token, end='')
        
        return token, last == '\n'

    def write(self, msg, obscure=False):
        self.spawn.sendline(msg)
        if self.debug:
            if obscure:
                msg = ''.join(['*' for _ in msg])
            print(">>>", msg)

    def expect(self, to_expect):
        self.spawn.expect(to_expect)

    def run_router(self, router):
        this_line = ''
        while True:
            token, is_new_line = self.read()  
            this_line += token

            clear_line, escape = router(this_line, token, is_new_line)
            if escape:
                break
                
            if is_new_line or clear_line:
                this_line = ''

def get_home():
    return str(Path.home())

def serve():    
    if os.path.exists(get_home() + '/.ssh/config.json'):
        with open(get_home() + '/.ssh/config.json', 'r') as json_file:
            data = json.load(json_file)
            username = data['username']
            password = data['password']
            id_rsa = data['id_rsa']

        alert("CSU-Ayyy! \N{winking face}", 'magenta')
        alert("Starting ssh...", 'yellow')
        server = Process('ssh -i ' + id_rsa + ' ' + username + '@latte.csua.berkeley.edu', debug=True)

        url = None

        def server_router(this_line, token, is_new_line):
            if "Identity file" in this_line and "not accessible" in this_line:
                alert(
                    "Identity file, " + 
                    id_rsa + 
                    " does not exist. Run config again.", 
                    'red'
                )
                exit()
            elif "(yes/no/[fingerprint])?" in this_line:
                alert("Adding fingerprint...", 'yellow')
                server.write("yes")
                return True, False
            elif "Permission denied" in this_line and is_new_line:
                alert("Authentication failed. Run config again.", 'red')
                exit()
            elif "password: " in this_line:
                server.write(password, obscure=True)
                alert("Authenticated", 'yellow')
                return True, False
            elif '$ ' in this_line:
                server.write('jupyter notebook')
                alert("Started Jupyter", 'yellow')
                return True, False
            elif 'http' in token and '?token=' in token:
                server_router.url = 'http' + token.split('http')[1]
                print("URL:", url)
                return True, True

            return False, False

        server.run_router(server_router)

        port = server_router.url.split(':')[-1].split('/')[0]
        print(colored("Connecting your port 8888 to server port " + port + "...", 'cyan'))

        cmd = 'ssh -i ' + id_rsa + ' -N -L 8888:localhost:' + port + ' ' + username + '@latte.csua.berkeley.edu'
        local = Process(cmd)


        local.expect("password: ")
        alert("Authenticating...", 'cyan')
        local.write(password)
        local.expect('\n')

        alert("Open: " + server_router.url.replace(port, '8888'), 'green')
  
        while True:
            pass
    else:
        alert("Please run csuayyy config first!", 'red')

def config():
    username = input("CSUA username: ")
    password = input("CSUA password: ")
    id_rsa = input("Path to id_rsa.pub file: ")

    data = {
        'username': username,
        'password': password,
        'id_rsa': id_rsa
    }

    os.makedirs(get_home() + '/.ssh', exist_ok=True)
    with open(get_home() + '/.ssh/config.json', 'w') as outfile:
        json.dump(data, outfile)

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('mode', nargs='?')
    parser.add_argument('--debug', action='store_true')

    args = parser.parse_args()

    if args.mode == 'config':
        config()
    elif args.mode == 'serve':
        serve()
    else:
        test()

