import json
from json import load, dumps


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
        upper_char = name[0].isupper()
        if upper_char == False:
            print("Please capitalize the first letter of the word: ")
            continue
        if is_item_exist(name, list_of_songs) == False:
            break

        print("This song name is taken.")
        show_songs(list_of_songs)

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
        char = writer.replace(' ', '').isalpha()
        if char == False:
            print("Please write characters containing only letters: ")
            continue
        # TODO: check if song writer string contain only letters
        return writer


def get_song_singer():
    while True:
        singer = input("Insert name of singer: ")
        char = singer.isalpha()
        if char == False:
            print("Please write characters containing only letters: ")
            continue
        # TODO: check if song writer string contain only letters
        return singer


def get_song_year():
    while True:
        try:
            year = int(input("Insert year of publish song: "))
            return year
        except Exception as error:
            print(f"print error massage: {error} ")

        # TODO adding try exept block


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


def get_update_song(database, song_name):
    song_data = database[song_name]

    while True:
        read_song(database, song_name)
        item = input("Insert item / action from list [song_writer, song_singer, song_year, exit] : ")

        if item == 'song_writer':
            song_writer = get_song_writer()
            song_data['song_writer'] = song_writer
        elif item == 'song_singer':
            song_singer = get_song_singer()
            song_data['song_singer'] = song_singer
        elif item == 'song_year':
            song_year = get_song_year()
            song_data['song_year'] = song_year
        elif item == 'exit':
            break

    return song_data


def update_database(song_name, song_data, database):
    database[song_name] = song_data
    return database


def add_new_song(database, song_name, song_details):
    database[song_name] = song_details
    return database


def update_song(database, song_name):
    song_writer = get_song_writer()
    song_singer = get_song_singer()
    song_year = get_song_year()
    database[song_name] = {"song_writer": song_writer, "song_singer": song_singer, "song_year": song_year}
    return database


def is_empty(database):
    for key in database.keys():
        return False
    return True


def read_song(database, song_name):
    # {'song_writer': 1, 'song_singer': 2, 'song_year': 3}
    for key, value in database[song_name].items():
        print(f'    {key}: {value}')


def create_file(database):
    with open('database.txt', 'a') as file_handler:
        file_handler.write(f'{database}')


def delete_song(database, song_name):
    del database[song_name]
    return database


def show_songs(songs_list):
    print("Songs list : ")
    for song in songs_list:
        print(f'    {song}')


def get_json_data_from_file(file_name):
    with open(file_name, mode='r') as file_handler:
        data = load(file_handler)

    return data


def convert_dict_to_json(data):
    json_object = json.dumps(data)
    return json_object


def write_to_json_file(file_name, data):
    with open(file_name, 'w') as file_handler:
        json.dump(data, file_handler)


if __name__ == '__main__':
    # write_to_json_file('database.json', {"A": 2, "B": 10})
    song_data = get_new_song({"A": 2, "B": 10})
    print(song_data)

# {"A": {"song_writer": "B", "song_singer": "C", "song_year": 123}}


