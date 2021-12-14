from flask import Flask
from src.system import OrderSystem

system = OrderSystem()

app = Flask(__name__)
app.secret_key = 'very-secret-123'  # Used to add entropy

