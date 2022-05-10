from re import X
from flask import Flask, render_template
from music import music

app = Flask(__name__)
# Incuindo a rota que receberá a temperatura e devolverá a lista de músicas
@app.route('/music', methods=['GET', 'POST'])
# Modelo de try/exept para rodar o código e lidar com possíveis erros
try:
  def prog():
    return render_template('input.html')
    music()
    print(X)
  
except:
  print("O serviço não está funcionando, porém segue em desenvolvimento")

if __name__ == '__main__':
    app.run(host='127.8.8.0', port=105)