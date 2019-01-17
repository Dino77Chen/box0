x = 16

my_list = [i for i in range(x)]
my_gen = (i * i for i in range(x))

print(my_list)

for i in range(x):
    my_list[i] = next(my_gen)
    print(i, my_list[i])

print(my_list)
