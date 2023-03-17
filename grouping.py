import random
number_per=0
number_of_members= 0
class_members = []
no_of_entry=0
#print(number_of_members)
#print(class_members)
while True:
    saka_suna = input('Write Name,(then press ENTER): ').upper()
    no_of_entry= no_of_entry+1
    print(no_of_entry)
    class_members.append(saka_suna)
    #print(class_members)

    if saka_suna == 'UP': break
    number_of_members  = number_of_members + 1
#print(number_of_members)
#print(class_members)
print(f'There are {number_of_members} member(s) in your class')
kaari= number_of_members + 1

divisible_number= []
for number in range(1,kaari):
    #print(number)
    rabawa= number_of_members/number
    #print(rabawa)
    if number_of_members % number==0:
        divisible_number.append(number)

        #print(number)
        number_per= number_per + 1
        print(f"({number_per}) you can have {number} per group")

#print(divisible_number)

del class_members[len(class_members)-1]
len_classmembers=len(class_members)
#print(class_members)
#print(len_classmembers)
m_member_len= len_classmembers
random_choice= []
while len(random_choice) < m_member_len:
    chose_member=random.choice(class_members)
    #print(chose_member)
    index_choice= class_members.index(chose_member)
    del class_members[index_choice]
    random_choice.append(chose_member)
#print(random_choice)
#print(class_members)


timesed_total= random_choice * number_per
#print(timesed_total)

for ordered_number in divisible_number:
    loop_number= max(divisible_number)/ordered_number
    group_number= 1
    while loop_number >0 :
        #print(timesed_total)
        print(f'Group{group_number} Member(s)')
        result_needed=timesed_total[: ordered_number]
        del timesed_total[: ordered_number]
        loop_number = loop_number - 1
        group_number=group_number+1
        #print(timesed_total)
        serial_number=1
        for name_student in result_needed:
            print(f'({serial_number}) {name_student}')
            serial_number=serial_number+1




















