from youtube_client import YoutubeClient


def main():
    #get playlists from our youtube
    youtube_client=YoutubeClient('./creds/client_id.json')
    playlists=youtube_client.get_playlist()

    #ask which playlist we want the music video from, make it more interactive
    for index,playlist in enumerate(playlists):
        print(f"{index}:{playlist:title}")
    choice =int(input("Enter your choice: "))


if __name__=='__main__':
    main()