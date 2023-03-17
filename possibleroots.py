while True:
    try:
        entrance=input("Enter Integer: ")
        if entrance== 'stop':
            break
        if entrance==1:
            print(f'{entrance} to the power of {entrance}')
            continue
        given_number_search = int(entrance)
        turns_tried = 0
        equal_halves=given_number_search%2
        for number_search in range(2,int(given_number_search/2)+1):
            if equal_halves==0 and number_search%2==0 and given_number_search%number_search==0:
                number_searcheven= number_search
                number_of_turns = 1
                for root in range((int(given_number_search/2))) :
                    number_searcheven =number_searcheven * number_search
                    number_of_turns= number_of_turns+1
                    #print(number_searcheven)
                    if number_searcheven == given_number_search:
                        turns_tried=turns_tried+1
                        print(f'{number_search} to the power of {number_of_turns}')
                    elif number_searcheven > given_number_search:
                        #print(number_searcheven)
                        #print('next number')
                        break
            elif equal_halves >0 and number_search%2>0 and given_number_search%number_search==0:
                number_searchodd = number_search
                #print(number_search)
                number_of_turns = 1
                for root in range(int(given_number_search / 2)):
                    number_searchodd = number_searchodd * number_search
                    number_of_turns = number_of_turns + 1

                    if number_searchodd == given_number_search:
                        turns_tried = turns_tried + 1
                        print(f'{number_search} to the power of {number_of_turns}')
                        continue

        if turns_tried==0:
            print(f'{given_number_search} has no possible root')


    except:
        print('INTEGER only')

