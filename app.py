from re import X
from flask import Flask, render_template
from music import music

app = Flask(__name__)

@app.route('/music', methods=['GET', 'POST'])

try:
  def prog():
    return render_template('input.html')
    music()
    print(X)
  
except:
  print("O serviço não está funcionando, porém segue em desenvolvimento")

if __name__ == '__main__':
    app.run(host='127.8.8.0', port=105)