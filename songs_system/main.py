from helper import show_welcome_message, get_action,\
    get_songs_list,get_exist_song_name, is_empty,\
    get_new_song, add_new_song, update_song, read_song, delete_song


def main():
    songs_data = {'A':  {"song_writer": 1, "song_singer": 2, "song_year": 3}}

    while True:
        show_welcome_message()
        action = get_action(['Create', 'Read', 'Update', 'Delete', 'Exit'])

        if action == "Create":
            print("In create mode")
            name_of_song, details_of_song = get_new_song(songs_data)
            songs_data = add_new_song(songs_data, name_of_song, details_of_song)

        elif action == "Read" and is_empty(songs_data) is True:
            print("In read mode")
            list_of_songs = get_songs_list(songs_data)
            print(f"list_of_songs: {list_of_songs}")
            song_name = get_exist_song_name(list_of_songs)
            read_song(songs_data, song_name)

        elif action == "Update":
            # TODO: If songs_data empty : block update
            # TODO: add option of update specific filed of song :
            #   region update song data
                    # item = input("Insert item / action from list [song_name, song_writer, song_singer, song_year, exit] : ")
                    # if item == 'song_name':
                    #     items_list[song_name] = ''
                    # elif item == 'song_writer':
                    #     items_list[name]['song_writer'] = ''
                    # elif item == 'song_singer':
                    #     items_list[name]['song_singer'] = ''
                    # elif item == 'song_year':
                    #     items_list[name]['song_year'] = ''
                    # elif item == 'exit':
                    #     break
                    # endregion update song data

            print(f"In update mode")
            list_of_songs = get_songs_list(songs_data)
            song_name_data = get_exist_song_name(list_of_songs)
            songs_data = update_song(songs_data, song_name_data)
            print(f"songs_data = {songs_data}")

        elif action == "Delete":
            # TODO: If songs_data empty : block Delete
            print("In Delete mode")
            list_of_songs = get_songs_list(songs_data)
            song_name = get_exist_song_name(list_of_songs)
            songs_data = delete_song(songs_data, song_name)
            print(f'songs_data = {songs_data}')

        else:
            print("Exit from system")
            break


if __name__ == '__main__':
    main()

# TODO:
#  create the main dict
#  show welcome massage to user
#  get action from user
#  check if action is one of options [Create, Read, Update, Delete] - CRUD

#  if action is Create:
#       get name of new song!
#       get name of writer
#       get name of singer
#       get year of publish
#       update in dict {name of song: {"writer": coldplay, "singer" : coldplay, "year" : 2010}}

#  if action is Read:
#       show list of songs
#       get name of song
#       show details on song
#       show successful message

#  if action is Update:
#       show list of song
#       get name of song
#       show details of song
#       get action from user
#       check if action is one of options [name, singer, write, year]
#       update main dict
#       show successful message

#  if action is Delete:
#       show list of song
#       get name of song
#       show details of song
#       delete song and update main dict
#       show successful message
