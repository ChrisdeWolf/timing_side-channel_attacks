import requests
import statistics

respTimes = []
for i in range(20):
    response = requests.post('http://127.0.0.1:5000/login', data={'username':'deWolf','password':'j3rySeKr3t123'})
    respTime = response.elapsed.total_seconds()
    respTimes.append(respTime)

print('avg: ')
print(statistics.mean(respTimes))