import os
import json

from flask import Flask, jsonify, session, request
from flask_cors import CORS

from model_class.model import Model

from data.data_cleaning_functions import load_data
from data.data_class import Data

from data.constants import target

import pickle


def serialize_class(obj):
    return pickle.dumps(obj)

# A helper function to deserialize the class object
def deserialize_class(serialized_obj):
    return pickle.loads(serialized_obj)

csv_file_path = 'data/data_raw.csv'
rp = 'data/repeat_off.csv'


app = Flask(__name__)
app.secret_key = 'your_secret_key'
cors = CORS(app, origins='*')

# @app.route('/api/test', methods=['GET'])

def load_d_data(target):
    rd = load_data(csv_file_path)
    rd1 = load_data(rp)
    D = Data(rd, rd1)
    D.add_actors()

    D.split_data()

    D.make_feature_options()

    M = Model(D, target)

    return (D, M)

@app.route('/api/start', methods=['GET'])
@app.route('/api/test', methods=['GET'])
def start():
    rd = load_data(csv_file_path)
    rd1 = load_data(rp)
    D = Data(rd, rd1)
    D.add_actors()

    D.split_data()

    D.make_feature_options()
    D.make_json()
    D.test_movies_json()

    AM = []
    for x in target:
        M = Model(D, x )
        M.make_log_reg()

        M.get_distribution()
        M.make_box_plot()
        M.heat_map()
        M.make_histograms()

        model_obj = {
            'target': M.target,
            'score': M.score,
            'distribution': M.distribution,
            'correlation_matrix': M.corr_matrix,
            'histograms': M.histograms,
        }
        AM.append(model_obj)

    return jsonify({
        'data': {
            'models': AM,
            'movie_data': D.json,
            'test_movies': D.test_movies
        }
    })

@app.route('/api/ada_boost', methods=['GET'])
def ab():
    (D, M) = load_d_data(request.args.get('target'))
    M.ada_boost()

    return jsonify({
        'data': M.ada_boost_results
    })

@app.route('/api/dt', methods=['GET'])
def dt():
    (D, M) = load_d_data(request.args.get('target'))
    M.decision_tree()

    return jsonify({
        'data': M.dt_results
    })

@app.route('/api/kbest', methods=['GET'])
def k_best():
    (D, M) = load_d_data(request.args.get('target'))
    M.get_kbest()

    return jsonify({
        'data': {
            "best_features": M.k_best_features,
            "models": M.k_best_results
        }
    })

@app.route('/api/best_log_reg', methods=['GET'])
def best_log_reg():
    (D, M) = load_d_data(request.args.get('target'))
    M.make_log_reg()

    return jsonify({
        'data': M.log_reg_results
    })

@app.route('/api/rfe', methods=['GET'])
def get_rfe():
    (D, M) = load_d_data(request.args.get('target'))
    M.get_rfe()

    return jsonify({
        'data': {
            "best_features": M.rfe_best_features,
            "models": M.rfe_scores
        }
    })

@app.route('/api/random_forest', methods=['GET'])
def get_rf():
    (D, M) = load_d_data(request.args.get('target'))
    M.random_forrest()

    return jsonify({
        'data': {
            'models': M.rf_scores,
            "best_features": M.rf_best_features,
        }
    })

@app.route('/api/svc', methods=['GET'])
def get_svc():
    (D, M) = load_d_data(request.args.get('target'))
    M.svc()

    return jsonify({
        'data': M.svc_results
    })

@app.route('/api/poly', methods=['GET'])
def get_poly():
    (D, M) = load_d_data(request.args.get('target'))
    M.poly_preprocess()

    return jsonify({
        'data': M.ply_results
    })

@app.route('/api/best', methods=['GET'])
def get_best():
    (D1, M1) = load_d_data('Zach')
    (D2, M2) = load_d_data('Amin')
    (D, M) = load_d_data('Mayes')
    M.find_best_log_reg()
    M1.find_best_log_reg()
    M2.find_best_log_reg()

    return jsonify({
        'data': {
            'Mayes': {
                'best': M.best,
                'f': M.best_f
            },
            'Zach': {
                'best': M1.best,
                'f': M1.best_f
            },
            'Amin': {
                'best': M2.best,
                'f': M2.best_f
            },
        }
    })

@app.route('/api/prediction', methods=['POST'])
def predict():
    (D, M) = load_d_data("Zach")
    (D, M1) = load_d_data("Mayes")
    (D, M2) = load_d_data("Amin")
    this_data = request.get_json()
    print(this_data)

    test = this_data.get('data')

    # test = {
    #     'Time': 170,
    #     'RT Aud': 94,
    #     'RT Crit': 83,
    #     'Box Off WW': 170000000,
    #     'Aud #': 100000,
    #     "Action": 1,
    #     'Crime': 1,
    #     'Drama': 1,
    #     'Budget': 50000000,
    #     'Comedy': 0,
    #     'Combo': 177,
    #     'Cost:': 0,
    #     'Pick_0': 1
    # }

    M.make_prediction(this_data)
    M1.make_prediction(this_data)
    M2.make_prediction(this_data)

    return jsonify({
        'data': {
            'Zach': M.movie_prediction,
            'Mayes': M1.movie_prediction,
            'Amin': M2.movie_prediction,
        }
    }), 200



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))