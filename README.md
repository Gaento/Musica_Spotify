
# 🎵 Bot do Spotify com PyAutoGUI

Este é um script Python simples que utiliza a biblioteca `pyautogui` para abrir o Spotify, buscar uma música desejada e controlá-la automaticamente via interface gráfica. Ele também permite ajustar o volume com comandos de teclado.

## 🚀 Funcionalidades

- Abre o Spotify automaticamente.
- Pesquisa e executa uma música informada pelo usuário.
- Permite ao usuário aumentar ou diminuir o volume do sistema.

## 🛠️ Pré-requisitos

- Python 3.x
- Biblioteca `pyautogui` instalada:
  ```bash
  pip install pyautogui
  ```

- Certifique-se de que:
  - O Spotify esteja instalado em seu computador.
  - Sua resolução de tela seja compatível com as coordenadas utilizadas no script (ou ajuste conforme necessário).
  - O sistema esteja em português, pois o script usa atalhos comuns e localizações específicas.

## 📋 Como usar

1. Execute o script no terminal ou editor de sua preferência:
   ```bash
   python spotify_bot.py
   ```

2. Digite o nome da música que deseja ouvir.

3. O script abrirá o Spotify, buscará a música e dará o play.

4. Você será perguntado se deseja ajustar o volume:
   - Pressione `+` para aumentar.
   - Pressione `-` para diminuir.
   - Você pode repetir esse ajuste quantas vezes quiser.

## ⚠️ Avisos

- O script utiliza cliques baseados em coordenadas de tela. Se sua resolução ou layout do Spotify for diferente, você precisará ajustar os valores de `pyautogui.click(x, y)`.
- O tempo de espera (`sleep` e `pyautogui.PAUSE`) pode ser ajustado se notar atrasos ou falhas nas ações.

## 🧠 Exemplo de uso

```bash
Digite a musica que você quer escutar: bohemian rhapsody
Gostaria de aumentar ou abaixar o som? [S/N] s
Digite (+) para aumentar ou (-) para diminuir: +
Gostaria de aumentar mais? [S/N] n
Ok!
```

## 📌 To-Do

- Detecção automática da janela do Spotify.
- Suporte a múltiplas resoluções de tela.
- Interface gráfica para facilitar o uso.

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e compartilhar.

---

Feito com 💻 por Gaento (Gabriel Tolardo)
