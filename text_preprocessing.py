from utils import *
from os.path import exists
import pandas as pd
import pickle
import numpy as np


def text_preprocessing(fd):
    folder_dir = fd
    # lê nomes dos arquivos da pasta
    files = get_text_name(folder_dir)

    # lê caminhos dos arquivos da pasta
    files_dir = get_text_dir(folder_dir)

    # retorna dicionário com hash e caminho dos documentos lidos
    hashes = [get_hash(file_dir) for file_dir in files_dir]
    hashes_dict = dict(zip(hashes, files_dir))

    # lê, atualiza e salva pickle caso o arquivo já exista ou cria novo arquivo pickle
    if exists('unique_hashes_dict.plk'):
        with (open("unique_hashes_dict.plk", "rb")) as f:
            loaded_dict = pickle.load(f)
            loaded_dict.update(hashes_dict)
            hashes_dict = loaded_dict
        with (open("unique_hashes_dict.plk", "wb")) as f:
            pickle.dump(hashes_dict, f)
    else:
        with (open('unique_hashes_dict.plk', 'wb')) as f:
            pickle.dump(hashes_dict, f)

    # carrega documentos e textos como objetos da biblioteca docx e quebra texto em parágrafos docx e '\n'
    docs, texts, para_texts = para_text_extract(files_dir)

    # extrai número de documentos, tamanho de cada documento e tamanho total dos documentos
    n_docs, docs_len, total_len = text_info(para_texts)

    print('Quantidade de documentos: ' + str(n_docs))
    print('Tamanho de cada documento: ' + str(docs_len))
    print('Tamanho total: ' + str(total_len))

    # extrai datas dos cabeçalhos
    dates = date_extract(docs)

    # extrai documentos inteiros e cria dicionário
    texts_dict = {}
    for i, f in enumerate(files_dir):
        texts_dict[f] = [full_text_extract(f)]

    # cria dataframe de textos
    pd.set_option('max_colwidth', 150)
    docs_df = pd.DataFrame.from_dict(texts_dict).transpose()
    docs_df.columns = ['texto']
    docs_df.sort_index(inplace=True)

    # reseta índice e cria coluna 'documento'
    docs_df.reset_index(inplace=True)
    docs_df = docs_df.rename(columns = {'index': 'documento'})

    # cria coluna 'texto_limpo' e coloca os textos limpos
    docs_df['texto_limpo'] = pd.DataFrame(docs_df['texto'].apply(clean_text_round1))

    # cria coluna 'paragrafos' e coloca textos separados em parágrafos
    docs_df['paragrafos'] = para_texts

    # cria coluna 'tokens' com tokens de palavras minúsculas, alfanuméricas e sem stopwords
    docs_df['tokens'] = pd.DataFrame(docs_df['paragrafos'].apply(tokenize))

    # cria coluna 'data'
    docs_df['data'] = dates

    # transforma o tipo da coluna 'data' em dt.date
    docs_df['data'] = pd.to_datetime(docs_df['data']).dt.date

    # salva dataframe dos documentos em arquivo pickle
    docs_df.to_pickle('docs_df.pkl')

    return docs_df

   
