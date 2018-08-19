CREDENTIALS_FILE_PATH = 'credentials.txt'
NOTES_FILE_PATH = 'notes.txt'
def are_credentials_correct(login, password):
    credentials = open(CREDENTIALS_FILE_PATH)
    success = False
    for line in credentials:
        if len(line.replace(' ', '').replace('\n', '')) == 0:
            continue
        login_from_file, password_from_file = line.replace('\n', '').split(' ')
        if login == login_from_file and password == password_from_file:
            success = True
            break
    credentials.close()
    return success


def sign_up():
    global login
    login = read_user_data('login: ', 'Invalid symbols are used: ')
    password = read_user_data('password: ', 'Invalid symbols are used: ')

    file = open(CREDENTIALS_FILE_PATH, 'a')
    file.write('{} {}\n'.format(login, password))
    file.close()
    print('Your credentials are saved.')
    user_choice_func()


def read_user_data(input_message, repeat_message, invalid_input=' '):
    data = str(input(input_message))
    while invalid_input in data:
        data = str(input(repeat_message))
    return data


def sign_in():
    global login
    login = str(input('Login: '))
    password = str(input("Password: "))
    if are_credentials_correct(login, password):
        print('Access granted')
        user_choice_func()
    else:
        print('Access denied')
        input('\nPress enter to exit')


def main():
    user_choice = str(input('Sign up[1]/sign in[2]? '))
    if user_choice == '1':
        sign_up()
    elif user_choice == '2':
        sign_in()
    else:
        input('Invalid input')


def user_choice_func():
    user_choice_func = str(input('New note[1]/Delete all notes[2]?/All notes[3]/Exit[4] '))
    if user_choice_func == '1':
        note()
    elif user_choice_func == '2':
        delete()
    elif user_choice_func == '3':
        all_notes()
    elif user_choice_func == '4':
        input('\nPress enter to exit')
    else:
        input('Invalid input')



def note():
    file = open(NOTES_FILE_PATH, 'a')
    file.write('\n')
    file.write(str(input('New note: ')))
    file.write('\nby ')
    file.write(login)
    file.close()
    input('\nYour note is saved\nPress enter to exit')


def delete():
    file = open(NOTES_FILE_PATH, 'w')
    file.write('')
    file.close
    input('\nAll notes are deleted now\nPress enter to exit')


def all_notes():
    file = open(NOTES_FILE_PATH, 'r')
    notes = file.read()
    file.close
    print(notes)
    input('\nPress enter to exit')


main()
