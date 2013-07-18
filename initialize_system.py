#!/usr/bin/python
#Currently unstable. Don't use.

#determine where config files are
import subprocess
import struct
import re
#if needed install dropbox


#if dropbox is set up


def install_dropbox():
    if((struct.calcsize("P") *8) is 32):
    #TODO: insert code to check if already installed    
        subprocess.call('cd ~ && wget -O - "https://www.dropbox.com/download?plat=lnx.x86" | tar xzf -', shell = True)
        subprocess.call('~/.dropbox-dist/dropboxd', shell=True)#TODO download management
    elif((struct.calcsize("P") * 8) is 64):
        subprocess.call('cd ~ && wget -O - "https://www.dropbox.com/download/?plat=lnx.x86_64" | tar xzf -', shell = True)
        subprocess.call('~/.dropbox-dist/dropboxd', shell=True)
#todo determine if you can pass parameters to this.

#download dropbox control script



#TODO: set apt-name
apt = "apt-get"

def install_git():
    subprocess.call("sudo " + apt + " install git -y", shell=True)


def config_git(email, name):
    subprocess.call("git config --global user.email " + email, shell=True)
    subprocess.call("git config --global user.name " + name, shell=True)

# config_git("ubergeek@jamesdressel.com", "'James Dressel'")
def config_git_editor(editor):
    #TODO: test this code
    p = re.compile(r'"(?!").+"$')
    m = p.match(editor)
    if(m):
        subprocess.call('git config --global core.editor ' + editor, shell=True)
    else:
        subprocess.call('git config --global core.editor vim', shell=True)

def config_gitignore(gitignore):
    subprocess.call('git config --global core.excludesfile ' + gitignore, shell=True)

def set_ssh_config(config):
    subprocess.call("ln -ifb " + config + " ~/.ssh/config",shell=True)

def set_aliases(aliases):
    subprocess.call("ln -ifb " + aliases + " ~/.bash_aliases", shell=True)

def set_profile(profile):
    subprocess.call("ln -ifb " + profile + " ~/.profile", shell=True)

def set_bashrc(bashrc):
    subprocess.call("ln -ifb " + bashrc + " ~/.bashrc", shell=True)

def part_a():
    install_dropbox()
    install_git()
    config_git("ubergeek@jamesdressel.com", "'James Dressel'")
    config_git_editor('"vim"')
def part_b():
    config_gitignore("~/Dropbox/config/.gitignore_global")
    set_ssh_config("~/Dropbox/config/ssh_config")
    set_aliases("~/Dropbox/config/.bash_aliases")
    set_profile("~/Dropbox/config/.profile")
    set_bashrc("~/Dropbox/config/.bashrc")

part_a()
#part_b()

