import requests 
import json
#API собственно, не трогай
API = '6c39b074-59ea-4ce3-8924-c1b26f5e9137'
#запрос, можешь попробовать подправить, но так тоже хорошо выдает
TEXT = 'Новочебоксарск, кафе'
#колличество запросов, то есть заведений которых код выдаст, максимум 50
RESULTS = 10

response = requests.get(f'https://search-maps.yandex.ru/v1/?apikey={API}&text={TEXT}&lang=ru_RU&results={RESULTS}')
text = json.loads(response.text)
print(len(text['features']))
for i in text['features']:
    #тут по порядку: название, вид, описание, адресс, номер, время работы. Делай с ними что хочешь в этом цикле
    name = i['properties']['CompanyMetaData']['name']
    clas = i['properties']['CompanyMetaData']['Categories'][0]['name']
    description = i['properties']['description']
    address = i['properties']['CompanyMetaData']['address']
    phone = i['properties']['CompanyMetaData']['Phones'][0]['formatted']
    hours = i['properties']['CompanyMetaData']['Hours']['Availabilities']
    print(name, '\n', clas, '\n', description, '\n', address, '\n', phone, '\n', hours, '\n')
