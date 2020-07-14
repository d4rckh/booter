import time

toddos = input('what would you like to ddos? ')

i = 0

while True:
    print('[bot' + str(i) + '] ddosing ' + str(toddos))
    time.sleep(1)
    i = i + 1
    if i == 5:
        print('ddos succesffully')
        exit()
    
