# flask routes go here
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "supersecretkey"

debug = DebugToolbarExtension(app)


@app.route('/')
def madlib_form():
    """Generate and show form to ask for words"""
    prompts = stories.story.prompts

    return render_template('form.html', prompts=prompts)


@app.route('/story')
def story():

    text = stories.story.generate(request.args)

    return render_template('story.html', story_text=text)
