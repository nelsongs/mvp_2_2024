# Projeto: TrackLastPackage - Verificador da última versão de Pacotes Python
### *MVP-2, "Arquitura de Software" do Curso de Engenharia de Software da PUC Rio, 2024*
### Aluno: Nelson Gomes da Silveira

Este projeto é o resultado final (**MVP-2**) da aplicação dos conhecimentos obtidos ao cursar a disciplina **Arquitetura de Software** do Curso de Engenharia de Software da PUC Rio, ano de 2024.

O objetivo do projeto é demonstrar a construção de uma aplicação python que exiba a últia versão de um determinado pacote python. Para tal, faremos uso de dados obtidos a partir de uma API externa, por meio de técnicas e padrões "REST". 

Os dados dos pacotes python retornados da API externa serão persistidos em uma base de dados MySQL, a partir do qual poderão ser consultados e atualizados, além de serem apresentados no *frontend*.

O projeto consiste dos seguintes componentes (todos no repositório https://github.com/nelsongs/mvp_2_2024):

1. Pasta **backend**, onde se encontra toda a estrutura de pastas e arquivos do *backend* da aplicação.

2. Pasta **frontend**, onde se encontra toda a estrutura de pastas e arquivos do *frontend* da aplicação.


Em seguida, uma breve descrição dos componentes principais da aplicação e os passos para replicá-la.

A porção *frontend* do aplicativo é uma aplicação web simples, rodando em um navegador web. No frontend você pode informar o nome do pacote python que você quer seguir e ele é cadastrado em uma base de dados MySQL, por meio de uma chamada REST para o **Back End**. 

Além de cadastrar novos pacotes do seu interesse, o **Front End** também exibe os pacotes já cadastrados e sua última versão e data/hora de upload dele para o repositório PyPI, pelos desenvolvedores. 

A porção *backend* é toda desenvolvida utilizando a linguagem de programação Python3. O script principal dessa porção *backend* chama-se **app.py** e encapsula, por meio de bibliotecas, a API de documentação open source **Swagger**, que padroniza a integração dos processos de definir, criar e documentar a aplicação, possuindo recuros como *endpoints*, dados recebidos, dados retornados, código HTTP e métodos de autenticação, entre outros. Apenas funcionalidades mínimas do **Swagger** são utilizados nesta aplicação.

## Como executar 

Clone ou copie o conteúdo existente na pasta do projeto em https://github.com/nelsongs/mvp_2_2024, onde se encontra todo o conteúdo da aplicação.

Ao acionar Ctrl-clicK no link acima, uma janela será aberta no seu navegador, no diretório público do projeto no GitHub. Logo acima, no canto superior direito, você visualiza o botão *<> Code* na cor verde. Clique em sua setinha e, na janela de diálogo que abre, clique naquele ícone com as duas janelinhas quadradas sobrepostas, ao final da linha com o endereço **https://github.com/nelsongs/mvp_2_2024.git**. Isso copiará esse endereço para a memória. 

Em seguida, no seu VSCode ,clique em Clone Git Repository e dê um Ctrl-V na janelinha de endereço que abre no topo. Com o endereço no campo de entrada, pressione **Enter** no seu teclado. Uma janela de diálogo será aberta, na qual você escolherá a pasta onde deseja que esse repositório seja clonado. Clique então no botão ***Select as Repository Destination***. O repositório Git será clonado nessa sua pasta.

Uma alternativa a clonar o diretório é você clicar na última linha dessa caixa de diálogo, em arquivo Download ZIP. Isso baixará todo essa pasta em formato comprimido .zip, para a pasta que você designar e onde você deverá descomprimir o seu conteúdo.

Em seguida, abra um Terminal ou Shell e vá para o diretório trackpy_backend. Lá, crie um ambiente virtual Python para rodar essa aplicação, da seguinte forma:

---
- python -m venv env
---

Esse comando criará o ambiente virtual onde essa aplicação será executada, resolvendo problemas de conflito entre ambientes python distintos que você possa ter.

Após criado o ambiente virtual, será necessário ativá-lo. Para isso, dependendo do seu Sistema Operacional, você utilizará um dos *scripts* presentes no diretório **env/Scripts** (ou **env\Scripts** no Windows). Provavelmente nos sistemas Unix-like, como o Mac OSX e o Linux, o comando será:

---
- env/Scripts/activate
---

Para o caso específico do Windows, no qual você normalmente usa o PowerShell, o comando é:

---
- env\Scripts\Activate.ps1
---

Pronto, o ambiente virtual python deverá estar rodando, o qual você poderá confirmar pela **(env)** no início da sua linha de comando.

Se precisar desativar o ambiente virtual por qualquer motivo, utilize o comando **env/Scripts/deactivate ou env\Scripts\deactivate** (Unix-like ou Windows, respectivamente).

Em seguida, instale as bibliotecas listadas no arquivo `requirements.txt`, presente no mesmo diretório onde você se encontra com o Terminal/Shell aberto. As bibliotecas presentes nesse arquivo são dependências que a aplicação python necessita. Instale-as por meio do seguinte comando:

---
- pip install -r requirements.txt
---

Na sequência, para executar a API que criará e gerenciará a base de dados, execute o seguinte comando:

---
- (env)$ flask run --host 0.0.0.0 --port 8002
---

Esse comando, além de criar uma instância vazia da base de dados MySQL, fará com que a aplicação de *backend* espere requisições no endereço 127.0.0.1, na porta 8002. As requisições serão entregues por meio da aplicação de *frontend* e serão recebidas e tratadas pela aplicação de *backend*, interfaceando com a API externa e com camada de base de dados da aplicação.

As camadas **Back End**, **Front End** e **Database** da aplicação estão conteinizadas por meio do aplicativo **Docker**

Um arquivo MVP_2_NGS.SVG, presente na pasta do **Back End**, mostra o esquema da aplicação como um todo.

Para que essa aplicação de ***backend*** rode e fique esperando requisições por parte da porção cliente (***frontend***), é necessário abrir uma página no navegador, com o seguinte endereço:
---
- http://127.0.0.1:8002
---

Alternativamente você pode utilizar o endereço:

---
- http://localhost:8002
---

O navegador deve mostrar uma página inicial com o ***Swagger***, o qual serve para não apenas confirmar que a aplicação está executando satisfatoriamnmete, como também pode ser usado para inserir e verificar o sucesso da inserção de dados na base de dados SQLite3.

Feito isso, você agora pode rodar a aplicação *frontend*, presente na pasta **frontend**. Para isso, execute (duplo clique) o arquivo index.html presente na raiz dessa pasta. Você poderá então verificar que, se inseriu dados pelo Swagger, esses aparecerão na interface web. A partir dai você poderá continuar cadstrando nomes de pacotes diretamente na interface web. Após a confirmação da inserção dos dados, esses serão enviados à aplicação *backend*, onde serão tratados, persistidos no banco de dados  e apresentados no fronend, na porção **Pacotes python cadastrados**.

Se estiver com a janela do Terminal/Shell ainda aberta, você poderá acompanhar o retorno dos códigos de execução no Terminal/Shell e verificar os dados sendo inseridos/deletados etc.

Boa sorte!
