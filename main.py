from datetime import timedelta 
from pydub import AudioSegment
import os
import math





def get_seconds(time_str):
    time = time_str.split(':')
    if(len(time) == 2):
        return int(time[0]) * 60 + int(time[1])
    else:
        return int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])

def split_audio(input_file, output_folder, data_songs):
    audio = AudioSegment.from_mp3(input_file)
    num_parts = len(data_songs)
 
    for i in range(num_parts):
        start = data_songs[i][0] * 1000
        end = data_songs[i][1] * 1000
        split_audio = audio[start:end]
        output_path = os.path.join(output_folder, f"{data_songs[i][2]}.mp3")
        split_audio.export(output_path, format="mp3")
        print(f"Exported {output_path}")

def get_data(file_name):
    with open(file_name) as f:
        lines = f.read().splitlines() #mejorar conversion
        leng = len(lines)
        data = []
        data_split = []
        for i in range(leng):
            data_split.append(lines[i].split(maxsplit=1))
        for i in range(leng-1):
            aux = []
            aux.append(data_split[i][0])
            aux.append(data_split[i+1][0])
            aux.append(data_split[i][1])
            data.append(aux)
        aux = []
        aux.append(data_split[leng-1][0])
        aux.append('00:00')
        aux.append(data_split[leng-1][1])
        data.append(aux)
        return data
    

def convert_data(list_data):
    for i in range(len(list_data)):
        aux1 = get_seconds(list_data[i][0])
        aux2 = get_seconds(list_data[i][1])
        list_data[i][0] = aux1
        list_data[i][1] = aux2
    return list_data


def split_data(str_data):
     str_data.split()

#AudioSegment.converter = "C:\\Users\\Jhoaho\\Downloads\\ffmpeg\\bin\\ffmpeg.exe"
#AudioSegment.ffmpeg = "C:\\Users\\Jhoaho\\Downloads\\ffmpeg\\bin\\ffmpeg.exe"
#AudioSegment.ffprobe = "C:\\Users\\Jhoaho\\Downloads\\ffmpeg\\bin\\ffprobe.exe"
file_data = "./data/data.txt" #archivo txt
input_file = "./song.mp3" #archivo mp3
output_folder = "./result/" #carpeta
#int, int, string
list_data_unconverted = get_data(file_data)
#print(list_data_unconverted)
#print("Ended 1")
list_data_converted = convert_data(list_data_unconverted)
split_audio(input_file, output_folder, list_data_converted)

#print(list_data_converted)

#print("Ended 2")




