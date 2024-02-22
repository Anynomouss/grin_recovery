## Author: Anynomous
## Dependencies
## Don't forget to install mimlewimble.py: python -m pip install .
import json    
import os
import sys
import mimblewimble
from mimblewimble.wallet import Wallet

if __name__ == '__main__':
    ## USER INPUT
    '''
    1) Copy the wallet you want to recover the password for into the same directory
    as the script. It is assumed your wallet has the name "wallet.seed"
    2) Run the script with your passwords list as input, see examples below:
     - time cat password_list.txt ../../../Python/Python311/python.exe grin-recover.py
    3) A - Benchmark the speed, measure time it takes to test 10000 passwords single core
     - time printf 'HelloWorld\n%.0s' {1..10000} | ../../Python/Python311/python.exe grin-recover_0.1.py  
    3) B - Benchmark in parallel, settings are chose for 16 thread Ryzen 7
     - time printf 'HelloWorld\n%.0s' {1..100000} |  parallel --pipe -j 16 --blocksize 100000 --spreadstdin ../../Python/Python311/python.exe grin-recover.py
     
     BENCHMARK RESULTS (Ryzen 7):
     - single core 6.693 pwds/second
     - 16 thread 40.0000 pwds/second
     
    3) C - Example using hashcat output with multithreading
    ./hashcat.exe -a1 words.txt endings.txt --stdout |  parallel --pipe -j 16 --blocksize 100000 --spreadstdin ../../Python/Python311/python.exe grin-recover.py
    '''
    target_keystore_file = "wallet.seed"

    ## PASSWORDS are read from standard in (stdin) to allow pyping and multithreading
    passwords = sys.stdin.readlines()
   
    ## 1) Load the data from the keystore wallet in dictionary
    f = open(target_keystore_file)
    blob = f.read()
    seed = json.loads(blob)
        
    ## 2) Loop over all passwords
    for pwd in passwords:
        pwd = pwd.strip()
        password = pwd
        
        ## convert to bytes
        encrypted_seed = bytes.fromhex(seed['encrypted_seed'])
        nonce = bytes.fromhex(seed['nonce'])
        salt = bytes.fromhex(seed['salt'])
        
        ## instantiate the wallet
        w = Wallet(encrypted_seed=encrypted_seed, nonce=nonce, salt=salt)
        
        ## decrypt
        valid = True
        try:
            w.unshieldWallet(password, nonce=nonce, salt=salt)
            ## If found, print to stdout/console and to log.txt file
            if valid: ## Print found password and store to a log file
                print('Password found: {}'.format(password)) 
                with open("log.txt", "a") as f:
                    print("{}:{}".format(target_keystore_file,pwd), file=f)
        except Exception as e:
            if str(e) == 'MAC check failed':
                valid = False