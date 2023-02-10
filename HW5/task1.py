import os
import pickle
import random


os.makedirs('test/data')

if __name__ == '__main__':
    # write as string
    # with open('./test/data/user.txt', 'a') as file:
    #     my_list = [(random.randint(1, 100), random.randint(1, 100), random.randint(1, 3)) for i in range(100)]
    #     print(my_list)
    #     for row in my_list:
    #         file.write(f'{str(row)}\n')

    # write as bytes
    with open('./test/data/user.txt', 'w+b') as file:
        my_list = [(random.randint(1, 100), random.randint(1, 100), random.randint(1, 3)) for i in range(100)]
        my_list_bytes = pickle.dumps(my_list)
        file.write(my_list_bytes)
