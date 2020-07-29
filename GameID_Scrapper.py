import subprocess
import sys


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


ans = {}


for i in range(23266, 99999):
    # for i in range(1,2):

    gid = 'CUSA'+str(i).zfill(5)+'_00'

    myurl = 'https://ps4database.io/view/'+gid+'/NP'

    r = requests.get(myurl)

    html_doc = r.text

    soup = bs(html_doc, 'html.parser')

    print(gid)
    print(soup.find_all('h1')[0].string)
    # print([i.string for i in soup.find_all('li')])
    # print([i.string for i in soup.find_all('td')][:10])
    # print([i for i in soup.find_all('td')][10:11])

    ans[gid] = [
        soup.find_all('h1')[0].string,
        [i.string for i in soup.find_all('li')],
        [i.string for i in soup.find_all('td')][:10],
        [i for i in soup.find_all('td')][10:11]
    ]

    with open('file.csv', 'a', encoding='utf8') as f:
        f.write(gid+repr(ans[gid])+'\n')


print(ans)


# import csv
# csv_columns = ['No','Name','Country']
# dict_data = [
# {'No': 1, 'Name': 'Alex', 'Country': 'India'},
# {'No': 2, 'Name': 'Ben', 'Country': 'USA'},
# {'No': 3, 'Name': 'Shri Ram', 'Country': 'India'},
# {'No': 4, 'Name': 'Smith', 'Country': 'USA'},
# {'No': 5, 'Name': 'Yuva Raj', 'Country': 'India'},
# ]
# csv_file = "Names.csv"
# try:
#     with open(csv_file, 'w') as csvfile:
#         writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
#         writer.writeheader()
#         for data in dict_data:
#             writer.writerow(data)
# except IOError:
#     print("I/O error")
