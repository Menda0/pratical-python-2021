# https://api.spaceflightnewsapi.net/v3/articles
# public apis https://github.com/public-apis/public-apis

# 1. Use reuqest to get space news
# 2. Write all the news inside a csv file
# 3. id, title, imageUrl, summary, url

# From Henrique
import requests
import csv

#pedido ao web service
response =  requests.get("https://api.spaceflightnewsapi.net/v3/articles")
#conversao da resposta em json
artigos = response.json()

#abertura do ficheiro para escrita
with open('artigos.csv', 'w',newline = '') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ') 
    #linha de titulo
    linha = ['ID', 'TITLE', 'IMAGE_URL', 'SUMMARY','URL']
    #escrita da linha par ao csv
    spamwriter.writerow(linha)
    #restantes linhas
    for f in artigos:
       # print(f["id"])
        #print(f["title"])
        #print(f["imageUrl"])
        #print(f["summary"])
        #print(f["url"])
        linha = [f["id"], f["title"], f["imageUrl"], f["summary"], f["url"]]
        #escrita da linha para o ficheiro csv 
        spamwriter.writerow(linha)


""" with open('artigos.csv', 'w',newline = '') as csvfile:
    
    spamwriter = csv.writer(csvfile, delimiter=' ') 

    for a in artigos:

        line = 

        spamwriter.writerow(fib_line) """

 