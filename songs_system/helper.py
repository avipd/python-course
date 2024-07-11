def show_welcome_message():
    print('Welcome to the songs system')


def is_item_exist(item, items_list):
    return item in items_list


def get_action(list_of_actions):
    while True:
        user_action = input(f'Select from options {list_of_actions} : ')
        if is_item_exist(user_action, list_of_actions) == True:
            break

        print('This option is not valid')

    return user_action


def get_songs_list(songs_data_dict):
    return list(songs_data_dict.keys())


def get_song_name(list_of_songs):
    while True:
        name = input("Insert name of song : ")
        if is_item_exist(name, list_of_songs) == False:
            break

        print("This option is not valid")

    return name


def get_exist_song_name(list_of_songs):
    while True:
        name = input("Insert name of song : ")
        if is_item_exist(name, list_of_songs) == True:
            break

        print("This option is not valid please chose Create:")

    return name


def get_song_writer():
    while True:
        writer = input("Insert writer of song: ")
        # TODO: check if song writer string contain only letters
        return writer


def get_song_singer():
    while True:
        singer = input("Insert name of singer: ")
        # TODO: check if song writer string contain only letters
        return singer


def get_song_year():
    while True:
        year = int(input("Insert year of publish song: "))
        # TODO adding try exept block
        return year


def successful_update_message():
    print('Successful update')


def get_new_song(songs_database):
    songs_list = get_songs_list(songs_database)
    song_name = get_song_name(songs_list)
    song_writer = get_song_writer()
    song_singer = get_song_singer()
    song_year = get_song_year()
    song_details = {"song_writer": song_writer, "song_singer": song_singer, "song_year": song_year}
    return song_name, song_details


def add_new_song(database, song_name, song_details):
    database[song_name] = song_details
    return database


def update_song(database, song_name):
    song_writer = get_song_writer()
    song_singer = get_song_singer()
    song_year = get_song_year()
    database[song_name] = {"song_writer": song_writer, "song_singer": song_singer, "song_year": song_year}
    return database


def read_song(database, song_name):
    # {'song_writer': 1, 'song_singer': 2, 'song_year': 3}
    for key, value in database[song_name].items():
        print(f'    {key}: {value}')



def delete_song(database, song_name):
    del database[song_name]
    successful_update_message()
    return database


if __name__ == '__main__':
    action_list = get_action(['Create', 'Read', 'Update', 'Delete', 'Exit'])