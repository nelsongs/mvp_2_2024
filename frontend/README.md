# Front End da aplicação TrackLastPackage
## *MVP-2 2024 do Curso de Engenharia de Software da PUC Rio*

Este projeto faz parte do escopo da aplicação desenvolvida para o MVP-2 da Disciplina **Arquitetura de Software**.

Foi desenvolvido utilizando **HTML5**, **CSS3** e **Javascript** puros, sem utilização de frameworks ou bibliotecas.

Trata-se de uma aplicação minimalista, de 1 página apenas, contendo uma aplicação simples cujo objetivo é armazenar as informações
sobre a última versão dos pacotes python de interesse.

A aplicação recebe um nome de pacote e consulta uma API externa, no modo REST, onde é verificada a existência do nome de pacote inserido.

A API externa, que contém os dados dos pacotes python é o repositório PyPI, presente em https://pypi.org/pypi.
 

## Características:

- Simplista
- 1 página apenas
- *index.html* com estruturação básica para conter uma grade dividida em 2 áreas: a primeira é onde você insere o nome do pacote que você quer buscar e a segunda é onde os dados adicionais do pacote, retornados da API externa, sâo exibidos.

- Toda a formatação da página é realizada por meio do arquivo **CSS3** _styles.css_, empregando o conceito de Grid
- Uso da linguagem **Javascript**, presente no arquivo *scripts.js* para responder aos eventos de cadastramento, exibição e eliminação de items da base de dados

Todo o frontend foi conteinizado usando o Docker. A imagem gerada pode ser utilizada para rodar a aplicação.

> As rotinas Javascript desta aplicação  
> interfaceiam, via protocolos HTML POST, GET, PUT e DEL  
> com a aplicação de _Back End_ escrita em linguagem **Python**  
> a qual, por sua vez, encapsula as funcionalidades necessárias  
> para gerenciar a persistência dos dados em uma base de dados **MySQL**. 

---
## Como executar

Simplesmente baixe (clone) as duas pastas do projeto, **frontend** e **backend** a partir do meu repositário público [MVP_2_2024](https://github.com/nelsongs/mvp_2_2024/) no **GitHUB**. 

Depois de clonar os dois arquivos leia o arquivo ***README.md***, presente na raiz do diretório **backend**, que orienta como executar a aplicação de **Back End**, responsável por abrir e gerenciar a base de dados **MySQL**, que suporta a persistência dos dados da aplicação.

Com a aplicação de **Back End** rodando, vá à raiz do diretório **frontend** e execute o arquivo ***index.html***, clicando-o duas vezes com o seu mouse.

Se já houver dados na base de dados, estes serão exibidos na tela de exibição de dados, no painel direito da página web. 

Você pode inserir novos items no painel de entrada de dados, à esquerda. Basta clicar no primeiro campo e inserir o nome do pacote desejado.  

Com o nome do pacote inserido, basta clicar no botão **Inserir**. Esse dado inserido (nome do pacote desejado) é repassado ao **Back End**,
que fará uma chamada à API externa para verificar a existência desse pacote. Caso exista naquele repositórios, seus dados são retornado ao **Back End**, 
que os processa e captura apenas as informações sobre a última versão de sse pacote e a data e hora em que foi carregadao para o repositório pelos desenvolvedores.

Na sequencia, os dados são então cadastrados na base de dados **MySQL**, e retornados para exibição no **Front End**

Após a entrada dos dados, sua exibição no painel direito e sua gravação na base de dados, o cursor se posiciona no campo Nome do Pacote para nova entrada de dados.

Caso deseje encerrar a aplicação, basta clicar no botão **Sair**.

Boa sorte!
