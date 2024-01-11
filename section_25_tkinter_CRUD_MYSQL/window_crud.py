from tkinter import *
from tkinter import ttk, messagebox
from connection_db import ConnectionDB


class WindowCrud(Frame):
    __connection = ConnectionDB()
    __NEW = 0
    __UPDATE = 1

    def __init__(self, master=None):
        super().__init__(master, width=1000, height=400)
        self.master = master
        self.pack()
        self.create_widgets()
        self.list_data()
        self.status_txt()
        self.status_btn_actions("normal")
        self.status_btn_behavior()
        self.action_button_save = self.__NEW

    def list_data(self):
        self.clear_grid()
        data = self.__connection.get_all_customers()
        for element in data:
            self.grid.insert("", END, text=f"{element[0]}", values=(element[1], element[2], element[3], element[4]))

    def clear_grid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)
    def new_customer(self):
        self.status_txt("normal")
        self.status_btn_behavior("normal")
        self.status_btn_actions()
        self.clear_data_txt()
        self.action_button_save = self.__NEW

    def update_customer(self):

        select = self.grid.focus()
        id = self.grid.item(select, "text")
        data = self.grid.item(select, "values")

        if id == "":
            messagebox.showwarning("Update", "You should select valid customer.")
        else:
            self.status_txt("normal")
            self.status_btn_behavior("normal")
            self.status_btn_actions()

            self.txt_code.insert(0, id)
            self.txt_name.insert(0, data[0])
            self.txt_ap_pate.insert(0, data[1])
            self.txt_ap_mate.insert(0, data[2])
            self.txt_cred.insert(0, data[3])

            self.action_button_save = self.__UPDATE



    def delete_customer(self):
        select = self.grid.focus()
        id = self.grid.item(select, "text")
        if id == "":
            messagebox.showwarning("Delete", "You should select valid customer.")
        else:
            response = messagebox.askquestion("Delete", "Do you want to delete this customer?")
            if response == messagebox.YES:
                try:
                    self.__connection.delete_customer(id)
                    messagebox.showinfo("Delete", "Customer deteled successfully.")
                except:
                    messagebox.showinfo("Delete", "Error on delete customer.")
                finally:
                    self.list_data()


    def save_data(self):
        code = self.txt_code.get()
        name = self.txt_name.get()
        last_name_pa = self.txt_ap_pate.get()
        last_name_ma = self.txt_ap_mate.get()
        credits = self.txt_cred.get()

        if self.action_button_save == self.__NEW:
            self.__connection.insert_customer(code, name, last_name_pa, last_name_ma, credits)
            messagebox.showinfo("Saved", "Customer saved successfully.")
        elif self.action_button_save == self.__UPDATE:
            self.__connection.update_customer(code, name, last_name_pa, last_name_ma, credits)
            messagebox.showinfo("Saved", "Customer updated successfully.")

        self.list_data()
        self.clear_data_txt()
        self.status_btn_actions("normal")
        self.status_btn_behavior()
        self.status_txt()
    def cancel(self):
        self.list_data()
        self.clear_data_txt()
        self.status_btn_actions("normal")
        self.status_btn_behavior()
        self.status_txt()

    def create_widgets(self):
        frame1 = Frame(self, bg="#3F99F3")
        frame1.place(x=0, y=0, width=150, height=399)

        # Buttons
        self.btn_new = Button(frame1, text="Crear Cliente", command=self.new_customer, bg="black", fg="white")
        self.btn_new.place(x=15, y=50, width=110, height=40)

        self.btn_update = Button(frame1, text="Modificar Cliente", command=self.update_customer, bg="black", fg="white")
        self.btn_update.place(x=15, y=140, width=110, height=40)

        self.btn_delete = Button(frame1, text="Eliminar Cliente", command=self.delete_customer, bg="black", fg="white")
        self.btn_delete.place(x=15, y=230, width=110, height=40)

        # TextBox
        frame2 = Frame(self, bg="#09436D")
        frame2.place(x=150, y=0, width=230, height=399)

        label1 = Label(frame2, text="Código: ")
        label1.place(x=30, y=30)
        self.txt_code = Entry(frame2)
        self.txt_code.place(x=30, y=58, width=150, height=20)

        label2 = Label(frame2, text="Nombre: ")
        label2.place(x=30, y=90)
        self.txt_name = Entry(frame2)
        self.txt_name.place(x=30, y=118, width=150, height=20)

        label3 = Label(frame2, text="Apellido Paterno: ")
        label3.place(x=30, y=150)
        self.txt_ap_pate = Entry(frame2)
        self.txt_ap_pate.place(x=30, y=178, width=150, height=20)

        label4 = Label(frame2, text="Apellido Materno: ")
        label4.place(x=30, y=210)
        self.txt_ap_mate = Entry(frame2)
        self.txt_ap_mate.place(x=30, y=238, width=150, height=20)

        label5 = Label(frame2, text="Créditos: ")
        label5.place(x=30, y=270)
        self.txt_cred = Entry(frame2)
        self.txt_cred.place(x=30, y=298, width=150, height=20)

        self.btn_save = Button(frame2, text="Guardar", command=self.save_data, bg="#0B4162", fg="white")
        self.btn_save.place(x=20, y=340, width=90, height=40)

        self.btn_cancel = Button(frame2, text="Cancelar", command=self.cancel, bg="#9A0812", fg="white")
        self.btn_cancel.place(x=120, y=340, width=90, height=40)

        # GRID
        frame3 = Frame(self, bg="#ed3913")
        frame3.place(x=380, y=0, width=590, height=390)

        self.grid = ttk.Treeview(self, columns=("col1", "col2", "col3", "col4"))

        self.grid.column("#0", width=40, anchor=CENTER)
        self.grid.column("col1", width=90, anchor=CENTER)
        self.grid.column("col2", width=90, anchor=CENTER)
        self.grid.column("col3", width=90, anchor=CENTER)
        self.grid.column("col4", width=90, anchor=CENTER)

        self.grid.heading("#0", text="Código", anchor=CENTER)
        self.grid.heading("col1", text="Nombre", anchor=CENTER)
        self.grid.heading("col2", text="Apellido Paterno", anchor=CENTER)
        self.grid.heading("col3", text="Apellido Materno", anchor=CENTER)
        self.grid.heading("col4", text="Créditos", anchor=CENTER)

        self.grid.place(x=380, y=0, width=590, height=390)
        self.grid['selectmode'] = "browse"

    def status_txt(self, status="disabled"):
        self.txt_code.configure(state=status)
        self.txt_name.configure(state=status)
        self.txt_ap_pate.configure(state=status)
        self.txt_ap_mate.configure(state=status)
        self.txt_cred.configure(state=status)

    def status_btn_actions(self, status="disabled"):
        self.btn_new.configure(state=status)
        self.btn_update.configure(state=status)
        self.btn_delete.configure(state=status)

    def status_btn_behavior(self, status="disabled"):
        self.btn_save.configure(state=status)
        self.btn_cancel.configure(state=status)

    def clear_data_txt(self):
        self.txt_code.delete(0, END)
        self.txt_name.delete(0, END)
        self.txt_ap_pate.delete(0, END)
        self.txt_ap_mate.delete(0, END)
        self.txt_cred.delete(0, END)
        self.txt_code.focus()
