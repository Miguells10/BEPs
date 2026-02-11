from flask import Flask, jsonify, request
from flasgger import Swagger, swag_from
import base64

app = Flask(__name__)
swagger = Swagger(app)

tarefas = [
    {'id': 1, 'titulo': 'Comprar leite', 'concluida': False},
    {'id': 2, 'titulo': 'Estudar para a prova', 'concluida': True},
    {'id': 3, 'titulo': 'Lavar o carro', 'concluida': False}
]

@app.route('/tarefas', methods=['GET'])
@swag_from('docs/listar_tarefas.yml')
def listar_tarefas():
    return jsonify(tarefas)

@app.route('/tarefas', methods=['POST'])
@swag_from('docs/adicionar_tarefa.yml')
def adicionar_tarefa():
    dados = request.get_json()
    nova_tarefa = {
        'id': len(tarefas) + 1,
        'titulo': dados['titulo'],
        'concluida': False
    }
    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa), 201

@app.route('/tarefas/<int:tarefa_id>', methods=['DELETE'])
@swag_from('docs/deletar_tarefa.yml')
def deletar_tarefa(tarefa_id):
    global tarefas
    tarefas = [tarefa for tarefa in tarefas if tarefa['id'] != tarefa_id]
    return '', 204

@app.route('/tarefas/<int:tarefa_id>', methods=['PUT'])
@swag_from('docs/alterar_tarefa.yml')
def atualizar_tarefa(tarefa_id):
    dados = request.get_json()
    for tarefa in tarefas:
        if tarefa['id'] == tarefa_id:
            tarefa['titulo'] = dados.get('titulo', tarefa['titulo'])
            tarefa['concluida'] = dados.get('concluida', tarefa['concluida'])
            return jsonify(tarefa)
    return jsonify({'erro': 'Tarefa não encontrada'}), 404

@app.route("/basic")
@swag_from('docs/basic.yml')
def basic():
    auth = request.headers.get("Authorization")
    if not auth:
        return jsonify({"error": "Credenciais não enviadas"}), 401
    scheme, encoded = auth.split()
    user, pwd = base64.b64decode(encoded).decode().split(":")
    if user == "admin" and pwd == "123":
        return {"message": "Acesso permitido"}
    return {"error": "Credenciais inválidas"}, 403

if __name__ == '__main__':
    app.run(debug=True)