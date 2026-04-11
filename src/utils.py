import os

def clear_screen():
    """Limpa a tela do terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_choice(prompt, valid_options):
    """Obtém uma escolha válida do usuário."""
    while True:
        choice = input(prompt).strip()
        if choice in valid_options:
            return choice
        print("Opção inválida. Tente novamente.")