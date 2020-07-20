from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = 'madlib'
debug = DebugToolbarExtension(app)


@app.route('/')
def home_page():
    prompts = story.prompts
    return render_template('home_questions.html', prompts=prompts)


@app.route('/story')
def madlib_story():
    text = story.generate(request.args)
    return render_template('story.html', story=text)
