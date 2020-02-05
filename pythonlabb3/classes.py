import requests
import json
class meny():

    def __init__(self):
    
        def Meny(self):
            choice = int(input('1)Välj film\n2)Visa senaste sökningar\n3)Avsluta\n'))
            while True:
                if choice == 1:
                    MovieDB()                 
                    break
                elif choice == 2:
                    print('1)Visa information om senaste sökningar\n2)Visa information om vald sökt film\n')
                    break
                elif choice == 3:
                    break
        
    
        Meny(self)

class MovieDB():
    def __init__(self):
        def SearchFilm(self):
            iput = input('Sök\n')
            
            search = requests.get(f'http://www.omdbapi.com/?i=tt3896198&apikey=3dde47b4&s={iput}')
            data = search.json()
            try: 
                with open('hej.json', 'w', encoding="utf-8") as big:
                    json.dump(data, big, ensure_ascii=False, indent=2)
            except FileNotFoundError as error:
                print(error)
            lol = data['Search']
            count = 0
            for i in lol:
                count += 1
                print(count,i['Title'],i['Year'])
            
            nsearch = input('Skriv exakt vilken title du menar')
            for u in range(len(lol)):
                
                if nsearch == lol[u]['Title']:
                    try:
                        with open('savedsearch.json', 'w', encoding="utf-8") as jobb:
                            json.dump(lol[u], jobb, ensure_ascii=False, indent=2)
                    except FileNotFoundError:
                        print(FileNotFoundError)
                    print(lol[u])

                
            
            
        SearchFilm(self)
        
        #def SortFilm(self, filename):
            #newlist = [] 
            #listig = []          
            #try:
            #    with open('hej.json', encoding="utf-8") as sJson:
            #        newlist = json.load(sJson)                                    
            #except FileNotFoundError as error:
            #    print(error)









