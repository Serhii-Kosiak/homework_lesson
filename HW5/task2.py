import pickle

if __name__ == '__main__':
    with open('./test/data/user.txt', 'rb') as file:
        result_in_bytes = file.read()
        my_list = pickle.loads(result_in_bytes)

        # var 1
        # for row in my_list:
        #     result = None
        #
        #     if row[2] == 1:
        #         result = row[0] + row[1]
        #     elif row[2] == 2:
        #         result = row[0] - row[1]
        #     else:
        #         result = row[0] * row[1]
        #
        #     print(result)

        # var 2
        for row in my_list:
            action_dict = {
                '1': row[0] + row[1],
                '2': row[0] - row[1],
                '3': row[0] * row[1],
            }
            result = action_dict[str(row[2])]

            print(result)
