import os
import subprocess


def update_progress(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█'):
    percent = ("{0:." + str(decimals) + "f}").format(100 *
                                                     (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end='\r')

    if iteration == total:
        print()


# Config
wordlist_file = 'rockyou-75.txt'
input_file = 'LAND2.BMP'
output_file = input_file[:-4] + ".txt"
steghide_path = 'D:\\ctf\\tools\\steghide\\steghide.exe'

print('[i] File:', input_file)


i = 0
with open(wordlist_file, 'r') as wordlist:
    passwords = wordlist.readlines()
    total = len(passwords)
    for i, password in enumerate(passwords):
        password = password.strip()
        command = steghide_path + ' --extract --stegofile ' + \
            input_file + ' --passphrase ' + password + ' --extractfile '+output_file

        result = subprocess.run(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        update_progress(i, total, 'Progress:', password)

        if os.path.exists(output_file):
            print("extracted using:", password)
            print("see:", output_file)
            break
