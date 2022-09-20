# A simple program intended to eliminate the monotony
# of typing out lists.

import sys


def listify():
    possible_mode_inputs = ['auto', 'auto singular', 'numbers',
                            'numbers as strings', 'letters', 'words',
                            'auto singlular', 'help', 'exit',
                            '1', '2', '3', '4', '5', '6',
                            'a', 'as', 'n', 'nas', 'l', 'w', 'h', 'e',
                            '?', 'x'
                            ]

    mode = input(
        '\nModes:\n 1 - Auto\n 2 - Auto Singular\n 3 - Numbers\n 4 - Numbers as strings\n 5 - Letters\n 6 - Words\n\n ? - Help\n X - Exit\n\n -> '
    ).lower()

    while mode not in possible_mode_inputs:
        mode = input(
            '\n🔴 Invalid input. Modes:\n 1 - Auto\n 2 - Auto Singular\n 3 - Numbers\n 4 - Numbers as strings\n 5 - Letters\n 6 - Words\n\n ? - Help\n X - Exit\n\n -> '
        ).lower()

    if (mode == 'x') or (mode == 'exit') or (mode == 'e'):
        sys.exit()

    # Displays the function of every mode.
    elif (mode == '?') or (mode == 'help') or (mode == 'h'):
        print('\n - Auto mode detects numbers and converts them into int values,\n   everything else (words, letters, misc.) is kept as strings.\n')
        print(' - Auto singular mode seperates every single character in the\n   string and determines whether it is an int or a string.\n')
        print(' - Numbers mode converts all numerical inputs into int values.\n   This does not support negative numbers.\n')
        print(' - Numbers as strings mode splits numbers at every space, but\n   keeps them as strings.\n')
        print(' - Letters mode keeps everything as strings, and only appends\n   one letter at a time.\n')
        print(' - Words mode seperates words at every space and keeps them as\n   string values.\n')

        mode = input(
            '\nModes:\n 1 - Auto\n 2 - Auto Singular\n 3 - Numbers\n 4 - Letters\n 5 - Words\n\n X - Exit\n\n -> '
        ).lower()

        while mode not in possible_mode_inputs:
            mode = input(
            '\n🔴 Invalid input. Modes:\n 1 - Auto\n 2 - Auto Singular\n 3 - Numbers\n 4 - Numbers as strings\n 5 - Letters\n 6 - Words\n\n X - Exit\n\n -> '
            ).lower()

    # Auto mode detects numbers and converts them into int values,
    # everything else (words, letters, misc.) is kept as strings.
    if (mode == '1') or (mode == 'auto') or (mode == 'a'):
        print('\n➡️ You\'ve entered \'auto\' mode.')
        input_string = input(
            '   Listify (seperate entries with spaces):\n     -> ')
        # Used to check if the string is letters or numbers
        stripped = input_string.replace(' ', '')

        if stripped.isdigit():
            # String is all numbers
            _list = input_string.split()
            listified = []

            for num in _list:
                listified.append(int(num))

            print()
            print(listified)

        elif stripped.isalpha():
            # String is all letters
            listified = input_string.split()

            print()
            print(f'🟢 Your list: {listified}')

        else:
            # Everything else
            _list = input_string.split()
            listified = []

            for i in _list:
                if i.isdigit():
                    listified.append(int(i))
                else:
                    listified.append(i)

            print()
            print(f'🟢 Your list: {listified}')

    # Auto singular mode seperates every single character
    # in the string and determines whether it is an int
    # or a string.
    elif (mode == '2') or (mode == 'auto singluar') or (mode == 'as'):
        print('\n➡️ You\'ve entered \'auto singular\' mode.')
        input_string = input('   Listify:\n     -> ')

        # Used to check if the char is a letter or number
        stripped = input_string.replace(' ', '')
        listified = []

        for i in stripped:
            if i.isdigit():
                listified.append(int(i))
            else:
                listified.append(i)

        print()
        print(f'🟢 Your list: {listified}')

    # Numbers mode converts all numerical inputs into
    # int values.
    elif (mode == '3') or (mode == 'numbers') or (mode == 'n'):
        print('\n➡️ You\'ve entered \'numbers\' mode.')
        input_string = input(
            '   Listify (seperate entries with spaces):\n     -> ')

        stripped = input_string.replace(' ', '')
        while not stripped.isdigit():
            print('\n🔴 Invaild entry. This mode allows for the entry of numbers only.')
            input_string = input(
                '   Listify (seperate entries with spaces):\n     -> ')
            stripped = input_string.replace(' ', '')

        _list = input_string.split()
        listified = []

        for num in _list:
            listified.append(int(num))

        print()
        print(f'🟢 Your list: {listified}')

    elif (mode == '4') or (mode == 'numbers as strings') or (mode == 'nas'):
        print('\n➡️ You\'ve entered \'numbers as strings\' mode.')
        input_string = input(
            '   Listify (seperate entries with spaces):\n     -> ')

        stripped = input_string.replace(' ', '')
        while not stripped.isdigit():
            print('\n🔴 Invaild entry. This mode allows for the entry of numbers only.')
            input_string = input(
                '   Listify (seperate entries with spaces):\n     -> ')
            stripped = input_string.replace(' ', '')

        _list = input_string.split()
        listified = []

        for num in _list:
            listified.append((num))

        print()
        print(f'🟢 Your list: {listified}')

    # Letters mode keeps everything as strings, and only
    # appends one letter at a time.
    elif (mode == '5') or (mode == 'letters') or (mode == 'l'):
        print('\n➡️ You\'ve entered \'letters\' mode.')
        input_string = input('   Listify:\n     -> ')

        stripped = input_string.replace(' ', '')
        while not stripped.isalpha():
            print('\n🔴 Invaild entry. This mode allows for the entry of letters only.')
            input_string = input('   Listify:\n     -> ')
            stripped = input_string.replace(' ', '')

        listified = []

        for letter in stripped:
            listified.append(letter)

        print()
        print(f'🟢 Your list: {listified}')

    # Words mode seperates words at every space and keeps
    # them as string values.
    elif (mode == '6') or (mode == 'words') or (mode == 'w'):
        print('\n➡️ You\'ve entered \'words\' mode.')
        input_string = input(
            '   Listify (seperate entries with spaces):\n     -> ')

        stripped = input_string.replace(' ', '')
        while not stripped.isalpha():
            print(
                '\n🔴 Invaild entry. This mode allows for the entry of words or letters only.')
            input_string = input(
                '   Listify (seperate entries with spaces):\n     -> ')

        listified = input_string.split()

        print()
        print(f'🟢 Your list: {listified}')


if __name__ == '__main__':
    listify()
