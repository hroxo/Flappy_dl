# Flappy Bird RL – Jogo + Deep Learning em Python

Projeto em Python que recria o jogo **Flappy Bird** com duas modalidades:
- 🕹️ **Modo Jogador Humano** – jogas com o teclado.
- 🤖 **Modo IA (Deep RL)** – um agente com rede neural aprende a jogar sozinho.
- 👀 **Treino em tempo real** – opção para veres o agente a treinar “ao vivo”.

O objetivo deste projeto é ser **uma peça forte de portefólio**, combinando:
- Programação de jogos com `pygame`
- Conceitos de **Reinforcement Learning** (DQN)
- Estruturação de código limpa e modular
- Visualização clara da evolução do agente

---

## 🔧 Tecnologias usadas

- **Python 3.10+** (recomendado)
- [Pygame](https://www.pygame.org/)
- [PyTorch](https://pytorch.org/)
- `numpy`

Mais tarde, poderás acrescentar:
- `matplotlib` (para gráficos de evolução de score)
- `tqdm` (barra de progresso no treino)

---

## 📁 Estrutura do projeto

Estrutura sugerida:

```text
flappy-bird-rl/
│
├─ game/
│   ├─ __init__.py
│   ├─ bird.py           # classe Bird (física e desenho)
│   ├─ pipes.py          # classe Pipe(s) e gestão dos obstáculos
│   └─ game_core.py      # lógica do jogo + ambiente RL (FlappyEnv)
│
├─ rl/
│   ├─ __init__.py
│   ├─ dqn_agent.py      # definição da rede neural + agente DQN
│   └─ replay_buffer.py  # memória de experiências (replay buffer)
│
├─ assets/               # imagens, fontes, etc. (opcional)
│
├─ main_human.py         # jogar Flappy Bird como humano
├─ main_train.py         # treinar a IA (DQN) no ambiente
├─ main_watch.py         # ver o agente treinado a jogar
│
├─ requirements.txt
└─ README.md
````

---

## 🚀 Instalação

1. **Clonar o repositório**

```bash
git clone https://github.com/<o-teu-username>/flappy-bird-rl.git
cd flappy-bird-rl
```

2. **Criar e ativar ambiente virtual (opcional, mas recomendado)**

```bash
python -m venv venv

# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

3. **Instalar dependências**

```bash
pip install -r requirements.txt
```

Exemplo de `requirements.txt` (podes ir ajustando):

```text
pygame
torch
numpy
matplotlib
tqdm
```

---

## ✅ Passos para desenvolver o projeto

### 1. Implementar o jogo base (modo humano)

**Objetivo:** ter um Flappy Bird jogável por um humano, sem IA.

Tarefas:

* Criar a janela com `pygame` (por ex. 400x600).
* Implementar a classe `Bird` (`game/bird.py`):

  * posição (x, y)
  * velocidade vertical
  * gravidade
  * método `flap()` que aplica impulso para cima
  * métodos `update()` e `draw(screen)`
* Implementar os `Pipes` (`game/pipes.py`):

  * geração de pares de canos (topo/fundo) com um gap
  * movimento para a esquerda
  * reciclagem quando saem do ecrã
* Implementar lógica de jogo em `game_core.py`:

  * detetar colisões (bird vs pipes, bird vs chão/teto)
  * gerir o score (incrementa quando passas um par de canos)

Criar `main_human.py` para:

* Ler input do teclado (ex.: tecla espaço → `bird.flap()`).
* Atualizar bird e pipes a cada frame.
* Desenhar tudo no ecrã.
* Mostrar score atual.

Quando esta fase estiver feita, tens um jogo Flappy Bird básico.

---

### 2. Transformar o jogo num “ambiente” RL

**Objetivo:** criar uma interface tipo OpenAI Gym para a IA poder interagir.

No ficheiro `game/game_core.py`, criar uma classe:

```python
class FlappyEnv:
    def __init__(self, render: bool = False):
        ...

    def reset(self):
        """
        Reinicia o jogo e devolve o estado inicial.
        """
        return state

    def step(self, action: int):
        """
        Executa uma ação:
          action = 0 -> não faz nada
          action = 1 -> flap
        Avança o jogo um passo (frame) e devolve:
          next_state, reward, done, info
        """
        return next_state, reward, done, info

    def render(self):
        """
        Desenha o estado atual no ecrã (se render estiver ativo).
        """
        ...
```

#### Definir o estado (state)

Sugestão de features:

* `bird_y` – posição vertical do pássaro
* `bird_velocity` – velocidade vertical
* `dist_x` – distância horizontal até ao próximo cano
* `gap_y` – posição vertical do gap do próximo cano
* opcional: `bird_y - gap_y`

O `state` pode ser um `numpy.array` com estes valores (normalizados se necessário).

#### Definir as ações

* `0` = não fazer nada (deixar o pássaro cair por gravidade).
* `1` = flap (aplicar impulso para cima).

#### Recompensa (reward)

Exemplo simples:

* `+0.1` por cada frame vivo.
* `+1` (ou +5) por cada cano passado.
* `-1` no momento em que o pássaro morre (colisão).

---

### 3. Implementar o agente DQN

Na pasta `rl/`:

#### 3.1. Rede neural (PyTorch) – `dqn_agent.py`

* Input: tamanho igual ao número de features do estado.
* 2–3 camadas fully-connected com ReLU.
* Output: 2 valores → Q(s, ação=0) e Q(s, ação=1).

Criar uma classe `DQNAgent` com:

* `select_action(state, epsilon)` – política ε-greedy.
* `optimize_model()` – um passo de treino a partir do replay buffer.
* gestão de duas redes (online e target), se quiseres fazer DQN “clássico”.

#### 3.2. Replay Buffer – `replay_buffer.py`

Classe para guardar experiências:

```python
(state, action, reward, next_state, done)
```

Com métodos:

* `push(...)` – adicionar transição
* `sample(batch_size)` – amostrar batch aleatório

---

### 4. Treinar a IA (`main_train.py`)

**Objetivo:** loop de treino de RL com DQN.

Pseudo-código:

```python
env = FlappyEnv(render=VER_TREINO_AO_VIVO_OU_NAO)
agent = DQNAgent(...)
buffer = ReplayBuffer(...)

for episode in range(num_episodes):
    state = env.reset()
    done = False
    total_reward = 0

    while not done:
        # 1. Escolher ação (ε-greedy)
        action = agent.select_action(state, epsilon)

        # 2. Executar ação no ambiente
        next_state, reward, done, info = env.step(action)

        # 3. Guardar transição no replay buffer
        buffer.push(state, action, reward, next_state, done)

        # 4. Atualizar rede
        agent.optimize_model(buffer)

        state = next_state
        total_reward += reward

        # 5. Render opcional (para ver o treino ao vivo)
        if RENDER_DURING_TRAIN:
            env.render()

    # Atualizar epsilon ao longo dos episódios
    # Guardar melhor modelo com base no score
```

Durante o treino, podes:

* Imprimir no terminal:

  * episódio, score, melhor score
* Mostrar na janela (usando Pygame):

  * episódio atual
  * epsilon
  * score atual
  * best score

---

### 5. Ver o agente treinado (`main_watch.py`)

Neste script:

* Carregar o modelo treinado (ficheiro `.pt` ou `.pth`).
* Criar `FlappyEnv(render=True)`.
* Correr um loop onde a ação é sempre:

  * `argmax(Q(state))` (sem exploração random).
* Não é preciso replay buffer nem treino, apenas **inferência**.

Isto é o “modo espetáculo” para mostrar no portefólio.

---

## 🕹️ Como correr

### Jogar como humano

```bash
python main_human.py
```

### Treinar a IA

```bash
python main_train.py
```

### Ver a IA a jogar (modelo já treinado)

```bash
python main_watch.py
```

---

## 📊 Melhorias futuras / Roadmap

* [ ] Guardar e plotar gráficos de:

  * score por episódio
  * média móvel dos últimos N episódios
* [ ] Suporte a diferentes esquemas de recompensa
* [ ] Ajustar hiperparâmetros (learning rate, γ, tamanho do replay, etc.)
* [ ] Adicionar menu inicial para escolher:

  * jogar humano
  * treinar IA
  * ver IA treinada
* [ ] Otimizações de performance quando o render está desligado (treino mais rápido)

---

## 🎓 Conceitos abordados (para CV/portefólio)

* Programação de jogos com **Pygame**
* Conceitos de física simples (gravidade, velocidade)
* Design de **ambientes RL** (reset/step/state/reward)
* Implementação de **DQN** com PyTorch
* Uso de **Replay Buffer** e política ε-greedy
* Organização modular de projeto em Python
