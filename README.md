🎲 Jogo Senha (Mastermind) em Python
Este é um projeto simples de implementação do clássico jogo de tabuleiro Senha (também conhecido como Mastermind), desenvolvido em Python.

O objetivo do jogo é adivinhar uma senha secreta de 4 cores gerada aleatoriamente pelo computador, dentro de um limite de tentativas.

📋 Regras do Jogo
A Senha: O computador gera uma senha aleatória com 4 cores distintas.

Cores Disponíveis:

🔴 R (Red - Vermelho)

🟢 G (Green - Verde)

🔵 B (Blue - Azul)

🟡 Y (Yellow - Amarelo)

🟠 O (Orange - Laranja)

🟣 P (Purple - Roxo)

Tentativas: Você tem 10 chances para acertar a sequência exata.

Dicas: Após cada tentativa, o jogo fornece um feedback:

Posição Certa: Quantas cores você acertou e estão no lugar correto.

Posição Errada: Quantas cores fazem parte da senha, mas você colocou no lugar errado.



🛠️ Tecnologias Utilizadas
Python 3

Biblioteca random (para geração aleatória da senha)

Manipulação de sets (conjuntos) e listas para lógica de verificação.

🧠 Lógica do Código
O código utiliza algumas funções interessantes do Python:

random.sample: Garante que a senha gerada não tenha cores repetidas.

zip(): Permite iterar simultaneamente sobre a senha secreta e o palpite do jogador para verificar posições exatas.

set(): Utilizado para calcular a interseção de cores entre o palpite e a senha, facilitando a contagem de cores certas na posição errada.

🤝 Contribuição
Sinta-se à vontade para fazer um fork deste projeto e enviar pull requests. Algumas ideias de melhorias:

Adicionar validação para impedir que o usuário digite cores inválidas.

Permitir que o jogador escolha o nível de dificuldade (mais ou menos tentativas).

Criar uma interface gráfica.
