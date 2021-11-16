from utils import *

def similarity(df):
    docs_df = df
     # seleciona duas cláusulas obrigatórias hipotéticas
    clause0 = docs_df['paragrafos'].iloc[0][4]
    clause1 = docs_df['paragrafos'].iloc[0][18]
    clauses = [clause0, clause1]


    text_index = 0 # define o índice do texto
    text = docs_df['paragrafos'].iloc[text_index] # pega o texto do índice definido

    # calcula a matriz de similaridade por diff das cláusulas em cada parágrafo do texto definido
    similarity_array = similarities(clauses, text)
    np.set_printoptions(linewidth=150, edgeitems=5)

    # mostra quais cláusulas estão presentes no texto com similaridade acima do corte
    cut = 0.8
    included = included_clauses(similarity_array)

    # mostra quantas cláusulas estão presentes no texto
    print(sum(included))

    # cria dataframe cláusulas incluídas
    included_df = pd.DataFrame({'paragrafos': text, 'incluidas_diff': included})

    # salva dataframe das cláusulas incluídas arquivo pickle
    included_df.to_pickle('included_df.pkl')

    included_selection_df = included_df[included_df['incluidas_diff'] == True]
    print(included_selection_df)
    


    # salva dataframe da seleção das cláusulas incluídas em arquivo pickle
    included_selection_df.to_pickle('included_selection_df.pkl')

    return included_selection_df