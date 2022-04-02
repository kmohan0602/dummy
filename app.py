import os
import sys
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # device = torch.device('cpu')
    # return render_template('index.html')
    return "Hello WOrld!!"


if __name__ == '__main__':
    app.run()