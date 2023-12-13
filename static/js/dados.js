function somarkm(){
    var kmi = document.getElementById('kmi');
    var kmf = document.getElementById('kmf');
    var qnt = document.getElementById('qnt');
    var kmr = document.getElementById('kmr');
    if (qnt.value == ""){
        alert('Quantidade deve ser preenchida!!');
        kmf.value = "";
        qnt.focus();
    }else{
        kmr.value = parseInt(kmf.value) - parseInt(kmi.value);
        var media = parseFloat(kmr.value) / parseFloat(qnt.value)
        document.getElementById('consumo').value = media.toFixed(2);
        document.getElementById('cidade').focus();
    };
    
};


function despesa(){
    var despesa = document.getElementById('tipo');
    var kmi = document.getElementById('kmi');
    var kmf = document.getElementById('kmf');
    var kmr = document.getElementById('kmr');
    var consumo = document.getElementById('consumo');
    var cidade = document.getElementById('cidade');
    var qnt = document.getElementById('qnt');
    if (despesa.value == '5'){
        kmi.value = '';
        kmf.value = '';
        kmr.value = '';
        consumo.value = '';
        qnt.value = '';
        kmi.readOnly = false;
        kmf.readOnly = false;
        qnt.readOnly = false;
    }else{
        if (despesa.value == '4' || despesa.value == '7'){
            var qnt = document.getElementById('qnt'); 
            qnt.value = '0';
            qnt.readOnly = true;
        }else{
            qnt.value = '';
            qnt.readOnly = false;
        };
        kmi.value = 0;
        kmf.value = 0;
        kmr.value = 0;
        consumo.value = 0;
        cidade.value = 22;
        kmi.readOnly = true;
        kmf.readOnly = true;
    };
};