# Hitochi (ひとち) – Seu vigilante fofo de autocuidado

![GitHub Actions](https://github.com/ArthurElias997/Hitotchi/actions/workflows/ci.yml/badge.svg)
![Versão](https://img.shields.io/badge/version-1.0.0-blue)
![Licença](https://img.shields.io/badge/license-MIT-green)

**Autor:** Arthur Elias de Oliveira Feitosa de Souza  
**Repositório:** [https://github.com/ArthurElias997/Hitotchi](https://github.com/ArthurElias997/Hitotchi)

---

## O problema real

Muitas pessoas, especialmente aquelas com rotinas intensas ou dificuldade de organização, esquecem de realizar pequenas ações essenciais para o bem-estar físico e mental, como:

- Beber água regularmente ao longo do dia.
- Concluir tarefas simples e pessoais (estudar, alongar, tomar remédio, etc.).

Esse esquecimento afeta a saúde, a produtividade e a qualidade de vida, gerando cansaço, desidratação leve e sensação de improdutividade.

## A solução

**Hitochi** é um aplicativo de autocuidado com interface gráfica (GUI) que ajuda o usuário a:

- Manter uma lista de tarefas diárias (to-do list).
- Controlar a ingestão de água com meta personalizável.
- Receber reforços positivos e mensagens motivacionais de personagens amigáveis.

O nome vem do japonês: **hito** (pessoa) + **chi** (vigia) – um “vigia de pessoa” que cuida de você, ao contrário de um Tamagotchi onde você cuida do bichinho.

## Público-alvo

- Pessoas com dificuldade em manter hábitos básicos de autocuidado.
- Estudantes, profissionais ou cuidadores que esquecem de beber água ou organizar tarefas.
- Usuários que apreciam uma experiência leve, fofa e motivacional.

## Funcionalidades principais

### 💧 Controle de água
- Meta diária configurável (padrão: 2000ml).
- Registro de quantidade ingerida (ex: 200ml).
- Exibição do progresso em ml e porcentagem.
- Mensagem de parabéns ao atingir a meta.

### 📝 Lista de tarefas
- Adicionar nova tarefa.
- Marcar tarefa como concluída.
- Remover tarefa da lista.
- Visualização clara do status (pendente/concluído).

### 🐾 Personagens motivacionais
Três personagens interativos que incentivam o usuário:

| Personagem | Personalidade | Exemplo de mensagem |
|------------|---------------|----------------------|
| **Kukorou** | Ansioso, preocupado, carinhoso | “Ufa! Você bebeu água. Eu estava muito preocupado!” |
| **Feretchi** | Energético, infantil, brincalhão | “Glub glub! Água te dá mais energia para pular!” |
| **Kumafu** | Calma, preguiçosa, possessiva | “Água é aceitável. Continue bebendo.” |

As mensagens mudam conforme a ação: `idle`, `water`, `task_done` ou `goal_reached`.

## Tecnologias utilizadas

- **Python 3.13**
- **Tkinter** – Interface gráfica (biblioteca padrão)
- **unittest** – Testes automatizados
- **Ruff** – Linting e análise estática
- **GitHub Actions** – Integração contínua (CI)
- **Git** – Controle de versão

## Instruções de Execução

# 1. Clone o repositório
git clone https://github.com/ArthurElias997/Hitotchi.git
cd Hitotchi

# 2. (Opcional) Crie um ambiente virtual
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

# 3. Instale as dependências (apenas ruff para lint, não necessário para execução)
pip install -r requirements.txt

# 4. Execute a aplicação
python src/main.py