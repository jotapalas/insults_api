from flask import Flask
from flask_restful import Resource, Api
from flask.json import jsonify
from get_data import get_data, get_data_mapped

app = Flask(__name__)
api = Api(app)


class Comeback(Resource):
  def get(self):
    comebacks = get_data('comebacks', ['id', 'comeback'])
    return jsonify({'comebacks': comebacks})

class Insult(Resource):
  def get(self):
    insults = get_data('insults', ['id', 'insult'])
    return jsonify({'insults': insults})

class All(Resource):
  def get(self):
    insult_comebacks = get_data('insult_comeback', ['insult_id', 'comeback_id'])
    insults = get_data_mapped('insults')
    comebacks = get_data_mapped('comebacks')
    for ic in insult_comebacks:
      insult_id = ic['insult_id']
      comeback_id = ic['comeback_id']
      insult = insults[insult_id]
      if 'comebacks' not in insult.keys():
        insult['comebacks'] = []
      comeback = comebacks[comeback_id]
      insult['comebacks'].append(comeback)
    return jsonify({'insults': insults})


api.add_resource(Insult, '/api/insults')
api.add_resource(Comeback, '/api/comebacks')
api.add_resource(All, '/api/all')

if __name__ == '__main__':
  app.run(port=1337, debug=True)