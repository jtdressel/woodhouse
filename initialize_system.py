#determine where config files are
import subprocess
import struct
#if needed install dropbox


#if dropbox is set up

print("stuff")
subprocess.call(["ls","-l"])

if((struct.calcsize("P") *8) is 32):
    print "32 bit archetecture"
#TODO: insert code to check if already installed    subprocess.call('cd ~ && wget -O - "https://www.dropbox.com/download?plat=lnx.x86" | tar xzf -', shell = True)
elif((struct.calcsize("P") * 8) is 64):
    print "64 bit archetecture"
#subprocess.call('~/.dropbox-dist/dropboxd', shell=True)
#todo determine if you can pass parameters to this.

#download dropbox control script

#TODO: set apt-name
apt = "apt-get"
subprocess.call("sudo " + apt + " install git -y", shell=True)


def config_git(email, name):
    subprocess.call("git config --global user.email " + email, shell=True)
    subprocess.call("git config --global user.name " + name, shell=True)

# config_git("ubergeek@jamesdressel.com", "'James Dressel'")