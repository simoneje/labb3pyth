import requests
import json
import sys
#sokTermer = []
savedVal = []


class meny():
    def __init__(self):   
        self.Meny()

    def Meny(self):
        
        while True:
            choice = input('\n1)Välj film\n2)Visa senaste sökningar\n3)Avsluta\n')    
            if choice == '1':
                MovieDB()
                #Meny(self)                 
                break
            elif choice == '2':
                SokHistorik()
                DoubleMeny()
                #Meny(self)
                    #print('1)Visa information om senaste sökningar\n2)Visa information om vald sökt film\n')
                break
            elif choice == '3':
                #sys.exit()
                break
            else:
                break
                #Meny(self)

class MovieDB():
    global savedVal
    def __init__(self):
        self.SearchFilm()

    def SearchFilm(self):
        try:
            iput = input('Sök\n')
            sokHist.AddTerm(input)
            #sokTermer.append(iput) + ', '
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
                    idGetFilm = filmVal["imdbID"]
                    newSearch = requests.get(f"http://www.omdbapi.com/?i={idGetFilm}&apikey=3dde47b4")
                    newData = newSearch.json()
            except FileNotFoundError:
                print(FileNotFoundError)
            try:
                with open('savedsearch.json', 'w', encoding="utf-8") as jsonfil2:
                    json.dump(newData, jsonfil2, ensure_ascii=False, indent=2)
            except FileNotFoundError:
                print(FileNotFoundError)
            print(LastSearch())
        except: print('försök igen')
   

class LastSearch():
    def __init__(self):
        self.serHist()
    def serHist(self):
        with open('savedsearch.json', 'r', encoding='utf-8') as file_read:
            p = json.load(file_read)
        IDplacehold = p['imdbID']
        print("\nNamn: ",p['Title'],"\nRelease: ",p["Released"],"\nIMDB rating: ",p["imdbRating"],f"\nLänk: https://www.imdb.com/title/{IDplacehold}/?ref_=hm_fanfav_tt_3_pd_fp1","\nGenre: ",p["Genre"],"\nSkådepselare: ",p["Actors"],"\nTyp: ",p['Type'],"\nBild: ",p['Poster'],"\nStory: ",p["Plot"])


class SokHistorik():

    def __init__(self):
        self.sokTermer = []
        self.historiken()
    
    def AddTerm(self, value):
        self.sokTermer.append(value)

    def historiken(self):
        for s in self.sokTermer:
            print(s)
        
        # if value in sokTermer:
        #     ind = value.strip('"\[]')
        #     history.append(ind)
        # histlist = []
        # histdict = {}
        # histlist = sokTermer
        # histdict = histlist
        # hero = json.dumps(histdict)
        # # for i in sokTermer:
        # #     histlist.append({i[0]})
        # try:
        #     with open('historiksok', 'w', encoding="utf-8") as jsonfil3:
        #         json.dump(hero, jsonfil3, ensure_ascii=False, indent=2)
        # except FileNotFoundError:
        #     print(FileNotFoundError)

class DoubleMeny():    
    def __init__(self):
        self.menyTva()

    def menyTva(self):
        choice = input('\n1)Visa info om senaste sökningar\n2)Visa info om senast vald sökning\n3)Gå tillbaka\n')
        while True:
            if choice == '1':
                #print("\nNamn: ",savedVal[0],"\nRelease: ",savedVal[1],"\nID: ",savedVal[2],"\nTyp: ",savedVal[3],"\nBild: ",savedVal[4])
                print(savedVal)
                self.menyTva()                 
                break
            elif choice == '2':
                LastSearch()
                self.menyTva()
                break
            elif choice == '3':
                meny()
            else:
                self.menyTva()

    





sokHist = SokHistorik()