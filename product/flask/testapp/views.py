from testapp import app
from flask import render_template  # 追加

@app.route('/')
def index():
    my_dict = {
        'insert_something1': 'safariのブラウザを使用していると、音が鳴らないことがあります。',
        'insert_something2': 'safariのwebサイトの自動再生設定を「すべてのメディアを自動設定」にすると直ります。',
        #'test_titles': ['title1', 'title2', 'title3']
    }
    return render_template('testapp/index.html', my_dict=my_dict)

@app.route('/test')
def other1():
    return render_template('testapp/index2.html')


