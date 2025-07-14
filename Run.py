#!/usr/bin/python3
_A='bold dodger_blue3'
try:import requests,re,json,time,datetime,os,random,base64,binascii,struct,io,uuid,urllib,sys,urllib.parse,hashlib,string;from concurrent.futures import ThreadPoolExecutor;from urllib.parse import quote;from requests.exceptions import RequestException;from platform import platform;from nacl.public import PublicKey,SealedBox;from rich.console import Console;from rich.panel import Panel;from Crypto.Cipher import AES,PKCS1_v1_5;from rich import print;from rich.tree import Tree;from rich.columns import Columns;from Cryptodome.Cipher import AES;from Cryptodome import Random as randoms;from Crypto.PublicKey import RSA;from Crypto.Random import get_random_bytes
except Exception as e:import os,urllib.parse;os.system(f"xdg-open https://wa.me/6283847921480?text=FACEMASH%20%3A%20{urllib.parse.quote(str(e))}");exit()
os.system('cls'if os.name=='nt'else'clear')
Console(width=65,style=_A).print(Panel('[bold red]●[bold yellow] ●[bold green] ●\n[bold red]___________                                         .__     \n\\_   _____/____    ____  ____   _____ _____    _____|  |__  \n |    __) \\__  \\ _/ ___\\/ __ \\ /     \\\\\\__  \\  /  ___/  |  \\ \n |     \\   / __ \\\\  \\__\\  ___/|  Y Y  \\/ __ \\_\\___ \\|   Y   \\\n[bold white] \\___  /  (____  /\\___  >___  >__|_|  (____  /____  >___|  /\n     \\/        \\/     \\/    \\/      \\/     \\/     \\/     \\/ \n  [bold white]|| Author :[bold green] Rozhak[bold white] || Version :[bold red] 1.0.0[bold white] || Type :[bold green] Premium[bold white] ||'))
Console(width=65,style=_A).print(Panel(f"""[bold red]Maaf,[/][bold white] Anda Harus Menggunakan Perangkat [bold cyan]64-Bit[/][bold white] Dan Python Ver
si [bold cyan]3.12 Ke Atas[/][bold white] Untuk Menjalankan Script Ini.

Jika Anda Menggunakan Termux, Jalankan Perintah Berikut Di Terminal Anda:

[bold green]$ cd $HOME/Facemash
$ chmod +x Run
$ ./Run[/]

[bold yellow]Peringatan![/][bold white] Script Ini Hanya Untuk Tujuan Pembelajaran. Jan
gan Gunakan Untuk Hal Negatif! Kami Tidak Bertanggung Jawab Atas Segala Akibat Yang Ditimbulkan Jika Anda Melanggar.""",title='>> [Welcome] <<'))