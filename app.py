# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import argparse
import pymysql
import config
DEFAULT_PORT = 5001
DEFAULT_HOST = '0.0.0.0'


def parse_args():
    parser = argparse.ArgumentParser(description='Tensorflow object detection API')

    parser.add_argument('--debug', dest='debug',
                        help='Run in debug mode.',
                        required=False, action='store_true', default=True)

    parser.add_argument('--port', dest='port',
                        help='Port to run on.', type=int,
                        required=False, default=DEFAULT_PORT)

    parser.add_argument('--host', dest='host',
                        help='Host to run on, set to 0.0.0.0 for remote access', type=str,
                        required=False, default=DEFAULT_HOST)

    args = parser.parse_args()
    return args



app = Flask(__name__)

db = pymysql.connect(host=config.DATABASE_CONFIG['host'], port=3306, user=config.DATABASE_CONFIG['user'], passwd=config.DATABASE_CONFIG['passwd'], db=config.DATABASE_CONFIG['db'], charset="utf8")
cur = db.cursor()
sql = "SELECT cnumber from zcompany"
cur.execute(sql)

data_list = cur.fetchall()

print(data_list[0][0])
print(data_list[1])
print(data_list[2])
print(data_list[3])

@app.route('/')
def main():
    return render_template('main.html')


#디텍션 처리
@app.route('/upload_process', methods=['POST'])
def upload_process():
    value = request.form['text']
    print(value)
    return render_template("upload.html",value=value,data_list=data_list)



if __name__ == "__main__":
    args = parse_args()
    app.run(host=args.host, port=args.port, debug=args.debug)