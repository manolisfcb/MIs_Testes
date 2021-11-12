from text_preprocessing import *



folder = input('Enter files dir')
if len(folder)==0:
    folder_dir =r'debentures_data/'
else:
    folder_dir = folder

text_preprocessing(folder_dir)