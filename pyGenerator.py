import os
from os import listdir
from os.path import isfile,join

def main():
    mypath = os.getcwd()
    onlyfile = [f for f in listdir(mypath) if isfile(join(mypath, f)) and str(f).endswith('.ui')]

    for i in onlyfile:
        os.system('pyuic5 -x '+str(i)+' -o '+str(i).replace('.ui','.py'))

if __name__ == "__main__":
    main()
