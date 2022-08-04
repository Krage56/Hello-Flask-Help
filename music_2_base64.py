import base64
import json
import os


def m_2_b64(path):
    encode_string = base64.b64encode(open(path, "rb").read())
    return encode_string


def json_music_generator(root, filename, key):
    path = root + "/" + filename
    b_data = m_2_b64(path)
    b_data = b_data.decode('ascii')
    f = open(f"./convert_test_json/{filename}.json", "w")
    json.dump({key: b_data}, f)
    f.close()


def get_dir_files():
    root = "./music"
    playlist = os.listdir(root)
    for track in playlist:
        if track[-4] != ".":
            json_music_generator(root, track, "flac")
        else:
            json_music_generator(root, track, track[-3:len(track)])

get_dir_files()

