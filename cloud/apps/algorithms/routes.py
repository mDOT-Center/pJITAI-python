# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import render_template, request

import json
from apps import db
from apps.algorithms import blueprint
from apps.algorithms.models import PrebuiltAlgorithms
from apps.learning_models.learning_model_service import get_all_available_models

@blueprint.route('/prebuilt-algorithms', methods=['GET', 'POST'])
def view_prebuilt_algorithms():

    prebuilt_algorithms = db.session.query(PrebuiltAlgorithms).filter(PrebuiltAlgorithms.type=="prebuilt").all()
    print(prebuilt_algorithms[0])

    return render_template('algorithms/algorithms_definitions.html',
                           msg='No Message',
                           prebuilt_algorithms=prebuilt_algorithms)

@blueprint.route('/algorithms_definitions', methods=['GET'])
def algorithms_definitions():

    algorithms_definitions = list_algorithms()
    return render_template('algorithms/algorithms_definitions.html',
                           msg='No Message',
                           algorithms_definitions=algorithms_definitions)

@blueprint.route('/my_algorithms', methods=['GET', 'POST'])
def my_algorithms():

    prebuilt_algorithms = db.session.query(PrebuiltAlgorithms).filter(PrebuiltAlgorithms.algorithm_type=="custom").all()
    return render_template('algorithms/algorithms_definitions.html',
                           msg='No Message',
                           prebuilt_algorithms=prebuilt_algorithms)


@blueprint.route('/algorithm_form/<algorithm_id>', methods=['GET', 'POST'])
def algorithm_form(algorithm_id):

    prebuilt_algorithms = db.session.query(PrebuiltAlgorithms).filter(PrebuiltAlgorithms.id == algorithm_id).all()

    return render_template('algorithms/algorithm_form.html',
                           msg='No Message',
                           prebuilt_algorithms=prebuilt_algorithms[0])


@blueprint.route('/algorithm_form2/<algorithm_name>', methods=['GET', 'POST'])
def algorithm_form2(algorithm_name):

    algorithm_definition = list_algorithms(algorithm_name)

    return render_template('algorithms/add_algorithm.html',
                           msg='No Message',
                           algorithm_definition=algorithm_definition)

@blueprint.route('/add_update_algo/', methods=['GET', 'POST'])
def add_update_algo():
    dd = json.loads(json.dumps(request.form))
    if 'add_update_algo' in request.form:
        algorithm_id = request.form.get("algorithm_id")
        username = request.form.get("algorithm_name")
        email = request.form.get("algorithm_description")
        email = request.form.get("algorithm_description")

        #prebuilt_algorithms = db.session.query(PrebuiltAlgorithms).filter(PrebuiltAlgorithms.id == algorithm_id).all()
        algorithm_name = ""
        algorithm_description = ""
        feature = {}
        tmp = {}
        #tmp["feature"] = {}
        tmp2 = []
        for param in request.form:
            if param.startswith("feature"):
                arr = param. split("__")
                if not tmp.get(arr[-1]):
                    tmp[arr[-1]] = {}
                tmp[arr[-1]].update({arr[0]:request.form[param]})
                #tmp["parameters"] = {}
        ss=""


@blueprint.route('/list_algorithms/', methods=['GET'])
@blueprint.route('/list_algorithms/<name>', methods=['GET'])
def list_algorithms(name=None):
    algos = get_all_available_models()
    if name:
        return algos.get(name)
    else:
        return algos
