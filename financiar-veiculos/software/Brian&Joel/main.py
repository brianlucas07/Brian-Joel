# ----Declara as importações das libs do software----
import base64
from tkinter import *
from tkinter import ttk
import awesometkinter as atk
import mysql.connector
from tkinter import messagebox

# ----Da inicío a janela "root"----
root = Tk()


# ----Início da classe "Application"----
class Application():
    # conexção com o banco de dados
    banco = mysql.connector.connect(host="blsoft-db.cd18ipy4zqlo.us-east-1.rds.amazonaws.com", user="admin",
                                    password="#greenday22", database="mydb")

    cursor = banco.cursor()
    cursor2 = banco.cursor()
    cursor3 = banco.cursor()
    cursor4 = banco.cursor()
    cursor5 = banco.cursor()
    cursor6 = banco.cursor()
    cursor7 = banco.cursor()
    cursor8 = banco.cursor()
    cursor9 = banco.cursor()
    cursor10 = banco.cursor()

    # ----Função __init__ da classe----
    def __init__(self):
        self.root = root
        self.light = "#ebe8e8"
        self.dark = "#262626"
        self.back = f"#738fba"
        self.tela()
        self.widgets()
        self.root.mainloop()

    # ----Função "tela" das propriedades da janela root----
    def tela(self):
        self.root.title("Seja Bem-Vindo")
        self.root.geometry("992x600")
        self.root.configure(bg=f'{self.back}')

        self.root.minsize(675, 550)
        self.root.maxsize(992, 600)

    # ----Função Widgets de conteudo da janela "root"----
    def widgets(self):
        def botao_entrar():
            def botao_cadastro():
                def botao_criar_conta():
                    # inicio do comando do botao_criar_conta #
                    # variaveis para o banco termina com a letra b
                    self.nomeb = self.entry_cadastro_nome.get()
                    self.sobrenomeb = self.entry_cadastro_sobrenome.get()
                    self.cpfb = self.entry_cadastro_cpf.get()
                    self.nascimentob = self.entry_nascimento.get()
                    self.sexob = self.entry_sexo.get()
                    self.scoreb = self.entry_score.get()
                    self.paisb = self.entry_nacionalidade.get()

                    if len(self.cpfb) ==11 :

                        try:
                            self.cursor.execute("insert into CADASTRO values(default, '" + self.nomeb + "','" + self.sobrenomeb + "','" + self.cpfb + "','" + self.nascimentob + "','" + self.sexob + "','" + self.scoreb + "','" + self.paisb + "')")
                            self.cursor.execute("commit")
                        except:
                            messagebox.showerror('CADASTRO', 'Erro ao cadastrar')
                        else:
                            messagebox.showinfo('CADASTRO', 'CADASTRO REALIZADO COM SUCESSO')
                            self.entry_cadastro_nome.delete(0, END)
                            self.entry_cadastro_sobrenome.delete(0, END)
                            self.entry_cadastro_cpf.delete(0, END)
                            self.entry_nascimento.delete(0, END)
                            self.entry_sexo.delete(0, END)
                            self.entry_score.delete(0, END)
                            self.entry_nacionalidade.delete(0, END)


                    else:
                        messagebox.showerror('CPF', 'DIGITE OS 11 DÍGITOS')

                    # print("Agora terá que desenvolver a conexão com as caixas de texto e o banco!!!!") #<----Apage isso depois!----#)

                    # ^^^^ fim do comando do botao_criar_conta ^^^^ #

                # -------comando do botao_cadastro-------#

                def botao_voltar():
                    self.notebook.hide(self.frame_cadastro)
                    botao_entrar()

                self.notebook.hide(self.frame_login)

                self.frame_cadastro = Frame(self.notebook)
                self.frame_cadastro.configure(bg=f'{self.back}')

                self.notebook.add(self.frame_cadastro)

                self.root.minsize(683, 525)

                self.root.title("Cadastre-se")

                self.botao_voltar = atk.Button3d(self.frame_cadastro, text="<--voltar", bg="#b8b8b8",
                                                 command=botao_voltar)
                self.botao_voltar.place(relx=0.01, rely=0.01, relheight=0.07)

                # comando do botao_voltar ----> linha  #

                self.img_cadastro_base64 = "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"

                self.img_cadastro = PhotoImage(data=base64.b64decode(self.img_login_base64))

                self.label_img_cadastro = Label(self.frame_cadastro, image=self.img_cadastro)
                self.label_img_cadastro.place(relx=0.5, rely=0.15, anchor=CENTER)
                self.label_img_cadastro.configure(bg=f"{self.back}")

                self.titulo_cadastro = Label(self.frame_cadastro, font=("arial", 17, "bold"), text="Cadastro")
                self.titulo_cadastro.place(relx=0.5, rely=0.30, anchor=CENTER)
                self.titulo_cadastro.configure(bg=f"{self.back}")

                self.label_cadastro_nome = Label(self.frame_cadastro, font=("arial", 14, "italic"), text="Nome:",
                                                 anchor=W)
                self.label_cadastro_nome.place(relx=0.5, rely=0.40, anchor=CENTER, relwidth=0.35)
                self.label_cadastro_nome.configure(bg=f"white", fg="black")

                self.entry_cadastro_nome = Entry(self.frame_cadastro)
                self.entry_cadastro_nome.place(relx=0.503, rely=0.40, anchor=W, relwidth=0.169)

                self.label_cadastro_sobrenome = Label(self.frame_cadastro, font=("arial", 14, "italic"),
                                                      text="Sobrenome:", anchor=W)
                self.label_cadastro_sobrenome.place(relx=0.5, rely=0.47, anchor=CENTER, relwidth=0.35)
                self.label_cadastro_sobrenome.configure(bg=f"white", fg="black")

                self.entry_cadastro_sobrenome = Entry(self.frame_cadastro)
                self.entry_cadastro_sobrenome.place(relx=0.503, rely=0.47, anchor=W, relwidth=0.169)

                self.label_cadastro_cpf = Label(self.frame_cadastro, font=("arial", 14, "italic"), text="CPF:",
                                                anchor=W)
                self.label_cadastro_cpf.place(relx=0.5, rely=0.54, anchor=CENTER, relwidth=0.35)
                self.label_cadastro_cpf.configure(bg=f"white", fg="black")

                self.entry_cadastro_cpf = Entry(self.frame_cadastro)
                self.entry_cadastro_cpf.place(relx=0.503, rely=0.54, anchor=W, relwidth=0.169)

                self.label_cadastro_nascimento = Label(self.frame_cadastro, font=("arial", 14, "italic"),
                                                       text="Nascimento:",
                                                       anchor=W)
                self.label_cadastro_nascimento.place(relx=0.5, rely=0.61, anchor=CENTER, relwidth=0.35)
                self.label_cadastro_nascimento.configure(bg=f"white", fg="black")

                self.entry_nascimento = Entry(self.frame_cadastro)
                self.entry_nascimento.place(relx=0.503, rely=0.61, anchor=W, relwidth=0.169)

                self.label_cadastro_sexo = Label(self.frame_cadastro, font=("arial", 14, "italic"),
                                                 text="Sexo:",
                                                 anchor=W)
                self.label_cadastro_sexo.place(relx=0.5, rely=0.68, anchor=CENTER, relwidth=0.35)
                self.label_cadastro_sexo.configure(bg=f"white", fg="black")

                self.entry_sexo = Entry(self.frame_cadastro)
                self.entry_sexo.place(relx=0.503, rely=0.68, anchor=W, relwidth=0.169)

                self.label_cadastro_score = Label(self.frame_cadastro, font=("arial", 14, "italic"),
                                                  text="Score:",
                                                  anchor=W)
                self.label_cadastro_score.place(relx=0.5, rely=0.75, anchor=CENTER, relwidth=0.35)
                self.label_cadastro_score.configure(bg=f"white", fg="black")

                self.entry_score = Entry(self.frame_cadastro)
                self.entry_score.place(relx=0.503, rely=0.75, anchor=W, relwidth=0.169)

                self.label_cadastro_nacionalidade = Label(self.frame_cadastro, font=("arial", 14, "italic"),
                                                          text="Nacionalidade:",
                                                          anchor=W)
                self.label_cadastro_nacionalidade.place(relx=0.5, rely=0.82, anchor=CENTER, relwidth=0.35)
                self.label_cadastro_nacionalidade.configure(bg=f"white", fg="black")

                self.entry_nacionalidade = Entry(self.frame_cadastro)
                self.entry_nacionalidade.place(relx=0.503, rely=0.82, anchor=W, relwidth=0.169)

                self.botao_logar = atk.Button3d(self.frame_cadastro, text="Cadastrar", bg="#b8b8b8",
                                                command=botao_criar_conta)
                self.botao_logar.place(relx=0.5, rely=0.90, anchor=CENTER, relwidth=0.35, relheight=0.07)

                # comando botao_criar_conta ----> linha 36 <----#

                # ^^^^ comando do botao_cadastro acima ^^^^

            def consultar():
                # inicio do comando do botao_logar #

                # colocar o resultado da entry para a variável
                self.login_cpf = self.entry_login_cpf.get()
                # consultar no banco de dados
                self.consulta = f"select cpf from CADASTRO where cpf = '{self.login_cpf}'"
                self.cursor3.execute(self.consulta)
                self.result = self.cursor3.fetchall()
                # validar apenas se digitar 11 dígitos
                if len(self.login_cpf) != 11:
                    messagebox.showinfo('CPF', 'PRECISA TER 11 DIGITOS')


                else:
                    # so vai consultar se tiver um cpf válido
                    if len(self.result) != 0:
                        messagebox.showinfo('AVISO SOBRE USUÁRIO', 'Ciente cadastrado!')

                        self.cursor2.execute(
                            f"select * from CADASTRO where cpf = '{self.login_cpf}'")
                        self.dados = (self.cursor2.fetchall())

                        self.mostrar_dados = Tk()
                        self.mostrar_dados.title("DADOS DO CLIENTE")
                        self.mostrar_dados.geometry("500x250")
                        self.mostrar_dados.maxsize(1600, 250)

                        self.mostrar_dados.minsize(750, 250)

                        self.tv = ttk.Treeview(self.mostrar_dados, columns=(
                            'Id', 'Nome', 'Sobrenome', 'CPF', 'Data', 'Sexo', 'Score', 'País'),
                                               show='headings')
                        self.tv.column('Id', minwidth=25, width=75)
                        self.tv.column('Nome', minwidth=25, width=75)
                        self.tv.column('Sobrenome', minwidth=25, width=75)
                        self.tv.column('CPF', minwidth=25, width=75)
                        self.tv.column('Data', minwidth=25, width=75)
                        self.tv.column('Sexo', minwidth=25, width=75)
                        self.tv.column('Score', minwidth=25, width=75)
                        self.tv.column('País', minwidth=25, width=75)


                        self.tv.heading('Id', text='Id')
                        self.tv.heading('Nome', text='Nome')
                        self.tv.heading('Sobrenome', text='Sobrenome')
                        self.tv.heading('CPF', text='CPF')
                        self.tv.heading('Data', text='Data')
                        self.tv.heading('Sexo', text='Sexo')
                        self.tv.heading('Score', text='Score')
                        self.tv.heading('País', text='País')
                        self.tv.place(relx=0, rely=0, relwidth=1, relheight=1)

                        for i in self.dados:
                            self.tv.insert("", "end", values=i)

                        self.consulta2 = (
                            f"select CADASTRO.nome, compra.valor from CADASTRO join compra on CADASTRO.id = compra.idcliente where cpf = {self.login_cpf}")
                        self.cursor5.execute(self.consulta2)
                        self.result2 = self.cursor5.fetchall()
                        if len(self.result2) != 0:
                            messagebox.showinfo('USUÁRIO', 'JA COMPROU VEÍCULO')
                            self.cursor9.execute(f" select CADASTRO.nome,CADASTRO.sobrenome,CARROS.fabricante, CARROS.modelo, CARROS.ano_veiculo,compra.valor,compra.data from CADASTRO join compra on compra.idcliente = CADASTRO.id join CARROS on CARROS.idcarros = compra.idveiculo where cpf = {self.login_cpf}")
                            self.res = (self.cursor9.fetchall())

                            self.objeto_show = {'nome':f'{self.res[0][0]}', 'sobrenome':f'{self.res[0][1]}','fabricante':f'{self.res[0][2]}','modelo':f'{self.res[0][3]}', 'ano':f'{self.res[0][4]}','valor':f'{self.res[0][5]}','data':f'{self.res[0][6]}'}

                            messagebox.showinfo('DADOS DA COMPRA', f"Nome: {self.objeto_show['nome']}\n"
                                                                   f"Sobrenome: {self.objeto_show['sobrenome']}\n"
                                                                   f"Fabricante: {self.objeto_show['fabricante']}\n"
                                                                   f"Modelo: {self.objeto_show['modelo']}\n"
                                                                   f"Ano: {self.objeto_show['ano']}\n"
                                                                   f"Valor: {self.objeto_show['valor']}\n"
                                                                   f"Data: {self.objeto_show['data']}\n")



                        else:
                            self.consulta4 = (f"select score from CADASTRO where cpf = {self.login_cpf}")
                            self.cursor7.execute(self.consulta4)
                            self.result4 = self.cursor7.fetchall()
                            self.objeto = {'Score':f'{self.result4[0][0]}'}
                            messagebox.showwarning('opa', f"Score:{self.objeto['Score']}")

                            self.consulta3 = (f"select * from CARROS where relacao between 0 and {self.result4[0][0]}")
                            self.cursor6.execute(self.consulta3)
                            self.result3 = self.cursor6.fetchall()

                            messagebox.showwarning('VEICULOS LIBERADOS PARA ESTE CPF', f'{self.result3}')

                        self.mostrar_dados.mainloop()
                    # se nao for cliente vai aparecer uma mensagem box
                    else:
                        messagebox.showinfo('AVISO SOBRE USUÁRIO', 'NÃO É UM CLIENTE')



                # fim do comando do botao_logar #

            def compra():
                def botao_registrar():
                    self.data_compra= int(self.entry_data.get())
                    self.valor_compra= int(self.entry_valor.get())
                    self.idcliente= int(self.entry_idcliente.get())
                    self.idveiculo= int(self.entry_idveiculo.get())

                    self.cursor8.execute(f"insert into compra values (default, {self.data_compra}, {self.valor_compra},{self.idcliente},{self.idveiculo})")
                    self.cursor8.execute("commit")
                def botao_voltar2():
                    self.notebook.hide(self.frame_compra)
                    botao_entrar()
                self.frame_compra = Frame()

                self.notebook.hide(self.frame_login)

                self.notebook.add(self.frame_compra)

                self.root.title("Cadastrar Compras")

                self.frame_compra.configure(bg=f'{self.back}')

                self.img_compra_base64 = "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"

                self.img_compra = PhotoImage(data=base64.b64decode(self.img_compra_base64))

                self.botao_voltar2 = atk.Button3d(self.frame_compra, text="<--voltar", bg="#b8b8b8", command=botao_voltar2)
                self.botao_voltar2.place(relx=0.01, rely=0.01, relheight=0.07)

                self.label_img_compra = Label(self.frame_compra, image=self.img_compra)
                self.label_img_compra.place(relx=0.5, rely=0.20, anchor=CENTER)
                self.label_img_compra.configure(bg=f"{self.back}")

                self.titulo_compra = Label(self.frame_compra, font=("arial", 17, "bold"), text="REGISTRAR COMPRA")
                self.titulo_compra.place(relx=0.5, rely=0.40, anchor=CENTER)
                self.titulo_compra.configure(bg=f"{self.back}")

                self.label_idcliente = Label(self.frame_compra, font=("arial", 12, "bold"), text='IDCliente', anchor=W)
                self.label_idcliente.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.35)
                self.label_idcliente.configure(bg="white")

                self.entry_idcliente = Entry(self.frame_compra)
                self.entry_idcliente.place(relx=0.503, rely=0.50, anchor=W, relwidth=0.169)

                self.label_idveiculo = Label(self.frame_compra, font=("arial", 12, "bold"), text='IDVeiculo', anchor=W)
                self.label_idveiculo.place(relx=0.5, rely=0.60, anchor=CENTER, relwidth=0.35)
                self.label_idveiculo.configure(bg="white")

                self.entry_idveiculo = Entry(self.frame_compra)
                self.entry_idveiculo.place(relx=0.503, rely=0.60, anchor=W, relwidth=0.169)

                self.label_data = Label(self.frame_compra, font=("arial", 12, "bold"), text='Data', anchor=W)
                self.label_data.place(relx=0.5, rely=0.70, anchor=CENTER, relwidth=0.35)
                self.label_data.configure(bg="white")

                self.entry_data = Entry(self.frame_compra)
                self.entry_data.place(relx=0.503, rely=0.70, anchor=W, relwidth=0.169)

                self.label_valor = Label(self.frame_compra, font=("arial", 12, "bold"), text='Valor', anchor=W)
                self.label_valor.place(relx=0.5, rely=0.80, anchor=CENTER, relwidth=0.35)
                self.label_valor.configure(bg="white")

                self.entry_valor = Entry(self.frame_compra)
                self.entry_valor.place(relx=0.503, rely=0.80, anchor=W, relwidth=0.169)

                self.botao_registrar = atk.Button3d(self.frame_compra, text="REGISTRAR", bg="#b8b8b8", command=botao_registrar)
                self.botao_registrar.place(relx=0.5, rely=0.90, anchor= CENTER, relwidth=0.35)


            self.notebook.hide(self.frame_root)

            self.frame_login = Frame(self.notebook)
            self.frame_login.configure(bg=f'{self.back}')

            self.notebook.add(self.frame_login)

            self.root.minsize(450, 500)

            self.root.title("Conta")
            self.img_login_base64 = "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"

            self.img_login = PhotoImage(data=base64.b64decode(self.img_login_base64))

            self.label_img_login = Label(self.frame_login, image=self.img_login)
            self.label_img_login.place(relx=0.5, rely=0.20, anchor=CENTER)
            self.label_img_login.configure(bg=f"{self.back}")

            self.titulo_login = Label(self.frame_login, font=("arial", 17, "bold"), text="ÁREA DO CLIENTE")
            self.titulo_login.place(relx=0.5, rely=0.40, anchor=CENTER)
            self.titulo_login.configure(bg=f"{self.back}")

            self.label_login_cpf = Label(self.frame_login, font=("arial", 14, "italic"), text="CPF:", anchor=W)
            self.label_login_cpf.place(relx=0.5, rely=0.50, anchor=CENTER, relwidth=0.35)
            self.label_login_cpf.configure(bg=f"white", fg="black")

            self.entry_login_cpf = Entry(self.frame_login)
            self.entry_login_cpf.place(relx=0.503, rely=0.50, anchor=W, relwidth=0.169)

            # -------criaçao do botao_logar-------#
            self.botao_logar = atk.Button3d(self.frame_login, text="Consutar", bg="#b8b8b8", command=consultar)
            self.botao_logar.place(relx=0.5, rely=0.60, anchor=CENTER, relwidth=0.35, relheight=0.07)
            # ------- comando botao_logar ----> linha 87 <----#

            self.label_ou = Label(self.frame_login, text="Ou")
            self.label_ou.place(relx=0.5, rely=0.67, anchor=CENTER)
            self.label_ou.configure(bg=f"{self.back}")

            # -------criaçao botao_cadastro-------#

            self.botao_cadastro = atk.Button3d(self.frame_login, text="Cadastrar", bg="#b8b8b8", command=botao_cadastro)
            self.botao_cadastro.place(relx=0.5, rely=0.73, anchor=CENTER, relwidth=0.35, relheight=0.07)

            # -------VEÍCULOS-------#

            self.botao_veiculos = atk.Button3d(self.frame_login, text="VEÍCULOS", bg="#b8b8b8", command=veiculos)
            self.botao_veiculos.place(relx=0.5, rely=0.83, anchor=CENTER, relwidth=0.35, relheight=0.07)

            #----------Registrar compras----------#

            self.botao_comprar = atk.Button3d(self.frame_login, text="Registrar Compra", bg="#b8b8b8", command=compra)
            self.botao_comprar.place(relx=0.5, rely=0.93, anchor=CENTER, relwidth=0.35, relheight=0.07)

            # -------comando botao_cadastro----> linha 35 -------#

        self.notebook = ttk.Notebook(self.root)
        self.notebook.place(relx=-0.001, rely=-0.041, relwidth=1.005, relheight=1.041)

        self.frame_root = Frame(self.notebook)
        self.frame_root.configure(bg=f'{self.back}')

        self.frame_superior = Frame(self.frame_root)
        self.frame_superior.place(relx=0, rely=0, relwidth=1, relheight=0.05)
        self.frame_superior.configure(bg=f'#b5b1b1')

        self.titulo_superior = Label(self.frame_superior, font=("Helvetica", 13, "bold"), fg="#241616", bg="#b5b1b1",
                                     text="Financie veículos")
        self.titulo_superior.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.notebook.add(self.frame_root)

        self.base64_veiculo = "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"

        self.img_veiculo = PhotoImage(data=base64.b64decode(self.base64_veiculo))

        self.titulo = Label(self.frame_root, font=("Helvetica", 16, "bold"), text="Faça o Financiamento do carro")
        self.titulo.place(relx=0.5, rely=0.25, anchor=CENTER)
        self.titulo.configure(bg=f'{self.back}')

        self.foto_veiculo = Label(self.frame_root, image=self.img_veiculo)
        self.foto_veiculo.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.foto_veiculo.configure(bg=f'{self.back}')

        self.paragrafo = Label(self.frame_root, font=("arial", 10, "italic"),
                               text="Com base no score, vamos encontrar o melhor carro.")
        self.paragrafo.place(relx=0.5, rely=0.75, anchor=CENTER)
        self.paragrafo.configure(bg=f'{self.back}')
        
        

        # -------criando botao começar-------

        self.botao_começar = atk.Button3d(self.frame_root, text="Entrar", bg="#1f1f1f", command=botao_entrar)
        self.botao_começar.place(relx=0.893, rely=0.92, relwidth=0.10, relheight=0.07)

        # -------comando botao_entrar---->linha 34


        def veiculos():
            self.cursor4.execute("select CARROS.fabricante, CARROS.modelo, CARROS.ano_veiculo from CARROS")
            self.dados4 = (self.cursor4.fetchall())
            self.carros4 = Tk()
            self.carros4.title("CARROS DISPONÍVEIS")
            self.carros4.geometry("500x500")
            self.carros4.maxsize(1600, 250)
            self.carros4.minsize(750, 250)

            self.tvc = ttk.Treeview(self.carros4, columns=('Fabricante', 'Modelo', 'Ano'), show='headings')
            self.tvc.column('Fabricante', minwidth=25, width=75)
            self.tvc.column('Modelo', minwidth=25, width=75)
            self.tvc.column('Ano', minwidth=25, width=75)

            self.tvc.heading('Fabricante', text='Fabricante')
            self.tvc.heading('Modelo', text='Modelo')
            self.tvc.heading('Ano', text='Ano')
            self.tvc.place(relx=0, rely=0, relwidth=1, relheight=1)

            for i in self.dados4:
                self.tvc.insert("", "end", values=i)
            self.carros4.mainloop()


Application()