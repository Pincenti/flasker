from app import app
from flask import redirect, jsonify


@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return jsonify({})


@app.route('/products')
def products():
    return jsonify({})
