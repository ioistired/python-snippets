from gmusicapi.clients import Mobileclient
import urllib.request
import taglib
import os
import argparse
import sys

def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits .
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")

def downResource(sr):
    print('Downloading ' + sr['title'])
    albumartist = sr['albumArtist'].replace('/','')
    artist = sr['artist'].replace('/','')
    title = sr['title'].replace('/','')
    album = sr['album'].replace('/','')
    try:
        tracknum = str(sr['trackNumber'])
    except Exception:
        pass
        tracknum = str(0)
    if not os.path.exists('download/' + albumartist):
        os.mkdir('download/' + albumartist, 493)
    if not os.path.exists('download/' + albumartist + '/' + album):
        os.mkdir('download/' + albumartist + '/' + album, 493)
    if len(tracknum) == 1:
        paddedtracknum = '0' + tracknum
    else:
        paddedtracknum = tracknum
    fname = 'download/' + albumartist + '/' + album + '/' + paddedtracknum + ' ' + artist + ' - ' + title + '.mp3'
    if os.path.exists(fname):
        print('Already downloaded')
        return
    try:
        durl = mc.get_stream_url(sr['storeId'])
    except Exception:
        pass
        print('error downloading')
        return
    urllib.request.urlretrieve(durl, fname)
    print('Downloaded ' + fname)
    song = taglib.File(fname)
    song.tags['TITLE'] = [sr['title']]
    song.tags['ARTIST'] = [sr['artist']]
    song.tags['ALBUM'] = [sr['album']]
    try:
        tracknum = str(sr['trackNumber'])
        song.tags['TRACKNUMBER'] = [tracknum]
    except Exception:
        pass
    try:
        song.tags['GENRE'] = [sr['genre']]
    except Exception:
        pass
        print('ERROR SETTING GENRE')
    try:
        song.tags['DATE'] = [str(sr['year'])]
    except Exception:
        pass
        print('ERROR SETTING DATE')
    song.save()
    song.close()
    print('Tagged ' + fname)

def downSong(search):
    sr = mc.search(search)
    if len(sr['song_hits']) == 0:
        print('no songs found for ' + search)
        return
    downResource(sr['song_hits'][0]['track'])

def downAlbum(search):
    sr = mc.search(search)
    if len(sr['album_hits']) == 0:
        print('no albums found for ' + search)
        return
    album = mc.get_album_info(sr['album_hits'][0]['album']['albumId'])
    query_yes_no('Download album ' + album['name'] + ' by ' + album['artist'] + '?')
    for track in album['tracks']:
        downResource(track)

parser = argparse.ArgumentParser(description='GPM Download Tool')
parser.add_argument('search', type=str, help='search term')
parser.add_argument('-a', '--album', dest='album', action='store_true', help='treat the search term as an album')
args = parser.parse_args()

mc = Mobileclient()
# username, password, deviceid
mc.login('aa', 'aa', 'aa')
print('Logged in')

if args.album:
    downAlbum(args.search)
else:
    downSong(args.search)
