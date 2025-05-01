from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Função para carregar o config.json
def carregar_config():
    with open('config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

# Função para salvar o config.json
def salvar_config(config):
    with open('config.json', 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4, ensure_ascii=False)

@app.route('/', methods=['GET', 'POST'])
def painel():
    config = carregar_config()

    if request.method == 'POST':
        origem = request.form.get('origem')
        destino = request.form.get('destino')
        link_original = request.form.get('link_original')
        link_afiliado = request.form.get('link_afiliado')

        if origem and destino:
            config['clone_pairs'][origem] = destino
        if link_original and link_afiliado:
            config['link_replacements'][link_original] = link_afiliado

        salvar_config(config)
        return redirect(url_for('painel'))

    return render_template('index.html', config=config)

@app.route('/delete_channel/<canal_origem>')
def delete_channel(canal_origem):
    config = carregar_config()
    if canal_origem in config['clone_pairs']:
        del config['clone_pairs'][canal_origem]
        salvar_config(config)
    return redirect(url_for('painel'))

@app.route('/delete_link/<link_original>')
def delete_link(link_original):
    config = carregar_config()
    if link_original in config['link_replacements']:
        del config['link_replacements'][link_original]
        salvar_config(config)
    return redirect(url_for('painel'))

if __name__ == '__main__':
    app.run(debug=True)
