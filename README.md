## Port Scanner
Um scanner de portas simples e visualmente agradável desenvolvido em Python com uma interface gráfica usando Tkinter. Este aplicativo permite escanear um intervalo de portas em um host específico e exibe o progresso do escaneamento em tempo real.

#### Funcionalidades
Escaneamento de portas: Especifique um host e um intervalo de portas para escanear.
Progresso em tempo real: Visualize o progresso do escaneamento através de uma barra de progresso.
Identificação de serviços conhecidos: Exibe o nome dos serviços mais comuns quando portas específicas são encontradas abertas.
Interface gráfica: Um design moderno e minimalista usando Tkinter.
Pré-requisitos
Para executar este projeto, você precisará do Python 3 instalado em seu sistema. Se ainda não o tem, pode baixá-lo e instalá-lo a partir do site oficial do Python.

#### Instalação
Clone o repositório:

`
git clone https://github.com/fernandovs4/roteiro1.git
Navegue até o diretório do projeto:

```
cd port-scanner
```
Instale as dependências (opcional):

O Tkinter já vem pré-instalado com o Python na maioria dos sistemas operacionais. No entanto, se você encontrar problemas ao executá-lo, instale-o manualmente:

Para Ubuntu/Debian:

```
sudo apt-get install python3-tk
```
Para macOS: Tkinter já deve estar disponível. Caso contrário, você pode precisar instalar o Python via Homebrew:
```
brew install python-tk
```
Para Windows: Tkinter já está incluído na instalação padrão do Python.

Uso
Execute o script:

Navegue até o diretório do projeto e execute o seguinte comando:

```
python3 port_scanner.py
```
Isso abrirá a interface gráfica do Port Scanner.

Escaneie as portas:

Insira o endereço do host (por exemplo, 127.0.0.1 para localhost).
Especifique a porta inicial e a porta final que deseja escanear.
Clique no botão "Scan" para iniciar o escaneamento.
Veja os resultados:

As portas abertas serão listadas na área de texto.
A barra de progresso mostrará o avanço do escaneamento.


