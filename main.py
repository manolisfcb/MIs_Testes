from text_preprocessing import *
from clausules_similarity import *
import tkinter as tk
from TkinterDnD2 import *

def drop_indide_listbox(event):
    clause0 = 'TIBAGI ENERGIA SPE S.A., sociedade por ações de capital fechado, com sede na Cidade de Belo Horizonte, Estado de Minas Gerais, na Avenida Getúlio Vargas, nº 874, 10º andar, Sala 1006, inscrita no Cadastro Nacional de Pessoa Jurídica do Ministério da Economia (“CNPJ”) sob o nº 23.080.281/0001-35 e na Junta Comercial do Estado de Minas Gerais (“JUCEMG”) sob o NIRE nº 31.3.00112209, neste ato representada por seu(s) representante(s) legal(is) devidamente autorizado(s) e identificado(s) nas páginas de assinaturas do presente instrumento (“Emissora” ou “Companhia”); e'
    clause1 = 'A presente 1ª (primeira) emissão de debêntures simples, não conversíveis em ações de emissão da Emissora, da espécie com garantia real, com garantia adicional fidejussória, em série única (“Emissão” e “Debêntures”, respectivamente), para distribuição pública com esforços restritos, nos termos da Instrução da Comissão de Valores Mobiliários (“CVM”) nº 476, de 16 de janeiro de 2009, conforme alterada (“Instrução CVM 476”), das demais disposições legais aplicáveis e desta Escritura de Emissão (“Oferta Restrita”), deverá observar os seguintes requisitos:'
    clause2 = 'el perro de mi vecina se llama suky'
    clauses = [clause0, clause1, clause2]
    clauses

    listb.insert("end", event.data)
    folder = event.data
    #

    print (folder)
    df = text_preprocessing(folder)
    included_selection_df = similarity(df)

    print(included_selection_df)

def drop_inside_textbox(event):
    tbox.delete("1.0", "end")
    if event.data.endswith(".txt"):
        with open(event.data, "r") as file:
            for line in file:
                line = line.strip()
                tbox.insert("end", f"{line} \n")





root = TkinterDnD.Tk()
root.geometry("800x500")


listb = tk.Listbox(root, selectmode=tk.SINGLE, background="#ffe0d6")
listb.pack(fill=tk.X)
listb.drop_target_register(DND_FILES)
listb.dnd_bind("<<Drop>>",drop_indide_listbox)
folder = listb.drop_target_register(DND_FILES)



tbox = tk.Text(root)
tbox.pack()
tbox.drop_target_register(DND_FILES)
tbox.dnd_bind("<<Drop>>",drop_inside_textbox)



root.mainloop()
