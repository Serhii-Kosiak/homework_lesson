import re
# You have a file of unknown length. Write a function that will remove all numbers from each line of the file.


def remove_numbers_for_lines_in_file(file_path: str):
    with open(file_path, 'r') as file:
        text_lines = file.readlines()
        text_without_nums = []
        for line in text_lines:
            text_without_nums.append(re.sub(r'\d+', '', line))

    with open(file_path, 'w') as file2:
        file2.writelines(text_without_nums)


def remove_numbers_for_file(file_path: str):
    with open(file_path, 'r') as file:
        text = file.read()

    with open(file_path, 'w') as file:
        file.write(re.sub(r'\d+', '', text))


if __name__ == '__main__':
    remove_numbers_for_file('./test/text.txt')
