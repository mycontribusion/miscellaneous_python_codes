print('Testing the kids to read FIGURES between ZERO-TRILLIONS in WORDS')
print('Choose any range:'
      ' that is above zero and less than quadrillion')
import random
first_number = int(input('From: '))
second_number = int(input('To: '))
#range_of_figures= range(first_number,second_number+1)
#print(range_of_figures)
#choosen_figures= 19
#print(choosen_figures)

labelled_numbers = {'zero':'nine',0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',
                    'ten':'hunderd',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',
                    17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'fourty',50:'fifty',
                    60:'sixty',70:'seventy',80:'eighty',90:'ninety',100:'one hundred',
                    'thousand':'trillion',1000:'one thousand',1000000:'one million',1000000000:'one billion',1000000000000:'one trillion',
                    1000000000000000:'one quadrillion'}

while True:
    figure_of_choice = random.randint(first_number, second_number)
    conjugator='and'
    print(figure_of_choice)
    input_of_answer=input('Write the above Figure in Words: ').lower()
    if input_of_answer == 'quit':
        break
    correct_answer1=labelled_numbers.get(figure_of_choice,0)
    #print(labelled_numbers[choosen_figures])
    #if input_of_answer==correct_answer1:
     #   print('Correct')
    #else:
    #    pass


    divide_ten=int(figure_of_choice/10)
    highest_ten= divide_ten * 10
    divide_ten_remainder= figure_of_choice % 10
    divide_hundred=int(figure_of_choice/100)


    stringized_figure=str(figure_of_choice)
    figure_lenght= len(stringized_figure)
    my_limit=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    #print(figure_lenght)


    if figure_lenght==1:
        unit_answer=labelled_numbers[figure_of_choice]
        if unit_answer==input_of_answer:
            print('Correct')
        else:
            print('Wrong')
            print(f'The correct answer is {unit_answer}')


    elif figure_lenght==2:
        unit_ty= labelled_numbers[highest_ten]
        unit=labelled_numbers[divide_ten_remainder]
        answer_for_tens=f'{unit_ty} {unit}'
    #    print(answer_for_tens)
        if answer_for_tens==input_of_answer or input_of_answer==correct_answer1:
            print('Correct')
        else:
            print('Wrong')
            print(f'The correct answer is {answer_for_tens}')


    elif figure_lenght==3:
        int(stringized_figure[2:])
        humdred_word=labelled_numbers[int(figure_of_choice/100)]
        if figure_of_choice%100 >0:
            if figure_of_choice%100 in labelled_numbers==True:
                answer3a= f'{humdred_word} hundred and {labelled_numbers[figure_of_choice%100]}'
                print(answer3a)
                if input_of_answer==answer3a:
                    print('Correct')
                else:
                    print('Wrong')
                    print(f'The correct answer is {answer3a}')
            elif figure_of_choice%100 <=20:
                answer_for_hund=(f'{humdred_word} hundred and {labelled_numbers[figure_of_choice%100]}')
                if input_of_answer==answer_for_hund:
                    print('Correct')
                else:
                    print('Wrong')
                    print(f'The correct answer is {answer_for_hund}')
            elif figure_of_choice % 100 >20:
                highest_ten3 = int((figure_of_choice%100)/10)*10
                divide_ten_remainder3= (figure_of_choice%100) % 10
                unit_ty3 = labelled_numbers[highest_ten3]
                unit3 = labelled_numbers[divide_ten_remainder3]
                if divide_ten_remainder3==0:
                    answer3b= f'{humdred_word} hundred and {labelled_numbers[highest_ten3]}'
                    if input_of_answer==answer3b:
                        print('Correct')
                    else:
                        print('Wrong')
                        print(f'The correct answer is {answer3b}')
                else:
                    answer_for_tens3 = f'{humdred_word} hundred and {unit_ty3} {unit3}'
                    if input_of_answer==answer_for_tens3:
                        print('Correct')
                    else:
                        print('Wrong')
                        print(f'The correct answer is {answer_for_tens3}')
            #    print(answer_for_tens)
        else:
            unit_hundred= f'{humdred_word} hundred'
            if unit_hundred == input_of_answer:
                print('Correct')
            else:
                print('Wrong')
                print(f'The correct answer is {unit_hundred}')


    elif figure_of_choice==1000:
        if input_of_answer==labelled_numbers[figure_of_choice]:
            print('Correct')
        else:
            print('Wrong')
            print(f'The correct answer is {labelled_numbers[figure_of_choice]}')



        


    else:
        pass
