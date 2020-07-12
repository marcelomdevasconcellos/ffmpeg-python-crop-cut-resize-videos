import os


def open_file(filename):
    import codecs
    file = codecs.open(filename, "r", "utf-8")
    text = file.read()
    file.close()
    return text


command = """
ffmpeg
 -i %(filename_input)s
 -ss %(time_initial)s 
 -t %(time_final)s  
 -async 1 
 -filter:v "crop=%(width)s:%(height)s:%(x)s:%(y)s" 
 temp.mp4
""".replace('\n', '')


command_rezise = """
ffmpeg
 -i temp.mp4
 -vf scale=768:432
 %(file_output)s
""".replace('\n', '')


data = open_file('data.txt')
data_list = data.split('\n')
del data_list[0]
for d in data_list:
    a = d.split('|')
    data_dict = {
        'filename_input': a[0],
        'file_output': a[1],
        'time_initial': a[2],
        'time_final': a[3],
        'width': a[4],
        'height': a[5],
        'x': a[6],
        'y': a[7],
    }
    if not os.path.exists(data_dict['file_output']):
        os.system(command % data_dict)
        os.system(command_rezise % data_dict)
        os.system('rm temp.mp4')
