from youtube_client import YoutubeClient
from spotify_client import SpotifyClient

# we dont want to hardcode api keys
import os


def main():
    # get playlists from our youtube
    youtube_client = YoutubeClient('./creds/client_id.json')
    spotify_client = SpotifyClient(os.getenv('SPOTIFY_AUTH_TOKEN'))
    playlists = youtube_client.get_playlist()

    # ask which playlist we want the music video from, make it more interactive
    for index, playlist in enumerate(playlists):
        print(f"{index}:{playlist.title}")
    choice = int(input("Enter your choice: "))
    chosen_playlist = playlists[choice]
    print(f"You selected: {chosen_playlist.title}")

    # for each video in the playlist get the song information from youtube
    songs = youtube_client.get_videos_from_playlist(chosen_playlist.id)
    print(f"Attempting to add: {len(songs)}")

    # search for song on spotify
    for song in songs:
        spotify_song_id = spotify_client.search_song(song.artist, song.track)

        # if we find the song, add it to our liked song
        if spotify_song_id:
            added_song = spotify_client.add_song_to_spotify_liked(spotify_song_id)

            # if the song is added then let the user know!
            if added_song:
                print(f"Added {song.artist}")


if __name__ == '__main__':
    main()
