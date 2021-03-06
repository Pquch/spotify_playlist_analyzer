import argparse

import tabulate
from dotenv import load_dotenv

import spotify_helpers as sph

load_dotenv()


def main():
    parser = argparse.ArgumentParser(
        description='Tabulate a Spotify playlists\'s audio features')
    parser.add_argument('playlist_id', type=str, help='Spotify Playlist ID')
    args = parser.parse_args()

    playlist_id = args.playlist_id

    scope = ['playlist-read-private', 'playlist-read-collaborative']
    client = sph.create_spotify_client(scope)
    tracks = sph.get_playlist_tracks(client, playlist_id, 10, 0)
    track_dictionary_list = sph.make_playlist_dictionary(client, tracks)
    print(sph.tabulate_tracks(track_dictionary_list))


if __name__ == "__main__":
    main()
