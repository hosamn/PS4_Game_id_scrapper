import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


try:
    from bs4 import BeautifulSoup as bs
except:
    install(beautifulsoup4)
    from bs4 import BeautifulSoup as bs


try:
    import requests
except:
    install(requests)
    import requests



'''
import requests

r = requests.get(myurl)

test = [
  r,
  r.status_code,
  r.headers['content-type'],
  r.encoding
  # r.text
]

for i in test : print(i)
'''




idli = [
    'CUSA00341',
    'CUSA00419',
    'CUSA00458',
    'CUSA00465',
    'CUSA00694',
    'CUSA00967',
    'CUSA01015',
    'CUSA01141',
    'CUSA01163',
    'CUSA01627',
    'CUSA02048',
    'CUSA02299',
    'CUSA02320',
    'CUSA04195',
    'CUSA05637',
    'CUSA05999',
    'CUSA07408',
    'CUSA08034',
    'CUSA08829',
    'CUSA10115',
    'CUSA11599',
    'CUSA11772',
    'CUSA12421'
    ]


ans = {}


for i in idli:

    myurl = 'https://ps4database.io/view/'+i+'_00/NP'

    r = requests.get(myurl)

    html_doc = r.text

    # print(html_doc)

    soup = bs(html_doc, 'html.parser')

    '''
    soup.title
    soup.title.name
    soup.title.string
    soup.title.parent.name
    soup.p
    soup.p['class']
    soup.a
    soup.find_all('a')
    soup.find(id="link3")
    '''

    # html body div.jumbotron.avknJumbo div.container h1.display-3
    # /html/body/div[1]/div/h1

    print(soup.find_all('h1')[0].string)

    # (soup.find_all('h1')[0].string)



