function alterarNome(id, nome){

      // Preencher os campos de input com os dados da linh
    document.getElementById('id').value = id;
    document.getElementById('nome').value = nome;
      // Adicione mais campos de input conforme necessário
    };


function alterCarro(id, placa, modelo){

    // Preencher os campos de input com os dados da linh
    document.getElementById('id').value = id;
    document.getElementById('placa').value = placa;
    document.getElementById('modelo').value = modelo;
    // Adicione mais campos de input conforme necessário
    };


function alterCidade(id, nome, estado){
    document.getElementById('id').value = id;
    document.getElementById('nome').value = nome;
    document.getElementById('estado').value = estado;
};


function alterTipo(id, tipo){
    document.getElementById('id').value = id;
    document.getElementById('tipo').value = tipo;
};


function alterPg(id, tipo){
    document.getElementById('id').value = id;
    document.getElementById('tipo').value = tipo;
};


function somaKm(){
    var kmi = document.getElementById('kmi');
    var kmf = document.getElementById('kmf');
    document.getElementById('kmr'). value = parseInt(kmf.value) - parseInt(kmi.value);
};




