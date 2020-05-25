from flask import Flask, jsonify, request
from flask_cors import CORS
from flaskext.mysql import MySQL
from commands.functions import *


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# MySQL

app.config['MYSQL_DATABASE_USER'] = 'admin_trbot'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Volkova2020!'
app.config['MYSQL_DATABASE_DB'] = 'admin_trbot'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL(app)

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/user', methods=['GET'])
def get_user():
    try:
        conn = mysql.connect()
        mycursor = conn.cursor()
        sql = "SELECT api_key, api_secret FROM users WHERE chat_id = 996298371"
        mycursor.execute(sql)
        result = mycursor.fetchone()
        if result == None:
            return jsonify('User does not exist')
        else:
            return jsonify(result)

    except Exception as e:
        print(e)

    finally:
        mycursor.close()
        conn.close()

@app.route('/adduser', methods=['POST'])
def add_user():
    try:
        conn = mysql.connect()
        mycursor = conn.cursor()
        login = str(request.get_json()['login'])
        password = str(request.get_json()['password'])
        chat_id = str(request.get_json()['chat_id'])
        sql = "UPDATE users set login = %s, password = %s WHERE chat_id = %s"
        val = (login, password, chat_id)
        mycursor.execute(sql, val)
        conn.commit()

        return jsonify('User update successfully')

    except Exception as e:
        print(e)

    finally:
        mycursor.close()
        conn.close()

@app.route('/deposit', methods=['GET'])
def get_user_balance():

    result = get_balance()

    return jsonify(btc=result[0],btc_frozen=result[1], eth = result[3], eth_frozen = result[4])




if __name__ == '__main__':
    app.run(host = '0.0.0.0')
