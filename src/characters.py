# === src/characters.py ===

CHARACTERS = {
    "Kukorou": {
        "image": "../assets/kukorou.png",
        "messages": {
            "idle": "Estou aqui! Squeak! Precisa de algo?",
            "water": "Ufa! Você bebeu água. Eu estava muito preocupado!",
            "task_done": "Você conseguiu! Squeak! Que alívio.",
            "goal_reached": "A meta de água foi atingida! Squeak! Squeak!"
        }
    },
    "Feretchi": {
        "image": "../assets/feretchi.png",
        "messages": {
            "idle": "Vamos brincar! O que tem para fazer hoje?",
            "water": "Glub glub! Água te dá mais energia para pular!",
            "task_done": "Ebaaa! Tarefa destruída! Qual o próximo jogo?",
            "goal_reached": "Você bebeu tudo! Uhuuul! Super poderes!"
        }
    },
    "Kumafu": {
        "image": "../assets/kumafu.png",
        "messages": {
            "idle": "*Bocejo*... estou aqui. Mas não toque no meu mel.",
            "water": "Água é aceitável. Continue bebendo.",
            "task_done": "Bom trabalho. Agora descanse. Vou tirar uma soneca.",
            "goal_reached": "Você atingiu a meta. Estou impressionada."
        }
    }
}

def get_character_message(name, action="idle"):
    """Retorna a mensagem do personagem para a ação específica."""
    char = CHARACTERS.get(name, CHARACTERS["Kukorou"])
    return char["messages"].get(action, char["messages"]["idle"])