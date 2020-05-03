import os

while True:
    all_files = os.listdir("./ELF0/0/")
    if len(all_files)==1 and os.path.isdir("./ELF0/0/"+all_files[0]) and all_files[0]=='0':
        os.system('mv ./ELF0/0/0 ./ELF0/1;rm -rf ./ELF0/0;mv ./ELF0/1 ./ELF0/0')
    else:
        break



