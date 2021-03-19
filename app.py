from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
try:
    import sqlite3
except:
    from pysqlite2 import dbapi2 as sqlite3
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

conn = sqlite3.connect("validator.db",check_same_thread=False)
cursor = conn.cursor()


app = Flask(__name__)



app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response



@app.route("/",methods=["POST"])
def index_post():

        nome = request.form.get('nome')
        matricula = str(request.form.get('matricula'))
        funcao = request.form.get('funcao')

        try:
            cursor.execute("SELECT * FROM colaboradores WHERE matricula = ? ", (matricula,))
            data = cursor.fetchone()

            if data == None:
                try:
                    cursor.execute("INSERT INTO colaboradores(matricula,nome,funcao) VALUES(?,?,?)", (matricula,nome,funcao))
                    conn.commit()

                    print('SUCESSO') #INSERIDO COM SUCESSO
                    return render_template('index.html')
                except ValueError:
                    print('ERRO AO INSERIR NO BD',ValueError) #ERRO AO INSERIR NO BD
                    return render_template('index.html')
            else:
                print('DUPLICADO') #ERRO MATRICULA DUPLICADA
                return render_template('index.html')
        except (ValueError):
            print('ERRO AO PESQUISAR DUPLICIDADE NO BANCO') #ERRO AO PESQUISAR DUPLICIDADE
            return render_template('index.html')







@app.route("/",methods=["GET"])
def index_get():

    return render_template('index.html')


@app.route("/scan",methods=["GET", "POST"])
def scan():



    if request.method == "POST":
        scan = str(request.form.get("scan"))
        equipe = request.form.get("equipe")
        equipe = equipe.upper()
        scan =  scan.upper()
        print(equipe)


        cursor.execute("SELECT * FROM equipes WHERE nome = ? ", (scan,))
        data = cursor.fetchone()

        print(equipe)

        if data == None:

            try:
                cursor.execute("SELECT * FROM veiculos WHERE ordem = ? ", (scan,))
                data = cursor.fetchone()
                print('passo 1')
                if data == None:
                    print('passo 2')
                    try:
                        print('passo 3')
                        cursor.execute("SELECT * FROM colaboradores WHERE matricula = ? ", (scan,))
                        colab = cursor.fetchone()
                        print('passo 4')


                        if colab == None:
                            print("ERRO NÃO COLABORADOR")
                            return render_template('scan.html',equipe=equipe)


                        else:
                            matricula = colab[1]
                            nome = colab[2]
                            funcao = colab[3]

                            print(matricula,nome,funcao,equipe)


                            #cadastrar na composição
                            try:
                                cursor.execute("INSERT INTO composicao(matricula, nome, funcao,equipe) VALUES(?,?,?,?)",(matricula, nome, funcao, equipe))
                                print('passo 5')
                                conn.commit()
                                cursor.execute("SELECT * FROM composicao WHERE matricula = ? ", (matricula,))
                                data = cursor.fetchone()
                            except:
                                print('ERRO AO INSERIR NA COMPOSIÇÃO')
                                return render_template('scan.html',equipe=equipe)


                            return render_template('scan.html', matricula=matricula,data=data[5], nome=nome, funcao=funcao,equipe=equipe)


                    except (ValueError):
                        print("NÃO É UM COLABORADOR")
                        return render_template('scan.html',equipe=equipe)
                else:

                    placa = data[1]
                    ordem = data[2]
                    tipo = data[3]
                    print(placa,ordem,tipo,equipe)


                    #cadastrar na composição
                    cursor.execute("INSERT INTO composicao(matricula, nome, funcao,equipe) VALUES(?,?,?,?)",(ordem, placa, tipo, equipe,))
                    print('passo 5.2')
                    conn.commit()
                    cursor.execute("SELECT * FROM composicao WHERE matricula = ? ", (ordem,))
                    data = cursor.fetchone()

                return render_template('scan.html',placa=placa,ordem=ordem,data=data[5],tipo=tipo,equipe=equipe)

            except:
                return render_template('scan.html',equipe=equipe)


        else:
            equipe = data[1]
            return render_template('scan.html',equipe=equipe)

    else:
        return render_template('scan.html') #PRIMEIRO ACESSO





@app.route("/veiculo",methods=["GET","POST"])
def veiculo():


    if request.method == "POST":
        placa = request.form.get('placa')
        ordem = str(request.form.get('ordem'))
        tipo = request.form.get('tipo')
        placa = placa.upper()
        tipo = tipo.upper()

        try:
            cursor.execute("SELECT * FROM veiculos WHERE ordem = ? ", (ordem,))
            data = cursor.fetchone()

            if data == None:
                try:
                    cursor.execute("INSERT INTO veiculos(placa,ordem,tipo) VALUES(?,?,?)", (placa,ordem,tipo))
                    conn.commit()
                    print('SUCESSO') #INSERIDO COM SUCESSO
                    return render_template('veiculo.html')
                except ValueError:
                    print('ERRO AO INSERIR NO BD',ValueError) #ERRO AO INSERIR NO BD
                    return render_template('veiculo.html')
            else:
                print('DUPLICADO') #ERRO MATRICULA DUPLICADA
                return render_template('veiculo.html')
        except (ValueError):
            print('ERRO AO PESQUISAR DUPLICIDADE NO BANCO') #ERRO AO PESQUISAR DUPLICIDADE
            return render_template('veiculo.html')
    else:
        return render_template('veiculo.html')







@app.route("/composicao",methods=["GET","POST"])
def composity():

    render_template("composicao.html", composicao='')

    rows = cursor.execute("SELECT * FROM composicao ORDER BY data DESC LIMIT 10")
    composicao = []
    for row in rows:
        colaborador = row

        composicao.append(colaborador)
    return render_template("composicao.html", composicao=composicao)






app.debug = True #Uncomment to enable debugging
app.run() #Run the Server
conn.commit()
"""if __name__ == '__main__':"""
