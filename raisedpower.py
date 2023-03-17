
while True:
    print('To LEAVE type: stop  ')
    try:
        enter1=input('Number> ')
        if enter1.lower()=='stop':
            break
        enter2=input('Power> ')
        if enter2.lower()=='stop':
            break

        number = int(enter1)
        power = int(enter2)
        answer=1
        while power>0:
            answer=answer*number
            power=power-1

        print(answer)
    except:
        print('INTEGERS only')
