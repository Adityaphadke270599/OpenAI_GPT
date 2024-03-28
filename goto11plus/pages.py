from flask import Blueprint, redirect, render_template, request, url_for
from goto11plus.gpt_api import callGPT
import json
from flask import Flask, jsonify, request

bp = Blueprint("pages", __name__)


@bp.route("/",methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return redirect("/essay")
    return render_template("pages/home.html")

@bp.route("/about")
def about():
    return render_template("pages/about.html")

@bp.route('/essay', methods=['GET', 'POST'])
def essay():
    question = None
    if request.method == 'POST':
        # Process the submitted form data
        answer = request.form['essay_content']
        question = request.form['essay_question']
        print("log : answer --- "+ answer)
        print("log : question --- "+question)
        if(question is not None):
            analysis = callGPT.getAnalysis(question,answer)
            return render_template('results.html', analysis=analysis)
        # Do something with the answer, like saving it to a database
    else:
        question = callGPT.getQuestion()
   
    return render_template('essay_form.html',question=question)

@bp.route('/submit', methods=['POST'])
def submit_essay():
    essay_content = request.form['essay_content']
    
    # Let's assume 'analysis' is the string you received from OpenAI
    analysis = "The analysis received from OpenAI goes here"

    # Pass the analysis string to the results template
    return render_template('results.html', analysis=analysis)


@bp.route('/getWizard', methods=['GET'])
def getQuestion():
    response={}
    question = callGPT.getQuestion()
    if(question != ''):
        response['question']= question
    return jsonify(response), 200

@bp.route('/getWizardReport', methods=['POST'])
def getWizardReport():
    userData = request.json
    response={}
    userAnswer = userData['userAnswer']
    question = userData['question']
    print("log : answer --- "+ userAnswer)
    print("log : question --- "+question)
    if((question is not None) and (userAnswer is not None)):
        response['analysis'] = callGPT.getAnalysis(question,userAnswer)
    
    return jsonify(response), 200

