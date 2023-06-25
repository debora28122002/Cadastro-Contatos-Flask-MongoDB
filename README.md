# Cadastro de Contatos - Flask e MongoDB

Bem-vindo ao Cadastro de Contatos, um aplicativo web desenvolvido utilizando Flask e MongoDB. Com este aplicativo, você pode cadastrar, excluir, editar e visualizar contatos, armazenando informações como nome, sobrenome, telefone e e-mail.

## Funcionalidades

- **Cadastro de Contatos:** Adicione novos contatos informando nome, sobrenome, telefone e e-mail.
- **Visualização de Contatos:** Veja a lista completa de contatos cadastrados.
- **Edição de Contatos:** Atualize as informações dos contatos existentes.
- **Exclusão de Contatos:** Remova contatos da lista.

## Tecnologias Utilizadas

- Python
- Flask
- MongoDB
- HTML
- CSS

## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes pré-requisitos instalados:

- Python (versão 3.6 ou superior)
- MongoDB (devidamente configurado e em execução)

## Como Executar o Projeto

1. Clone o repositório:
   ```
   git clone https://github.com/debora28122002/Cadastro-Contatos-Flask-MongoDB.git
   ```

2. Acesse o diretório do projeto:
   ```
   cd Cadastro-Contatos-Flask-MongoDB
   ```

3. Instale o Flask e pymongo utilizando o pip:
   ```
   pip install Flask pymongo
   ```

5. Execute o aplicativo:
   ```
   python app-mongo.py
   ```

6. Acesse o aplicativo no seu navegador web em `http://localhost:5000/`.

## Rotas

- `/`: Rota principal que exibe a lista de contatos cadastrados.
- `/criarContato`: Rota para criar um novo contato.
- `/criarContato` (método POST): Rota para enviar o formulário de criação de contatos.
- `/editarContato/<id>`: Rota para editar um contato específico com base no ID fornecido.
- `/editarContato/<id>` (método POST): Rota para enviar o formulário de edição de contatos.
- `/excluirContato/<id>`: Rota para excluir um contato específico com base no ID fornecido.

## Contribuindo

Contribuições são bem-vindas! Se você deseja contribuir com esta aplicação e torná-la ainda melhor, sinta-se à vontade para abrir issues ou enviar pull requests. Certifique-se de que suas contribuições estejam alinhadas com os padrões de código e diretrizes do projeto.

## Contato

Se tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato comigo pelo meu e-mail dbrdejesus15@gmail.com.
