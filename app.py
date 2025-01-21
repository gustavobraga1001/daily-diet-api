from flask import Flask, jsonify, request
from datetime import datetime

from models.snack import Snack # linha que adicionei
from database import db 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:admin123@127.0.0.1:3306/flask-diet-api'

db.init_app(app)

@app.route('/ola', methods=["GET"])
def ola():
    return jsonify({"message": "ola"})

@app.route("/snack", methods=["POST"])
def create_snack():
    data = request.json
    name = data.get('name')
    description = data.get('description')
    date = data.get('date')
    isInside = data.get('isInside')
    
    if name and description and date:
        date_format = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        snack = Snack(name=name, description=description, datetime=date_format, isInside=isInside)
        db.session.add(snack)
        db.session.commit()
        return jsonify({"message": "Refeição cadastrada com sucesso"}), 201
    
    return jsonify({"message": "Dados inválidos"}), 400

@app.route("/snack/<int:snack_id>", methods=["PUT"])
def update_snack(snack_id):
    data = request.json
    snack = Snack.query.get(snack_id)

    if snack:
        snack.name = data.get("name")
        snack.description = data.get("description")
        snack.datetime = data.get("datetime")
        snack.isInside = data.get("isInside")
        db.session.commit()

        return jsonify({"message": f"Refeição {snack_id} atualizada com sucesso!"}), 201
    
    return jsonify({"message": "Refeição não encontrada"}), 404

@app.route("/snack/<int:snack_id>", methods=["DELETE"])
def delete_user(snack_id):
    snack = Snack.query.get(snack_id)
    
    if snack :
        db.session.delete(snack)
        db.session.commit()
        return jsonify({"message": f"Refeição {snack_id} deletada com sucesso!"})
    
    return jsonify({"message": "Refeição não encontrada"}), 404

@app.route("/snack/<int:snack_id>", methods=["GET"])
def read_snack(snack_id):
    snack = Snack.query.get(snack_id)
    if snack:
        return jsonify({"snack": snack.to_dict()})
    
    return jsonify({"message": "Refeição não encontrada"}), 404

@app.route("/snack", methods=["GET"])
def read_snacks():
    snacks = Snack.query.all()
    if snacks:
        snacks_list = [snack.to_dict() for snack in snacks]
        return jsonify({"snacks": snacks_list})
    
    return jsonify({"message": "Nenhuma refeição encontrada"}), 404

if __name__ == "__main__":
    app.run(debug=True)