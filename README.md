# Hitochi (ひとち) – Seu vigilante fofo de autocuidado

## Versão
1.0.0

## Autor
Arthur Elias de Oliveira Feitosa de Souza

## Link do repositório
[URL do GitHub aqui]

---

## O problema real

Muitas pessoas esquecem de cuidar de si mesmas durante a rotina corrida. Pequenas ações como beber água regularmente ou completar tarefas simples do dia a dia são deixadas de lado. Isso afeta a saúde, a produtividade e o bem-estar geral.

## A solução

Hitochi é um aplicativo de autocuidado com interface de linha de comando (CLI) que ajuda o usuário a:

- Manter uma lista de tarefas simples (to-do)
- Controlar a ingestão diária de água
- Receber mensagens motivacionais de personagens fofos

O nome vem do japonês: **hito** (pessoa) + **chi** (watch) – um "relógio de pessoa" que observa e cuida de você, ao contrário de um Tamagotchi onde você cuida do bichinho.

## Público-alvo

Pessoas que têm dificuldade em manter hábitos básicos de autocuidado, que esquecem de beber água ou de completar tarefas diárias, e que apreciam uma experiência leve, fofa e motivacional.

## Funcionalidades principais

### Lista de tarefas (to-do)
- Adicionar um novo item
- Marcar um item como concluído
- Listar todos os itens (pendentes e concluídos)
- Remover um item

### Controle de água
- Definir meta diária (padrão: 2000ml)
- Registrar quantidade de água ingerida (ex: 200ml)
- Exibir progresso atual (ex: 400ml / 2000ml)
- Mensagem de parabéns ao atingir a meta

### Personagens motivacionais
Três personagens (Mihari-ban-tachi) se alternam no canto da tela:
- **Kukorou** – ansioso, medroso, agitado. Sempre à disposição.
- **Feretchi** – energético, infantil, impulsivo. Transforma tudo em brincadeira.
- **Kumafu** – possessiva, gulosa, calma. Ajuda quando tem tempo.

Cada personagem envia mensagens fofas e motivacionais conforme o usuário realiza tarefas ou bebe água.

## Tecnologias utilizadas

- Python 3.x
- Biblioteca padrão (sem dependências externas)
- Interface: CLI (terminal)
- Armazenamento: em memória (dados são perdidos ao fechar o programa)

## Instalação

1. Clone o repositório:
   ```bash
   git clone [URL do seu repositório]
   cd hitochi
