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

| Personagem | Personalidade |
|------------|---------------|
| **Kukorou** | Ansioso, preocupado, carinhoso |
| **Feretchi** | Energético, infantil, brincalhão |
| **Kumafu** | Calma, preguiçosa, possessiva |

As interações mudam conforme a ação: `idle`, `water`, `task_done` ou `goal_reached`.

## Tecnologias utilizadas

- **Python 3.13**
- **Tkinter** – Interface gráfica (biblioteca padrão)
- **requests** – Consumo de API HTTP
- **unittest** – Testes automatizados
- **Ruff** – Linting e análise estática
- **GitHub Actions** – Integração contínua (CI)
- **Git** – Controle de versão

---

## Integração com API Pública Aberta
O projeto consome a API pública Cat Facts (https://catfact.ninja/fact) de forma totalmente assíncrona e segura.

**Funcionamento:** Sempre que o usuário registra uma nova ingestão de água, o sistema faz uma requisição HTTP GET para buscar uma curiosidade aleatória sobre felinos.

**Tratamento de Falhas:** O código possui tratamento robusto contra quedas de conexão ou indisponibilidade do servidor (bloco try/except), garantindo que o app nunca trave e exiba uma mensagem amigável de contingência caso o usuário esteja offline.

---

## Testes Automatizados
O projeto possui uma suíte de testes unitários e de integração localizada na pasta /tests.

**Para rodar especificamente o Teste de Integração da API, garanta que seu terminal esteja na pasta raiz do projeto (Hitotchi) e execute:**

python3 -m unittest tests/test_api.py

**Para rodar toda a suíte de testes da aplicação:**

python3 -m unittest discover -s tests

---

## Fluxo de Trabalho (Git / GitHub)
O desenvolvimento desta etapa seguiu estritamente as boas práticas de engenharia de software do BootCamp:

**Branch Dedicada:** Toda a evolução (integração da API e testes) foi codificada na branch regulamentar entrega-intermediaria.

**Rastreabilidade:** O progresso e a resolução do problema foram diretamente atrelados à respectiva Issue aberta no repositório.

**CI/CD:** Integração contínua ativa via GitHub Actions garantindo a validação estática e execução automática de testes a cada push.

---

## 🛠️ Instruções de Instalação e Execução (Deploy Desktop)

Como o **Hitochi** é uma aplicação Desktop com Interface Gráfica (GUI) baseada em Tkinter, a publicação e execução ocorrem diretamente em ambiente local. Siga os passos abaixo:

**1. Clone o repositório**

git clone [https://github.com/ArthurElias997/Hitotchi.git](https://github.com/ArthurElias997/Hitotchi.git)
cd Hitotchi

**2. (Opcional) Crie um ambiente virtual**

python3 -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

**3. Instale as dependências**

pip install requests

**4. Execute o aplicativo**

cd src
python3 main.py