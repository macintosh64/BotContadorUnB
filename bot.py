import tweepy
import datetime

key =  ''  
secret = '' 

consumer_key = '' 
consumer_secret = '' 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)


termino_aulas = datetime.date(2021,11,7) 
hoje = datetime.date.today() 

resto_dias_horas = termino_aulas - hoje 
resto_dias = resto_dias_horas.days 

total_dias = 111

dias_passaram =  total_dias - resto_dias

porcentagem = dias_passaram / total_dias

if resto_dias !=1:
        api.update_status("Bom dia, estudante! Faltam " + str(resto_dias) + " para terminar o 2021.1 na UnB. Você já cursou " + str(porcentagem) + "%" + "do período! :)")
        

if resto_dias == 1:
    api.update_status("Bom dia, estudante! Falta " + str(resto_dias) + " para terminar o 2021.1 na UnB. Você já cursou " + str(porcentagem) + "%" + "do período! :)")
