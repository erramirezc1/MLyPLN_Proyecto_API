#!/usr/bin/python
from flask import Flask
from flask_restx import Api, Resource, fields
import joblib
from m02_model_deployment import predict_popu

app = Flask(__name__)

api = Api(
    app, 
    version='1.0', 
    title='API - prediccion de popularidad de canciones',
    description='API que predice la pularidad de una cancion con base en su duracion y si es explicita o no')

ns = api.namespace('predict', 
     description='Popularidad')

parser = ns.parser()
parser.add_argument(
    'duration_ms', 
    type=int, 
    required=True, 
    help='Duración de la canción en milisegundos', 
    location='args'
)
parser.add_argument(
    'explicit', 
    type=int, 
    required=True, 
    help='Indica si la canción es explícita (0 = No, 1 = Sí)', 
    location='args'
)

resource_fields = api.model('Resource', {
    'result': fields.String,
})

@ns.route('/')
class PopularidadApi(Resource):

    @ns.doc(parser=parser)
    @ns.marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()
        duration_ms = args['duration_ms']
        explicit = args['explicit']
        
        from model_deployment.m02_model_deployment import predict_popu

        resultado = predict_popu(duration_ms, explicit)
        return {
            "result": str(resultado)
        }, 200
        
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)