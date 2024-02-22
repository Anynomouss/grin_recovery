# grin_recovery a Grin Wallet Recovery Tool
Grin recovery is an as easy to use recovery script/tool to recover your grin wallet.
The scripts takes passwords printed from the console as input (STDIN) and tests if your wallet file can be unlocked.
This tool is powered by **Grinventions mimblewimble-py** library:

https://github.com/grinventions/mimblewimble-py  
  
If this tool was useful, you can thank the developer by donating to Grinvention, see the donation address on the GitHub page or any other Grin related fund such as the Grin general or CC fund.  

## How to use grin-recovery
Grin recovery is a Python script, to it requires you to 
1) Install Python (check your distribution, Linux comes with Python preinstalled, Window has Python in its APP store)
2) Install mimblewimble-py 
`python -m pip install mimblewimble`
3) Optionally for multi-threading install gnu-parallel, only works on bash, so on Windows I recommend installing Linux Subsystems for Windows
4) To try different passwords combinations, download Hashcat. Note that Hashcat is not added to the path, so you have to run it from its specific directory, e.g. by pasting this script and your wallet file inside the Hashcat directory:  
https://hashcat.net/hashcat/  
  
## Example command to run this script. 
Note that the test wallet provided with the script has the password "Test123"`. Note that on linux you have to use python 3, which often means you have to replace 'python' with 'python3'in the commands below. Similarly for installing libraries with 'pip', if it doe not work, try 'pip3'

    time cat passwords.txt |python.exe grin-recover.py
    time printf 'HelloWorld\n%.0s' {1..1000000} | ../../Python/Python311/python.exe

### Benchmark speed/time for one million passwords 
**Single Core:**

    time printf 'HelloWorld\n%.0s' {1..1000000} | ../../Python/Python311/python.exe grin-recover_0.1.py  
    
**Multi-threaded:**
    
    time printf 'HelloWorld\n%.0s' {1..10000000} |  parallel --pipe -j 16 --blocksize 10000 --spreadstdin ../../Python/Python311/python.exe grin-recover.py
     
Benchmark results on a Ryzen 7, 8 core 16 threads:
 
     single core 6.700 pwds/second
     multi core 16 thread 40.0000 pwds/second
     
### Example using hashcat output with multithreading

    ./hashcat.exe -a1 words.txt endings.txt --stdout |  parallel --pipe -j 16 --blocksize 100000 --spreadstdin ../../Python/Python311/python.exe grin-recover.py  
  
## Help needed?
In case you cannot figure it out yourself, I can help. You can contact me as user *Anynomous* on https://forum.grin.mw/. Note that I will only help you if you show ample proof (such as knowledge of the password) to proof you are the owner of the wallet.  
For issues with the code you can open a Github Issue.  
  
## Security implications  
The above benchmarks show you that on a decent CPU you can recover/brute-force a Grin wallets with 40.000 passwords per seconds. Should you be worried? No, not really. Bitcoin Core Wallets on a RTX2080-Ti GPU can be brute-forced with a speed of >10.000 passwords per second, while Electrum wallets can be recovered with a speed of close to a billion passwords per second. Having a recovery tool available is a healthy part of any crypt-currencies ecosystem. 
These benchmark results do show you you that you should use a properly safe password like you should for any crypto wallet. E.g. you can use two or three words, some numbers and a special character. Preferably a typo or a custom word to protect against dictionary attack. Using a pin, e.g. 19261231, should be considered unsafe .It would take 8 minutes to brute force such a pin on a Ryzen 7 CPU. Obviously, you should not share your *wallet.seed* file with anyone you do not completely trust with your funds.
  



