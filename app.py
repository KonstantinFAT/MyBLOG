from flask import Flask, render_template, url_for, send_file

app = Flask(__name__)

@app.route('/main')
def main():
    return render_template('Main.html')

@app.route('/articles')
def articles():
    return render_template('Menu_article.html')


    
@app.route('/Download/<name>')
def download(name):
    return send_file(name, as_attachment=True)
    
@app.route('/article1')
def article1():
    return render_template('Article1.html')
    
    
if __name__ == "__main__":
    app.run()