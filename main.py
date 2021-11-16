from text_preprocessing import *
from clausules_similarity import *


''' Colocar o caminho dos arquivos, pressione Enter para selecionar o diretório padrão ('debentures_data/')  '''

folder = input('Enter files path: ')

if len(folder)==0:
    folder_dir =r'debentures_data/'
else:
    folder_dir = folder
print("'" + folder_dir + "'")




'''realizar o pré-processamento de todos os documentos no diretório selecionado
   devolve um dataframe com: path | texto | texto limpo | texto separado por paragrafos | tokens | datas '''

df = text_preprocessing(folder_dir)





''' Procure por cláusulas obrigatórias '''
clausulas = similarity(df)
