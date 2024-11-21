# **Controle de Fluxo de Caixa**

Este é um projeto básico de controle de fluxo de caixa diário desenvolvido em **Python** usando **Flask**. Ele permite o registro de transações financeiras (créditos e débitos) e exibe um saldo diário consolidado.

---

## **Funcionalidades**

- Registrar transações financeiras (créditos e débitos).
- Exibir o saldo consolidado diário (total de créditos, débitos e saldo final).
- Servidor simples para testes locais.

---

## **Tecnologias Utilizadas**

- **Python 3.8+**
- **Flask**
- **Flask-SQLAlchemy**
- Banco de dados **SQLite** para armazenamento local.

---

## **Como Executar**

### **Pré-requisitos**

Certifique-se de ter o Python instalado. Caso não tenha, baixe-o em [python.org](https://www.python.org/).

### **Passos**

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/EduBatageli/projeto-arquitetura-cloud
   cd controle-fluxo-caixa

2. **Crie um ambiente virtual**
   ```bash
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows
3. **Instale as dependências:**
4. **Rode o programa**
5. **Acesse no navegador ou via ferramentas como Postman:**
   ```bash
   Status do servidor:
      http://127.0.0.1:5000/status
   Registrar transações:
      POST http://127.0.0.1:5000/transactions
   Consultar saldo diário:
      GET http://127.0.0.1:5000/balance
 
