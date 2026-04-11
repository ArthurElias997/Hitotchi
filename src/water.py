water_data = {
    "goal": 2000,
    "current": 0
}

def set_goal(amount):
    """Define a meta diária de água."""
    if amount <= 0:
        raise ValueError("A meta deve ser maior que zero.")
    water_data["goal"] = amount

def add_water(amount):
    """Adiciona a quantidade de água ingerida."""
    if amount <= 0:
        raise ValueError("A quantidade deve ser positiva.")
    water_data["current"] += amount

def get_progress():
    """Retorna a quantidade atual e a meta."""
    return water_data["current"], water_data["goal"]

def get_water_status():
    """Retorna uma string formatada com o progresso da água."""
    current, goal = get_progress()
    percentage = min(100, int((current / goal) * 100))
    return f"Progresso da Água: {current}ml / {goal}ml ({percentage}%)"

def reset_water():
    """Zera o consumo (útil para testes)."""
    water_data["current"] = 0
    water_data["goal"] = 2000