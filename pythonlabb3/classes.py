import requests
import json
import sys
sokTermer = []
savedVal = []
class meny():
    def __init__(self):   
        def Meny(self):
            choice = int(input('1)Välj film\n2)Visa senaste sökningar\n3)Avsluta\n'))
            while True:
                if choice == 1:
                    MovieDB()
                    Meny(self)                 
                    break
                elif choice == 2:
                    print(sokTermer)
                    DoubleMeny()
                    Meny(self)
                    #print('1)Visa information om senaste sökningar\n2)Visa information om vald sökt film\n')
                    break
                elif choice == 3:
                    sys.exit()
                    break    
        Meny(self)

class MovieDB():
    global sokTermer
    global savedVal
    def __init__(self):
        def SearchFilm(self):
            try:
                iput = input('Sök\n')
                sokTermer.append(iput)
                try:
                    search = requests.get(f'http://www.omdbapi.com/?i=tt3896198&apikey=3dde47b4&s={iput}')
                    data = search.json()
                except: print('oj')
                try: 
                    with open('hej.json', 'w', encoding="utf-8") as big:
                        json.dump(data, big, ensure_ascii=False, indent=2)
                except FileNotFoundError as error:
                    print(error)
                lol = data['Search']
                count = 0
                for i in lol:
                    count +=1
                    print(count,')',i['Title'],i['Year'])                            
                nsearch = int(input('Skriv siffran på filmen du vill ha\n'))
                try:
                    with open('hej.json', 'r', encoding="utf-8") as jsonfil1:
                        searchRes = json.load(jsonfil1)
                        filmVal = searchRes.get('Search')[nsearch-1]
                        savedVal.append(filmVal)
                except FileNotFoundError:
                    print(FileNotFoundError)
                try:
                    with open('savedsearch.json', 'w', encoding="utf-8") as jsonfil2:
                        json.dump(filmVal, jsonfil2, ensure_ascii=False, indent=2)
                except FileNotFoundError:
                    print(FileNotFoundError)
            except: print('försök igen')                       
        SearchFilm(self)    

class LastSearch():
    def __init__(self):
        def serHist(self):
            with open('savedsearch.json', 'r', encoding='utf-8') as file_read:
                p = json.load(file_read)
                print(p)
        
        serHist(self)


class DoubleMeny():    
    def __init__(self):
        def menyTva(self):
            choice = int(input('1)Visa info om senaste sökningar\n2)Visa info om senast vald sökning\n3)Gå tillbaka\n'))
            while True:
                if choice == 1:
                    print(savedVal)
                    menyTva(self)                 
                    break
                elif choice == 2:
                    LastSearch()
                    menyTva(self)
                    break
                elif choice == 3:
                    meny()
        menyTva(self)







