# Importando os módulos necessários
from flask import Flask, render_template, render_template_string, request, redirect, url_for
import json
import os
import random

# Inicializando a aplicação Flask
app = Flask(__name__)

# Definindo o caminho do arquivo JSON
CLIENTES_JSON_PATH = 'clientes.json'

# Função para obter os dados do cliente
def obterAluno():
    # Verificando se o arquivo existe
    if os.path.exists(CLIENTES_JSON_PATH):
        # Carregando os dados do arquivo JSON
        with open(CLIENTES_JSON_PATH, 'r') as arquivo:
            return json.load(arquivo)
    else:
        # Se o arquivo não existir, retorna uma lista vazia
        return []

# Função para salvar os dados do cliente
def salvarAluno(aluno):
    # Gravando os dados no arquivo JSON com formatação indentada
    with open(CLIENTES_JSON_PATH, 'w') as arquivo:
        json.dump(aluno, arquivo, indent=2)

# Rota para a página inicial
@app.route('/')
def pagInicial():
    return render_template('index.html')

# Rota para cadastrar um cliente
@app.route('/cadastrarAluno', methods=['POST'])
def cadastrarAluno():
    # Obtendo os dados do formulário
    nome = request.form.get('nome')
    telefone = request.form.get('telefone')
    filial = request.form.get('filial')
    curso = request.form.get('curso')
    

    # Verificando se o cliente já existe
    if not alunoExistente(nome, telefone, filial, curso):
        # Criando um dicionário com os dados do cliente
        aluno = {"nome": nome, "telefone": telefone, "filial": filial, "curso": curso}
        
        # Obtendo a lista de clientes existentes
        alunosExistentes = obterAluno()

        # Adicionando o novo cliente à lista
        alunosExistentes.append(aluno)


        # Salvando a lista atualizada de clientes
        salvarAluno(alunosExistentes)
        
        return redirect(url_for('pagInicial'))
    else:
        return 'Cliente já existente'
    
# Função para verificar se um cliente já existe
def alunoExistente(nome, telefone, filial, curso):
    alunos = obterAluno()
    for aluno in alunos:
        if aluno['nome'] == nome and aluno['telefone'] == telefone and aluno['filial'] == filial and aluno['curso'] == curso:
            return True
    return False

# Rota para listar os clientes
@app.route('/listarAlunos')
def listarAlunosRoute():
    return listarAlunos()
    
    
    
# Função para listar os clientes
def listarAlunos():
    alunos = obterAluno()
    respostaHtml = '<link rel="stylesheet" href="../static/css/style.css">'
    respostaHtml += '<table class="tabelaLista"><thead><td colspan="4">Lista de participantes</td></thead><tr><th>Nome</th><th>Telefone</th><th>Filial</th><th>Curso</th></tr>'
    for aluno in alunos:
            respostaHtml +=  f'<tr><td>{aluno["nome"]}</td><td>{aluno["telefone"]}</td><td>{aluno["filial"]}</td><td>{aluno["curso"]}</td></tr>'
    respostaHtml += '</table>'        
    return render_template_string(respostaHtml)

#função para sortear os alunos
@app.route('/sortearAlunos')
def sortearAlunosRoute():
    return sortearAlunos()

def sortearAlunos():
    alunos = obterAluno()
    aluno = random.choice(alunos)
    respostaHtml = '<link rel="stylesheet" href="../static/css/style.css">'
    respostaHtml += '<div class="pagGanhador"><h1> Parabéns '+f'{aluno["nome"]}'+'<br>Você ganhou o sorteio!!</h1><p>aluno da filial de '+f'{aluno["filial"]}'+' do curso '+f'{aluno["curso"]}</p></div>'
    return render_template_string(respostaHtml)

# Executando a aplicação se o script for executado diretamente
if __name__ == '__main__':
    app.run(debug=True)



