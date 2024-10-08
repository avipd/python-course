from helper import show_welcome_message, get_action,\
    get_songs_list, get_exist_song_name, is_empty, get_update_song,\
    get_new_song, add_new_song, update_database, read_song, delete_song,\
    show_songs, successful_update_message, get_json_data_from_file, convert_dict_to_json, write_to_json_file


def main():
    database = get_json_data_from_file('database.json')

    while True:
        show_welcome_message()
        action = get_action(['Create', 'Read', 'Update', 'Delete', 'Exit'])

        if action == "Create":
            print("In create mode")
            name_of_song, details_of_song = get_new_song(database)
            database = add_new_song(database, name_of_song, details_of_song)
            write_to_json_file('database.json', database)

        elif action == "Read" and is_empty(database) is False:
            print("In read mode")
            list_of_songs = get_songs_list(database)
            show_songs(list_of_songs)
            song_name = get_exist_song_name(list_of_songs)
            read_song(database, song_name)

        elif action == "Update" and is_empty(database) is False:
            print(f"In update mode")
            list_of_songs = get_songs_list(database)
            show_songs(list_of_songs)
            song_name = get_exist_song_name(list_of_songs)
            song_data = get_update_song(database, song_name)
            data_updated = update_database(song_name, song_data, database)
            write_to_json_file("database.json", data_updated)
            print(f"database = {database}")

        elif action == "Delete" and is_empty(database) is False:
            print("In Delete mode")
            list_of_songs = get_songs_list(database)
            show_songs(list_of_songs)
            song_name = get_exist_song_name(list_of_songs)
            database = delete_song(database, song_name)
            write_to_json_file("database.json", database)
            successful_update_message()
            print(f'database = {database}')

        elif is_empty(database) is True:
            print("database is empty please try Create mode")
            continue

        else:
            print("Exit from system")
            break


if __name__ == '__main__':
    main()

# TODO:
#   Integrate update function to json database
#   Add uppercase to the first letter in each song data
#   Add error handling
#   check if song writer string contain only letters
#   Add to git & gitHub

