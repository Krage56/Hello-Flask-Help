import json
import subprocess
import os
from pathlib import Path


def t_convert():
    j_files = os.listdir("../convert_test_json")
    Path("../output_mp3").mkdir(parents=True, exist_ok=True)
    for j_file in j_files:
        subprocess.run([
            'curl',
            '-X',
            "GET",
            "-H",
            "Content-type: application/json",
            "-H",
            "Accept: audio/mpeg",
            "-d",
            f"@../convert_test_json/{j_file}",
            'http://localhost:5000/convert',
            '-o',
            f'../output_mp3/{j_file}.mp3'
        ],
            capture_output=True
        )
    print("Проверьте папку output_mp3")


def t_generate():
    Path("../output_random_json").mkdir(parents=True, exist_ok=True)
    for i in range(0, 5):
        for j in range(0, 6):
            subprocess.run([
                'curl',
                f"http://localhost:5000/generate?level={i}&numkeys={j}",
                '-o',
                f'../output_random_json/lvl={i}, numkeys={j}.json'
            ],
                capture_output=True
            )
    print("Проверьте папку output_random_json")


def t_find():
    arr = [None] * 4
    arr[0] = {
        "America": "Great",
        "England": "Great",
        "Uganda": "Not_Great",
        "Dollar": 55,
        "Euro": "Equal with Dollar"
    }
    arr[1] = {
        "str_num": '10',
        "not_str_num": 10,
    }
    arr[2] = dict()
    arr[3] = []
    Path("../output_find").mkdir(parents=True, exist_ok=True)
    Path("../test_data_find").mkdir(parents=True, exist_ok=True)
    test_cases = [
        [
            "value=Great",
            "value='Not_Great'",
            "value=55"
        ],
        [
            "value='10'",
            "value=10"
        ],
        [
            'value=random_val'
        ],
        [
            'value=random_val'
        ]
    ]
    for i, el in enumerate(arr):
        f = open(f"../test_data_find/{i}.json", "w")
        json.dump(el, f)
        f.close()

    for i, sub_arr in enumerate(test_cases):
        for j, el in enumerate(sub_arr):
            subprocess.run([
                'curl',
                '-X',
                "GET",
                "-H",
                "Content-type: application/json",
                "-H",
                "Accept: application/json",
                "-d",
                f"@../test_data_find/{i}.json",
                f'http://localhost:5000/find?{el}',
                '-o',
                f'../output_find/{i},{j}.json'
            ],
                capture_output=True
            )

    print("Проверьте папку output_find")


def t_keys():
    Path("../test_data_keys").mkdir(parents=True, exist_ok=True)
    arr = [None] * 2
    arr[0] = {
        "America": "Great",
        "England": "Great",
        "Uganda": "Not_Great",
        "Dollar": 55,
        "Euro": [
            "Equal with Dollar",
            55
        ],
        "Africa": {
            "Uganda": 1,
            "CAR": 1,
            "Liberia": 1,
            "SAR": 0
        }
    }
    arr[1] = {
        "str_num": '10',
        "not_str_num": 10,
    }

    for i, el in enumerate(arr):
        f = open(f"../test_data_keys/{i}.json", "w")
        json.dump(el, f)
        f.close()

    Path("../output_keys").mkdir(parents=True, exist_ok=True)
    for i in range(len(arr)):
        subprocess.run([
            'curl',
            '-X',
            "GET",
            "-H",
            "Content-type: application/json",
            "-H",
            "Accept: application/json",
            "-d",
            f"@../test_data_keys/{i}.json",
            f'http://localhost:5000/keys',
            '-o',
            f'../output_keys/{i}.json'
        ],
            capture_output=True
        )
        print(f"{i}: {arr[i].keys()}")

    print("Проверьте папку output_keys")

def main():
    i = int(input(
        '''
        0. Выйти и закрыть программу.
        1. Вызвать проверку для keys с заготовленными параметрами.
        2. Вызвать проверку для find с заранее заготовленными параметрами.
        3. Вызвать проверку для generate с заранее заготовленными параметрами.
        4. Вызвать проверку для convert с заранее заготовленными параметрами.
        '''
    ))
    while i != 0:
        if i == 1:
            t_keys()
        if i == 2:
            t_find()
        if i == 3:
            t_generate()
        if i == 4:
            t_convert()
        i = int(input(
            '''
            0. Выйти и закрыть программу.
            1. Вызвать проверку для keys с заготовленными параметрами.
            2. Вызвать проверку для find с заранее заготовленными параметрами.
            3. Вызвать проверку для generate с заранее заготовленными параметрами.
            4. Вызвать проверку для convert с заранее заготовленными параметрами.
            '''
        ))
main()