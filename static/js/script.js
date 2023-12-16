function abrirSorteio(){
    sorteioVariavel = document.getElementById('sorteio').src='/sortearAlunos';
    document.getElementById('sorteio').style.display = 'block';
}

function formatarTelefone(inputTelefone) {
    var valorTelefone = inputTelefone.value.replace(/\D/g, ''); // Remove caracteres não numéricos
    var formatoTelefone = '';

    for (var i = 0; i < valorTelefone.length; i++) {
      if (i === 0) {
        formatoTelefone += '(';
      } else if (i === 2) {
        formatoTelefone += ') ';
      } else if (i === 3) {
        formatoTelefone += ' ';
      } else if (i === 7) {
        formatoTelefone += '-';
      }

      formatoTelefone += valorTelefone.charAt(i);
    }

    inputTelefone.value = formatoTelefone;

    // Exibir mensagem de erro se o número não tiver 11 dígitos
    var erroTelefone = document.getElementById('erroTelefone');
    erroTelefone.textContent = valorTelefone.length === 11 ? '' : 'Número de telefone inválido';
  }