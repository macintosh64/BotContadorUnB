import tweepy
import datetime

key =  '1Oi0WJk3YEKkMdzk2hpUNagiT'  #Acess
secret = 'wO4RsWWfkHLucaXBpiCiMAmEUlaBO0nUYWRuoSm13K1Tos7X6e' #Chave secreta

consumer_key = '1414662745845346308-u1vGOtFvxo59akIBjb3irG0ngHeOB9' #API
consumer_secret = 'wQ7a7CWOivYt3HTFXnyHM5YurFXM6OrdBqc04dMF72aC3' #Chave secreta

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)


termino_aulas = datetime.date(2021,11,7) #Último dia de aula
hoje = datetime.date.today() #Dia de hoje

resto_dias_horas = termino_aulas - hoje # Diferença entre os dias colocados anteriormente (Tempo para o fim do período)
resto_dias = resto_dias_horas.days  #Quantidade em dias

#Agora vamos inserir as porcentagens

# Primeiro o total de dias
total_dias = 111

# Dias que já se passaram
dias_passaram =  total_dias - resto_dias

# Dias que já se passaram dividido pelo total
porcentagem = dias_passaram / total_dias

#Temos que separar o caso em que falta apenas 1 dia, para poder mudar "dias" para "dia" no tweet

if resto_dias !=1:

    if resto_dias % 10 == 0: #Testando para ver se o dia é um multiplo de 10
        api.update_status("Bom dia, estudante! Faltam " + str(resto_dias) + " para terminar o 2021.1 na UnB. Você já cursou " + str(porcentagem) + "%" + "do período! :)")
       
    if resto_dias % 10 != 0: #Testando para ver se o dia é um multiplo de 10
        api.update_status("Bom dia, estudante! Faltam " + str(resto_dias) + " para terminar o 2021.1 na UnB. Você já cursou " + str(porcentagem) + "%" + "do período! :)")
        

if resto_dias == 1:
    api.update_status("Bom dia, estudante! Falta " + str(resto_dias) + " para terminar o 2021.1 na UnB. Você já cursou " + str(porcentagem) + "%" + "do período! :)")
