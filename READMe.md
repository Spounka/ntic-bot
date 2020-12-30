# NTIC-BOT
A Discord bot created in python for the NTIC students discord group

## What can it do ?
TODO:  
.  
.  
.  

## How to get started ?
----
### <center> Windows </center>
-----
1. First, download python version 3.8.6:
    \[[32 bits](https://www.python.org/ftp/python/3.8.6/python-3.8.6.exe)\]
    \[[64 bits](https://www.python.org/ftp/python/3.8.6/python-3.8.6-amd64.exe)\]  

    Next follow the installation  
    ![Python1](markdown/Python%201.png)  
    Make sure to add to path:  
    ![python2](markdown/Python%202.png)  
    Choose Customize installation:  
    ![Python3](markdown/Python%203.png)  
    Make sure to add pyhton to environment variables:  
    ![Python4](markdown/Python%204.png)

    Click next and wait for the installation to finish  
2. Clone this repository somewhere using:  

       git clone https://github.com/Spounka/ntic-bot.git

3. Create a virtual environment
   1. Open a terminal / shell and execute the following: 
   ```
   python -m venv .venv // replace .venv with a folder name you want
   ```
   2. If (replace `.venv` with your folder):
      1. You use `PowerShell` execute `\.venv\Scripts\Activate.ps1`
      2. You use `CMD` execute `\.venv\.Scripts\Activate.bat` 

4. Finally execute: `pip install -r requirements.txt`

---
### <center>Linux</center>
---
> **This bot needs version 3.8.6** if you have a newer / older version, 
please refer to **[pyenv](https://github.com/pyenv/pyenv)** for more details

On `Arch Linux` you can install pyenv using:

    yay -S pyenv
Or:

    git clone https://aur.archlinux.org/yay.git
    cd yay
    makepkg -sci
Finally install python 3.8.6 using:

    pyenv install 3.8.6

1. Create a virtual environment using:

       python3 -m venv .venv
    Or if you using `pyenv`

        pyenv exec python -m venv .venv
    (change `.venv` to something you want)

2. Activate the env using (change `.venv` to your folder name):
   
       source ./.venv/bin/activate

3. Run `pip` to install dependencies

       pip3 install -r requirements.txt
    
---
# <center>You're Ready To go! </center>