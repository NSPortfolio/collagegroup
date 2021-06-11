from flask.views import MethodView
from flask import Flask, render_template

app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        return render_template('index.html')

class SecondPage(MethodView):
    def get(self):
        question_page = QuestionForm()
        return render_template('second_page.html', questionpage=question_page)


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/select', view_func=SecondPage.as_view('second_page'))

app.run()
