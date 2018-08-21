CREDENTIALS_FILE_PATH = 'credentials.txt'
NOTES_FILE_PATH = 'notes.txt'
login = str()

def is_user_regestered(login, password):
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
    login = read_user_data('login: ', 'Invalid symbols are used: ')
    password = read_user_data('password: ', 'Invalid symbols are used: ')
    
    file = open(CREDENTIALS_FILE_PATH, 'a')
    file.write('{} {}\n'.format(login, password))
    file.close()
    return login


def read_user_data(input_message, repeat_message, invalid_input=' '):
    data = str(input(input_message))
    while invalid_input in data:
        data = str(input(repeat_message))
    return data


def sign_in():
    login = str(input('Login: '))
    password = str(input("Password: "))
    if is_user_regestered(login, password):
        return login
    else:
        return None


def main():
    login = None
    while login == None:
        user_choice = str(input('Sign up[1]/sign in[2]? '))
        if user_choice == '1':
            login = sign_up()
        elif user_choice == '2':
            login = sign_in()

    user_choice_func(login)


def user_choice_func(login):
    user_choice_func = str(input('New note[1]/Delete all notes[2]?/All notes[3]/Exit[4] '))
    if user_choice_func == '1':
        note(login)
    elif user_choice_func == '2':
        delete(login)
    elif user_choice_func == '3':
        all_notes(login)
    elif user_choice_func == '4':
        input('\nPress enter to exit')
    else:
        input('Invalid input')



def note(login):
    file = open(NOTES_FILE_PATH, 'a')
    file.write('\n')
    new_note = str(input('New note: '))
    file.write(new_note)
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


if __name__ == '__main__':
    main()
