/*
  ----------------------------------------------------------------------------------------
  Obter a lista de pacotes python registrados na base de dados, via requisição GET
  ----------------------------------------------------------------------------------------
*/

const getList = async () => {
  let url = 'http://localhost:8002/packages';
  fetch(url, {
    method: 'get',
    mode: 'cors'
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data)
      data.forEach(package => insertList(package.pkg_nome, package.pkg_last_version, package.pkg_uploaded_at))
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Carregamento inicial dos dados
  --------------------------------------------------------------------------------------
*/

getList()

/*
  --------------------------------------------------------------------------------------
  Inserir um pacote python na base de dados via requisição POST
  --------------------------------------------------------------------------------------
*/

const postItem = async (nome) => {
  const formData = new FormData();
  formData.append('nome', nome);
  
  let url = 'http://localhost:8002/package';
  fetch(url, {
    method: 'post',
    mode: 'cors',
    body: formData
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });

    window.location.reload(true); 
}

/*
  --------------------------------------------------------------------------------------
  Cria um botão "delete" para cada item da lista, para remover o item
  --------------------------------------------------------------------------------------
*/

const insertDeleteButton = (parent) => {
  let span = document.createElement("span");
  let txt = document.createTextNode("\u24CD");
  span.className = "delete-btn";
  span.appendChild(txt);
  parent.appendChild(span);
}

const insertUpdateButton = (parent) => {
  let span = document.createElement("span");
  let txt = document.createTextNode("\u21BA");
  span.className = "update-btn";
  span.appendChild(txt);
  parent.appendChild(span);
}

/*
  --------------------------------------------------------------------------------------
  Remover um item da lista ao clicar no botão "delete"
  --------------------------------------------------------------------------------------
*/

const removeElement = () => {
  let del = document.getElementsByClassName("delete-btn");
  let i;
  for (i = 0; i < del.length; i++) {
    del[i].onclick = function () {
      let div = this.parentElement.parentElement;
      const nome = div.getElementsByTagName('td')[0].innerHTML
      if (confirm("Tem certeza que quer remover " + nome + " ")) {
        div.remove()
        deleteItem(nome)
        alert(nome + " removido!")
      }
    }
  }
}

/*
  --------------------------------------------------------------------------------------
  Atualizar um item da lista ao clicar no botão "update"
  --------------------------------------------------------------------------------------
*/

const updateElement = () => {
  let upd = document.getElementsByClassName("update-btn");
  let i;
  for (i = 0; i < upd.length; i++) {
    upd[i].onclick = function () {
      let div = this.parentElement.parentElement;
      const nome = div.getElementsByTagName('td')[0].innerHTML
      if (confirm("Tem certeza que quer atualizar " + nome + " ")) {

        updateItem(nome)
        alert(nome + " atualizado!")
        window.location.reload()
      }
    }
  }
}

/*
  --------------------------------------------------------------------------------------
  Deletar um pacote da base de dados via requisição DELETE
  --------------------------------------------------------------------------------------
*/
const deleteItem = (nome) => {
  console.log(nome)
  let url = 'http://localhost:8002/package?nome=' + nome;
  fetch(url, {
    method: 'delete',
    mode: 'cors'
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    })
}

/*
  --------------------------------------------------------------------------------------
  Atualiza um pacote da base de dados via requisição UPDATE
  --------------------------------------------------------------------------------------
*/
const updateItem = (nome) => {
  console.log(nome)
  let url = 'http://localhost:8002/package?nome=' + nome;
  fetch(url, {
    method: 'put',
    mode: 'cors'
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    })
}

/*
  ---------------------------------------------------------------------------------------
  Adicionar um novo pacote python na base de dados 
  ---------------------------------------------------------------------------------------
*/
const newPackage = () => {
  let nome = document.getElementById("input-nome").value;

  // Verifica se o pacote já se encontra cadastrado, antes de tentar adicionar
  const checkExistente = 'http://localhost:8002/package';
  fetch(checkExistente, {
    method: 'post',
    mode: 'cors',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      nome: nome
    })
  })
  .then((response) => response.json())
  .then((data) => {
    if (!nome) {
      alert("Informe o nome do pacote!");
    } else if (data.packages && data.packages.some(item => item.nome === nome)) {
      alert("O pacote já se encontra cadastrado na base de dados.");
    } else {
      // Insere o nome do pacote na lista que será apresentada no frontend
      insertList(nome);
      // Envia esse dado para ser gravado na base de dados
      postItem(nome);
      alert("Pacote " + nome + " adicionado");
    }
  })
  .catch((error) => {
    console.error('Error:', error);
  });
}

/*
  --------------------------------------------------------------------------------------
  Insere items na lista a ser exibida  
  --------------------------------------------------------------------------------------
*/

const insertList = (nome, last_version, uploaded_at) => {
  let package = [nome, last_version, uploaded_at];
  let table = document.getElementById('table-pacotes'); //or let table = document.querySelector("table-pacotes")
  let row = table.insertRow();  
  
  for (let i = 0; i < package.length; i++) {
    let cel = row.insertCell(i);
    cel.textContent = package[i];
  }
  
  // Inserir um botão ao lado do registro inserido na lista, para possibilitar atualizar esse registro
  insertUpdateButton(row.insertCell(3));

  // Inserir um botão ao lado do registro inserido na lista, para possibilitar remover esse registro
  insertDeleteButton(row.insertCell(-1));

  // limpar elementos do formulário de entrada de dados
  document.getElementById("input-nome").value="";

  // Coloca o foco no primeiro item do formulário de entrada de dados
  document.getElementById("input-nome").focus();  

  // Caso o botão de atualização seja clicado, atualiza esse elemento e o retorna à lista
  updateElement();

  // Caso o botão de remoção seja clicado, remove esse elemento da lista
  removeElement();
  
}


/*
  ---------------------------------------------------------------------------------------
  Fechar a aplicação 
  ---------------------------------------------------------------------------------------
*/
function closeApp () {
  if (confirm("Deseja encerrar a aplicação?")) {
    window.close();
  }
}
