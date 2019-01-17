def say_hello(number, name):
    # print(str(number) + ' ' + str(name) + ' says "Hello World!"')
    print(number, name + ' says "Hello World!"')


persons_list = []
list_top = 5

for this_number in range(0, list_top):
    # 这种方式是传址，不是想要的效果
    # this_person['number'] = this_person['number'] + 1
    # this_person['name'] = input("What your name ? (input 'q' to exit) ")
    this_person = {'number': this_number+1, 'name': input("What your name ? (input 'q' to exit) ")}

    if this_person['name'] == 'q':
        break
    elif this_person['number'] >= list_top:
        print(" Too many persons !!! \n")

    persons_list.append(this_person)

if persons_list:
    print("\n Hello every one ! Let's say Hi !\n")
    for person in persons_list:
        say_hello(person['number'], person['name'])
else:
    print("\n No one come !!!\n")
