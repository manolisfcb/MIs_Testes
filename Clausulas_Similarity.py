from tkinter import *
from pathlib import Path
from text_preprocessing import *
from text_extract import *
from tkinterdnd2 import DND_FILES, TkinterDnD


def onClick():

    """Colocar chamada a função de procesamento dos textos"""

    # Colocar codigo aqui

    """If numero de clausulas encontradas == numero de clausulas predefinidas é não foram modificadas"""

    #colocar codigo aqui

    top = Toplevel()
    my_label = Label(top, text="verificação de clausulas concluida", font =("Arial", 25, 'bold')).pack()
    my_label2 = Label(top, text = "Não foram encontradas inconsistencias no contrato xpto0097").pack() # colocar nome do contrato analisado.
    top.geometry('600x400')

    """Todas as clausulas estão presente e algumas foram modificadas"""

    #Colocar codigo aqui

    #--------------------------Criação da app----------------------------------------------------------------------------------------



class Application(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()
        self.title("Clausulas Obrigatorias")
        self.main_frame = Frame(self)
        self.main_frame.pack(fill = 'both',expand = 'true')
        self.geometry('900x500')
        self.main_page = MainPage(parent=self.main_frame)

#-----------------------------Criação do ambiente da app-------------------------------------------------------------------------
class MainPage(Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.file_name_listbox = Listbox(parent, selectmode=SINGLE, background='darkgray')
        self.file_name_listbox.place(relheight=1, relwidth=0.25)
        self.file_name_listbox.drop_target_register(DND_FILES)
        self.file_name_listbox.dnd_bind("<<Drop>>", self.drop_inside_list_box)
        self.file_name_listbox.bind("<Double-1>",self._display_file)

        self.button = Button(parent, text = 'Verificar',command = onClick)
        self.button.pack(side=RIGHT, padx=15, pady=20)




    def drop_inside_list_box(self, event):
        pass
        # file_paths = self._parse_drop_file(event.data)
        # current_listbox_items = set(self.file_name_listbox.get(0,"end"))
        # for file_path in file_paths:
        #     if (file_path.endswith(".docx") or file_path.endswith(".DOCX")):
        #         path_object = Path(file_path)
        #         file_name = path_object.name
        #
        #         if file_name not in current_listbox_items:
        #             self.file_name_listbox.insert("end", file_name)
        #             self.path_map[file_name] = file_path


    def _display_file(self,event):
        pass
        # file_name = self.file_name_listbox.get(self.file_name_listbox.curselection())
        # path = self.path_map[file_name]
        # doc = getText(path)
        # text_dict = {}
        # text_dict[path] = [doc]
        #
        # pd.set_option('max_colwidth', 150)
        # docs_df = pd.DataFrame.from_dict(text_dict).transpose()
        # docs_df.columns = ['texto']
        # df = pd.read_pickle('included_selection_df.pkl')
        # self.data_table.set_datatable(dataframe=df)
        # if len(df)==3:
        #     top = tk.Toplevel()
        #     my_label = tk.Label(top, text = "verificação de clausulas concluida").pack()


    def _parse_drop_file(self, filename):
        size = len(filename)
        res = []
        name = ""
        indx = 0

        while indx < size:
            if filename[indx] == "{":
                j = indx+1
                while filename[j] != "}":
                    name+= filename[j]
                    j+=1
                res.append(name)
                name = ""
                indx = j

            elif filename[indx] == " " and name != "":
                res.append(name)
                name = ""

            elif filename[indx] != " ":
                name += filename[indx]
            indx +=1

        if name != "":
            res.append(name)

        return res



    def search_table(self,event):
        # entry = self.search_entrybox.get()
        # if entry == "":
        #     self.data_table.reset_table()
        # else:
        #     entry_split = entry.split(",")
        #     column_value_pairs = {}
        #     for pair in entry_split:
        #         pair_split = pair.split("=")
        #         if len(pair_split) == 2:
        #             col = pair_split[0]
        #             val = pair_split[1]
        #             column_value_pairs[col] = val
        #     self.data_table.find_value(pairs=column_value_pairs)
        pass


if __name__ == '__main__':

    root = Application()

    root.mainloop()