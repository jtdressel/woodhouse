#determine where config files are
import subprocess
import struct
#if needed install dropbox


#if dropbox is set up


def install_dropbox():
    if((struct.calcsize("P") *8) is 32):
    #TODO: insert code to check if already installed    
        subprocess.call('cd ~ && wget -O - "https://www.dropbox.com/download?plat=lnx.x86" | tar xzf -', shell = True)
    elif((struct.calcsize("P") * 8) is 64):
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
    #TODO: Code to verify editor is in quotes
    subprocess.call('git config --global core.editor ' + editor, shell=True)

def config_gitignore(gitignore):
    subprocess.call('git config --global core.excludesfile ' + gitignore, shell=True)

def set_ssh_config(config):
    subprocess.call("ln -ifb " + config + " ~/.ssh/config",shell=True)

#install_git()
#config_git_editor('"vim"')
#config_gitignore("~/Dropbox/config/.gitignore_global")
set_ssh_config("~/Dropbox/config/ssh_config")
