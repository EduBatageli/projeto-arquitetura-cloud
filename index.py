from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Configuração inicial do Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///finance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar banco de dados
db = SQLAlchemy(app)

# Modelo do Banco de Dados
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(10), nullable=False)  # "credit" ou "debit"
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, default=datetime.utcnow)

# Inicializar o banco de dados
with app.app_context():
    db.create_all()

# Rota para registrar lançamentos (créditos ou débitos)
@app.route('/transactions', methods=['POST'])
def add_transaction():
    data = request.get_json()
    type_ = data.get('type')
    amount = data.get('amount')

    if type_ not in ['credit', 'debit'] or amount is None:
        return jsonify({"error": "Invalid data"}), 400

    transaction = Transaction(type=type_, amount=amount)
    db.session.add(transaction)
    db.session.commit()
    return jsonify({"message": "Transaction added successfully"}), 201

# Rota para obter o saldo consolidado diário
@app.route('/balance', methods=['GET'])
def get_balance():
    today = datetime.utcnow().date()
    transactions = Transaction.query.filter_by(date=today).all()

    credit = sum(t.amount for t in transactions if t.type == 'credit')
    debit = sum(t.amount for t in transactions if t.type == 'debit')
    balance = credit - debit

    return jsonify({
        "date": str(today),
        "credit": credit,
        "debit": debit,
        "balance": balance
    })

# Rota de status para verificar o funcionamento do servidor
@app.route('/status', methods=['GET'])
def status():
    return jsonify({"message": "Server is running!"})

# Inicializar servidor
if __name__ == '__main__':
    app.run(debug=True)
