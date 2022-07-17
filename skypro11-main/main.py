from os import abort

from flask import Flask, render_template
import utils

app = Flask(__name__, template_folder='template')

@app.route("/")
def list_candidates():
    """ Главная страница приложения """
    candidate = utils.load_candidates_from_json("candidates.json")
    return render_template('index.html', candidates=candidate)

@app.route("/candidate/<int:candidate_id>")
def page_candidates(candidate_id):
    """ Страница одного кандидата """
    candidate = utils.get_candidate(candidate_id)
    if candidate:
        return render_template('card.html', candidates=candidate)
    else:
        abort(404)

@app.route("/skill/<string:skill_name>")
def get_candidates_by_skill(skill_name):
    """ Поиск кандидата по скиллу """
    candidate = utils.get_candidates_by_skill(skill_name)
    return render_template('skill.html', candidates=candidate, candidates_count=len(candidate))

@app.route('/search/<string:candidate_name>')
def get_candidates_by_name(candidate_name):
    """ Поиск кандидата по имени """
    candidate = utils.get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidate, candidates_count=len(candidate))

app.run()

