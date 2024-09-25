# 🎶 Python + Arduino Music Control with Hand Detection

Este projeto utiliza **Python**, **Arduino** e uma **biblioteca de machine learning** para tocar música de acordo com a quantidade de dedos detectados pela webcam. O sistema reconhece a quantidade de dedos exibidos na câmera e, com base nisso, aciona diferentes músicas ou sons.

## 📸 Funcionalidade

- O projeto detecta a quantidade de dedos levantados por meio da webcam.
- Com base no número de dedos detectados, um comando é enviado para o Arduino, que então toca uma nota específica e realiza uma ação sonora.
- Utiliza algoritmos de machine learning para reconhecimento de objetos (dedos) em tempo real.

## 🔧 Tecnologias Utilizadas

- **Python**: linguagem principal para a lógica do projeto.
- **OpenCV**: para a captura e processamento de imagens da webcam.
- **Mediapipe** ou **TensorFlow**: para o reconhecimento e contagem dos dedos usando machine learning.
- **Arduino**: microcontrolador que recebe os comandos do Python via porta serial para tocar músicas.
- **Biblioteca PySerial**: para a comunicação entre Python e Arduino.

## 🛠 Instalação e Configuração

1. **Clone o repositório**:
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. **Instale as dependências Python**:
    Certifique-se de ter o Python instalado em seu sistema. Em seguida, execute:
    ```bash
    pip install -r requirements.txt
    ```
    O arquivo `requirements.txt` deve incluir as bibliotecas necessárias, como:
    - `opencv-python`
    - `mediapipe` ou `tensorflow`
    - `pyserial`

3. **Configurar o Arduino**:
    - Faça o upload do código para o seu Arduino usando o **Arduino IDE**.
    - O código Arduino deve estar configurado para receber sinais via serial e tocar a música correspondente à quantidade de dedos detectados.

4. **Rodar o projeto**:
    - Conecte sua webcam.
    - Conecte o Arduino ao seu computador.
    - Execute o script Python principal:
      ```bash
      python main.py
      ```

   5.**Circuito**
   -Conecte um speaker ao arduino com uma protoboard de acordo com a entrada referente ao código.

## 🚀 Funcionalidades Futuras

- Adicionar novos gestos para controlar volume ou mudar as faixas de música.
- Melhorar a precisão do reconhecimento com mais algoritmos de machine learning.
- Implementar suporte para múltiplos instrumentos ou sons.

## 🤝 Contribuições

Sinta-se à vontade para abrir **issues** ou enviar **pull requests** para melhorias e correções.

## 📜 Licença

Este projeto está licenciado sob a licença MIT - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
