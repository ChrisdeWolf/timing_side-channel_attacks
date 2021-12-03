import requests
import statistics

inputPass = input("Password Guess: ")
respTimes = []
for i in range(10):
    response = requests.post('http://127.0.0.1:5000/login', data={'username':'admin','password':str(inputPass)})
    respTime = response.elapsed.total_seconds()
    respTimes.append(respTime)
print('avg: '+statistics.mean(respTimes))