# === src/main.py ===
import tkinter as tk
from tkinter import messagebox
import os
import todo
import water
import requests
from characters import CHARACTERS, get_character_message

class HitochiApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ひとち - Hitochi | Seu vigilante de autocuidado")
        self.root.geometry("800x550")
        self.root.configure(padx=20, pady=20)

        self.current_char = "Kukorou"
        self.photo_images = {} # Cache para evitar que o Python apague a imagem da memória

        self.build_ui()
        self.update_display("idle")

    def build_ui(self):
        # --- PAINEL ESQUERDO (Ações: Água e Tarefas) ---
        left_frame = tk.Frame(self.root)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Seção de Água
        tk.Label(left_frame, text="💧 Controle de Água", font=("Arial", 14, "bold")).pack(anchor=tk.W, pady=(0, 10))
        self.water_status_lbl = tk.Label(left_frame, text="", font=("Arial", 12))
        self.water_status_lbl.pack(anchor=tk.W)

        water_controls = tk.Frame(left_frame)
        water_controls.pack(anchor=tk.W, pady=5)
        self.water_entry = tk.Entry(water_controls, width=10)
        self.water_entry.pack(side=tk.LEFT, padx=(0, 5))
        tk.Button(water_controls, text="+ Beber (ml)", command=self.drink_water).pack(side=tk.LEFT)

        # Seção de Tarefas
        tk.Label(left_frame, text="📝 Lista de Tarefas", font=("Arial", 14, "bold")).pack(anchor=tk.W, pady=(20, 10))
        
        task_controls = tk.Frame(left_frame)
        task_controls.pack(anchor=tk.W, pady=5)
        self.task_entry = tk.Entry(task_controls, width=30)
        self.task_entry.pack(side=tk.LEFT, padx=(0, 5))
        tk.Button(task_controls, text="Adicionar", command=self.add_task).pack(side=tk.LEFT)

        self.task_listbox = tk.Listbox(left_frame, width=50, height=10)
        self.task_listbox.pack(anchor=tk.W, pady=5)

        task_actions = tk.Frame(left_frame)
        task_actions.pack(anchor=tk.W)
        tk.Button(task_actions, text="✔ Concluir Selecionada", command=self.complete_task).pack(side=tk.LEFT, padx=(0, 5))
        tk.Button(task_actions, text="❌ Remover Selecionada", command=self.remove_task).pack(side=tk.LEFT)

        # --- PAINEL DIREITO (Personagem) ---
        right_frame = tk.Frame(self.root)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Seletor de Personagem (No topo da direita)
        tk.Label(right_frame, text="Seu Vigia:", font=("Arial", 12)).pack(anchor=tk.NE)
        self.char_var = tk.StringVar(value=self.current_char)
        char_menu = tk.OptionMenu(right_frame, self.char_var, *CHARACTERS.keys(), command=self.change_character)
        char_menu.pack(anchor=tk.NE, pady=(0, 20))

        # Imagem e Balão de Fala (No canto inferior direito)
        # Usamos tk.SE (South-East) para ancorar no canto inferior direito
        self.char_image_lbl = tk.Label(right_frame)
        self.char_image_lbl.pack(side=tk.BOTTOM, anchor=tk.SE, pady=(10, 0))

        self.speech_bubble = tk.Label(right_frame, text="", font=("Arial", 11, "italic"), 
                                      bg="#5706ed", relief="solid", borderwidth=1, padx=10, pady=10, wraplength=250)
        self.speech_bubble.pack(side=tk.BOTTOM, anchor=tk.SE, pady=(0, 10))

    def update_display(self, action="idle"):
        """Atualiza os textos e a imagem do personagem na tela."""
        # Atualiza texto da água
        self.water_status_lbl.config(text=water.get_water_status())

        # Atualiza lista de tarefas
        self.task_listbox.delete(0, tk.END)
        for item in todo.list_todos():
            if item != "Nenhuma tarefa pendente. Você está livre!":
                self.task_listbox.insert(tk.END, item)
            else:
                self.task_listbox.insert(tk.END, item)

        # Atualiza a fala do personagem
        msg = get_character_message(self.current_char, action)
        # === ENTRADA DA API ===
        # Se for o Feretchi e a ação for registrar água, busca o fato na internet
        if self.current_char == "Feretchi" and action == "water":
            fato_externo = self.buscar_fato_animal()
            msg = f"{msg}\n\n💡 Curiosidade do Feretchi: {fato_externo}"
        # ======================
        self.speech_bubble.config(text=f"{self.current_char} diz:\n\"{msg}\"")

        # Atualiza a imagem do personagem (Lida com o PNG)
        img_path = CHARACTERS[self.current_char]["image"]
        try:
            # Carrega a imagem só se ela existir
            if os.path.exists(img_path):
                if img_path not in self.photo_images:
                    # 1. Carrega a imagem original grandona
                    img_original = tk.PhotoImage(file=img_path)
                    # 2. Encolhe ela (Aqui estou usando 4, mas você pode mudar para 6, 8, etc.)
                    self.photo_images[img_path] = img_original.subsample(8, 8)
                
                # 3. Coloca a imagem reduzida na tela
                self.char_image_lbl.config(image=self.photo_images[img_path], text="")
            else:
                self.char_image_lbl.config(image='', text=f"[Imagem {self.current_char} não encontrada]", fg="red")
        except Exception as e:
            self.char_image_lbl.config(image='', text=f"[Erro ao carregar PNG: {e}]", fg="red")

    # --- FUNÇÕES DE AÇÃO DOS BOTÕES ---

    def drink_water(self):
        try:
            amount = int(self.water_entry.get())
            water.add_water(amount)
            self.water_entry.delete(0, tk.END)
            
            curr, goal = water.get_progress()
            action = "goal_reached" if curr >= goal else "water"
            self.update_display(action)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, digite um número válido para a água.")

    def add_task(self):
        task = self.task_entry.get()
        try:
            todo.add_todo(task)
            self.task_entry.delete(0, tk.END)
            self.update_display("idle")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))

    def complete_task(self):
        selection = self.task_listbox.curselection()
        if not selection:
            messagebox.showwarning("Aviso", "Selecione uma tarefa para concluir.")
            return
        
        # Ignora se for a mensagem de "Nenhuma tarefa"
        if "Nenhuma tarefa" in self.task_listbox.get(selection[0]):
            return

        try:
            todo.mark_done(selection[0])
            self.update_display("task_done")
        except IndexError:
            messagebox.showerror("Erro", "Erro ao concluir tarefa.")

    def remove_task(self):
        selection = self.task_listbox.curselection()
        if not selection:
            messagebox.showwarning("Aviso", "Selecione uma tarefa para remover.")
            return
            
        if "Nenhuma tarefa" in self.task_listbox.get(selection[0]):
            return

        try:
            todo.remove_todo(selection[0])
            self.update_display("idle")
        except IndexError:
            messagebox.showerror("Erro", "Erro ao remover tarefa.")

    def change_character(self, new_char):
        self.current_char = new_char
        self.update_display("idle")

    def buscar_fato_animal(self):
            try:
                # Faz o pedido para a internet
                resposta = requests.get("https://catfact.ninja/fact", timeout=5)

                # Se a internet e a API estiverem ok (código 200)
                if resposta.status_code == 200:
                    dados = resposta.json()
                    return dados['fact'] # Pega só o texto da curiosidade
                else:
                    return "Sabia que beber água melhora o foco e a energia?"
            except:
                # Se o usuário estiver sem internet, o app não trava
                return "Sabia que beber água melhora o foco e a energia?"

if __name__ == "__main__":
    root = tk.Tk()
    app = HitochiApp(root)
    root.mainloop()