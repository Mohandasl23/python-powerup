# Automação de Cadastro de Produtos

Este projeto é um script de automação em Python que realiza o cadastro automático de produtos em um sistema web. Ele foi desenvolvido utilizando as bibliotecas **PyAutoGUI** (para controle do mouse e teclado) e **Pandas** (para leitura e manipulação da base de dados de produtos).

---

## 🛠️ Tecnologias Utilizadas

*   **Python 3.x**: Linguagem de programação principal.
*   **PyAutoGUI**: Biblioteca para automatizar interações com a tela (cliques, digitação e comandos de teclado).
*   **Pandas**: Biblioteca para análise de dados, utilizada para ler o arquivo `produtos.csv`.
*   **OpenPyXL**: Mecanismo de leitura/escrita para arquivos do Excel (requisito adicional para o Pandas).
*   **Time**: Módulo nativo do Python para gerenciar pausas e esperas durante a execução.

---

## 📋 Passos Executados pelo Script

1.  **Entrar no sistema da empresa:** Abre o navegador Chrome, acessa o link do sistema de cadastro:
    `https://dlp.hashtagtreinamentos.com/python/intensivao/login`
2.  **Fazer login:** Clica no campo de e-mail, preenche as credenciais padrão e submete o formulário.
3.  **Carregar base de dados:** Lê o arquivo [produtos.csv](file:///c:/Users/mohan/Desktop/python%20powerup/produtos.csv) que contém a lista de itens a serem cadastrados.
4.  **Cadastrar os produtos:** Percorre cada linha da tabela de produtos e preenche os seguintes campos no formulário web:
    *   Código do Produto
    *   Marca
    *   Tipo
    *   Categoria
    *   Preço Unitário (formatado automaticamente com prefixo `R$ ` e duas casas decimais separadas por vírgula)
    *   Custo do Produto (formatado automaticamente com prefixo `R$ ` e duas casas decimais separadas por vírgula)
    *   Observações (preenchido apenas se houver uma observação cadastrada na base de dados)
5.  **Repetir o processo:** Envia o formulário, rola a página para cima e repete a operação para o próximo produto até cadastrar toda a lista.

---

## 🚀 Como Configurar e Executar

### 1. Pré-requisitos
Certifique-se de ter o Python instalado em sua máquina. Em seguida, instale as bibliotecas necessárias executando o seguinte comando no seu terminal:

```bash
pip install pyautogui pandas openpyxl
```

### 2. Ajuste das Coordenadas da Tela (Muito Importante ⚠️)
O PyAutoGUI utiliza coordenadas de pixel absolutas na tela para clicar nos botões e campos corretos. Como as coordenadas do script atual estão calibradas para uma resolução específica, **você provavelmente precisará ajustar os valores de `x` e `y`** nos comandos `pyautogui.click()`.

Para descobrir as coordenadas exatas na sua tela:
1. Você pode executar o script auxiliar `AULA 01/pegar_posicao.py` ou abrir o terminal interativo do Python.
2. Posicione o cursor do mouse exatamente sobre o campo que você deseja obter a coordenada. Após 5 segundos, o terminal exibirá a posição.
   ```python
   import pyautogui
   import time
   time.sleep(5)  # Tempo para você posicionar o mouse
   print(pyautogui.position())
   ```
3. Substitua as coordenadas obtidas no arquivo `codigo.py` nos respectivos comandos `pyautogui.click(x=..., y=...)`.

Os principais pontos que necessitam de ajuste são:
*   Linha 27: Clique no campo de e-mail.
*   Linha 35: Clique no botão de enviar login.
*   Linha 48: Clique no primeiro campo do formulário de cadastro.

### 3. Executando o Script
Para iniciar a automação, execute o script com o comando:

```bash
python codigo.py
```

> [!WARNING]
> **Atenção:** Assim que o script começar a rodar, o PyAutoGUI assumirá o controle do mouse e do teclado. Evite mexer no computador até que o processo termine para não interferir na automação. Caso precise parar o script imediatamente em caso de emergência, mova o cursor do mouse rapidamente para qualquer um dos 4 cantos da tela (função Failsafe do PyAutoGUI).

---

## 📂 Estrutura do Projeto

*   `codigo.py`: Script principal contendo o código de automação.
*   `produtos.csv`: Arquivo contendo a base de dados de produtos a serem cadastrados.
*   `README.md`: Documentação de ajuda do projeto.
*   `AULA 01/`: Pasta com os materiais originais de apoio da aula.
    *   `Apostila Jornada Python - Aula 1.pdf`: Material didático em PDF.
    *   `pegar_posicao.py`: Script auxiliar para identificar as coordenadas do mouse na tela.
    *   `gabarito.py`: Código de referência resolvido pela equipe de ensino.

---

## 🎓 Aprendizados e Relato de Experiência

Quero, por meio deste, apresentar meus aprendizados durante o projeto **"Fundações & Seu Primeiro Robô"**.

Consegui concluir com sucesso o projeto de **Automação de Cadastro de Produtos**, e posso dizer que foi uma experiência bastante desafiadora. Embora eu já tivesse desenvolvido anteriormente uma automação utilizando **Playwright**, e soubesse que esse tipo de projeto exige atenção aos detalhes, este desafio trouxe novos obstáculos.

Apesar de parecer um projeto simples à primeira vista, durante o desenvolvimento surgiram diversos bugs que precisei investigar e corrigir. Cada problema solucionado representou uma oportunidade de aprendizado, pois muitas vezes foi necessário revisar, refazer e aprimorar partes do código até encontrar a solução correta.

Acreditei que concluiria o projeto rapidamente por já possuir uma base de conhecimento em automação, mas os desafios encontrados mostraram que sempre há algo novo para aprender. No final, ver o robô funcionando perfeitamente tornou toda a dedicação extremamente gratificante.

Satisfeito com o resultado, resolvi ir além do que havia sido proposto e implementei algumas melhorias no projeto, como a utilização de **f-strings** para tornar o código mais legível e a formatação dos valores monetários com o prefixo **R$**, duas casas decimais e separação decimal por vírgula, deixando a apresentação dos dados mais profissional e amigável ao usuário.

Esse projeto reforçou a importância da persistência, da prática e da busca contínua por soluções, mostrando que cada desafio superado contribui diretamente para o meu crescimento como desenvolvedor.

