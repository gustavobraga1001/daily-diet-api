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

if __name__ == "__main__":
    app.run(debug=True)