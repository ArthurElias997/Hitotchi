todos = []

def add_todo(task):
    """Adiciona uma nova tarefa."""
    if not task.strip():
        raise ValueError("A tarefa não pode estar vazia.")
    todos.append({"task": task.strip(), "done": False})

def list_todos():
    """Retorna a lista de tarefas formatada."""
    if not todos:
        return ["Nenhuma tarefa pendente. Você está livre!"]
    
    formatted_list = []
    for i, item in enumerate(todos):
        status = "[x]" if item["done"] else "[ ]"
        formatted_list.append(f"{i + 1}. {status} {item['task']}")
    return formatted_list

def mark_done(index):
    """Marca uma tarefa como concluída pelo índice (0-based)."""
    if index < 0 or index >= len(todos):
        raise IndexError("Índice de tarefa inválido.")
    todos[index]["done"] = True

def remove_todo(index):
    """Remove uma tarefa pelo índice (0-based)."""
    if index < 0 or index >= len(todos):
        raise IndexError("Índice de tarefa inválido.")
    todos.pop(index)

def clear_todos():
    """Limpa todas as tarefas (útil para testes)."""
    todos.clear()