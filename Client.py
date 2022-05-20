import socket
import random

f = open('data.txt', 'a')
port1 = 8000
port2 = 8001
i = 0
s = {}
try:
    while True:
        s[i] = socket.socket()

        initialCode = random.randrange(1000, 9999)
        print(' --- The unique code for connecting to server 1 is:', initialCode, ' ---')
        print('Please select one of the 2 options: ')
        print(' - Press 1 if you want to continue and provide the unique code.')
        print(' - Press 2 if you want to quit this program.')
        menu = int (input())
        if ( menu == 1):
            print('Please provide the unique code now.')
            identify = int(input())
            if (identify == initialCode):
                s[i].connect(('localhost', port1))
                data = s[i].recv(1024)
                dataCode = s[i].recv(4069)
                print(data.decode() + dataCode.decode())
                # print(dataCode.decode())

                print("Please enter the unique code you received after connecting to server1 ( port = 8000 )")
                uniqueCode = int(input())

                if (uniqueCode == int(dataCode)):
                    s[i].close()
                    s[i] = socket.socket()

                    print("Good job you managed to connect to server2")
                    s[i].connect(('localhost', port2))
                    data = s[i].recv(1024)
                    print(data.decode())
                    data = s[i].recv(1024)
                    print(data.decode())
                    clientMessage = str(input())
                    f.write(clientMessage + '\n')
                    print('\n')
                    i += 1

                else:
                    ok = 0
                    s[i].send(str(ok).encode())
                    print("Sorry the code you entered is not right! Stopping your connection")
                    s[i].close()
                    print('\n')
                    print("Your connection was stopped!")
                    print('\n')
                    i += 1

            else:
                print("Sorry the code you provided is incorrect! Stopping your connection now!")
                s[i].close()
                print('\n')
                print("Your connection was stopped!")
                print('\n')
        else:
            quit()




except KeyboardInterrupt:
    print("Caught keyboard interrupt, exiting!")
    s[i].close()
    quit()