from flask import Flask
from app.lib.biblioteca_gastronomie import descriere_cordon_bleu, origine_cordon_bleu

app = Flask(__name__)


@app.route('/gastronomie')
def gastronomie():
    return '''
    <html>
    <head><title>Gastronomie</title></head>
    <body>
        <h1>Bine ai venit la pagina de Gastronomie!</h1>
        <p>Alege un preparat:</p>
        <ul>
            <li><a href="/cordon_bleu">Cordon Bleu</a></li>
        </ul>
    </body>
    </html>
    '''


@app.route('/cordon_bleu')
def cordon_bleu():
    return '''
    <html>
    <head><title>Cordon Bleu</title></head>
    <body>
        <h1>Cordon Bleu</h1>
        <p>Afla mai multe despre acest preparat:</p>
        <ul>
            <li><a href="/cordon_bleu/descriere">Descriere</a></li>
            <li><a href="/cordon_bleu/origine">Origine</a></li>
        </ul>
        <br>
        <a href="/gastronomie">Inapoi la Gastronomie</a>
    </body>
    </html>
    '''


@app.route('/cordon_bleu/descriere')
def descriere():
    return '''
    <html>
    <head><title>Descriere Cordon Bleu</title></head>
    <body>
        <h1>Descriere Cordon Bleu</h1>
        <p>''' + descriere_cordon_bleu() + '''</p>
        <br>
        <a href="/cordon_bleu">Inapoi la Cordon Bleu</a> |
        <a href="/cordon_bleu/origine">Vezi Origine</a> |
        <a href="/gastronomie">Inapoi la Gastronomie</a>
    </body>
    </html>
    '''


@app.route('/cordon_bleu/origine')
def origine():
    return '''
    <html>
    <head><title>Origine Cordon Bleu</title></head>
    <body>
        <h1>Origine Cordon Bleu</h1>
        <p>''' + origine_cordon_bleu() + '''</p>
        <br>
        <a href="/cordon_bleu">Inapoi la Cordon Bleu</a> |
        <a href="/cordon_bleu/descriere">Vezi Descriere</a> |
        <a href="/gastronomie">Inapoi la Gastronomie</a>
    </body>
    </html>
    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
