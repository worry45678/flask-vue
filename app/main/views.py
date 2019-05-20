import json
from . import main
from datetime import datetime
from flask import render_template, session, redirect, url_for, request, send_from_directory, jsonify, flash
from .. import db

@main.route('/', methods=['GET','POST'])
def index():
    return 'hello,world'

@main.route('/log', methods=['GET','POST'])
def test():
    devices = list(db.devices.find({},{'_id':0}))
    for i,v  in enumerate(db.devices.find({}, {'_id':0})):
        devices[i]['date'] = devices[i]['date'].strftime('%Y-%m-%d %H:%M:%S')
        if db.check_log.find_one({'id': v['id']}):
            devices[i]['isCheck'] = True
        else:
            devices[i]['isCheck'] = False
    return jsonify({'data': devices})

@main.route('/check', methods=['POST'])
def check():
    db.check_log.insert_one({'id': 1, 'date': datetime.now(), 'user': 'ww'})
    return jsonify({'message': 'ok'})
