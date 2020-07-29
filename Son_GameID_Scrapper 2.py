import subprocess
import sys
import os

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    from bs4 import BeautifulSoup as bs
except:
    install('beautifulsoup4')
    from bs4 import BeautifulSoup as bs

try:
    import requests
except:
    install('requests')
    import requests

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# for i in range(1,99999):
# for i in range(1386,99999):
# for i in range(5991,99999):
# for i in range(6155,99999):
# for i in range(9342,99999):
# for i in range(9338,99999):
for i in range(14548,99999):

    gid = 'CUSA'+str(i).zfill(5)+'_00'
    
    myurl = 'https://store.playstation.com/en-us/product/' + gid

    print('{:.2f}%'.format(i/99999*100),'Requesting', myurl, end='  >  ')
    r = requests.get(myurl)

    html_doc = r.text

    soup = bs(html_doc, 'html.parser')

    # if soup.find_all("div", class_="not-found__title"):
            
    try:
        print('Got ',gid, 'With Title ', soup.find_all('h2')[0].string)

        psnFile = 'psnFiles/' + gid + '.html'
        with open( psnFile,'w',encoding='utf8') as f:
            f.write(repr(html_doc).replace('\\n',''))
    except:
        print('Unable to Find This Page')
        # continue