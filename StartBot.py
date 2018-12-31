import requests
from time import sleep

token = "751262939:AAE5FjCoyoFxcz4I_EW7M7l1opcMbECXXbo" 
alphabet = "abcdef0123456789"
hostname = ""

last_update = 0;

url = "https://api.telegram.org/bot" + token + "/"

def checkKey(key):
	if (len(key) != 32): return False
	for i in range(len(key)):
		if (alphabet.find(key[i]) == -1): return False
	return True

def get_updates_json(request):  
    response = requests.get(request + 'getUpdates')
    return response.json()


def last_update(data):  
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]


def get_chat_id(update):  
    chat_id = update['message']['chat']['id']
    return chat_id

def get_mess(update):
	text = update['message']['text']
	return text;

def send_mess(chat, text):  
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response


def providemess(server_ans):
	if checkKey(get_mess(server_ans)) == True:
		send_mess(get_chat_id(server_ans), "Ключ успешно активирован!")
	else:
		send_mess(get_chat_id(server_ans), "Неверный ключ активации!")
	return

def main():  
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
        	providemess(last_update(get_updates_json(url)))
        	update_id += 1
        sleep(1)       

if __name__ == '__main__':  
    main()

