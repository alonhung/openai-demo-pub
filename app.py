from flask import Flask, render_template, jsonify, request
import config
import openai
import aiapi
import azureApi
import func

def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__)
app.config.from_object(config.config['development'])

app.register_error_handler(404, page_not_found)


@app.route('/', methods = ['POST', 'GET'])
def index():
    
    if request.method == 'POST':
      prompt = request.form['prompt']

      res = {}
      res['answer'] = func.request_from_pribate_EC2(prompt)
      return jsonify(res), 200
        
    return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)
