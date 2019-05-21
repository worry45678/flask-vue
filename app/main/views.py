import json
from . import main
from datetime import datetime
from flask import render_template, session, redirect, url_for, request, send_from_directory, jsonify, flash, request
from .. import mongo

@main.route('/', methods=['GET','POST'])
def index():
    return 'hello,world'

@main.route('/log', methods=['GET','POST'])
def test():
    devices = list(mongo.db.devices.find({},{'_id':0}))
    now = datetime.now()
    for i,v  in enumerate(mongo.db.devices.find({}, {'_id':0})):
        if mongo.db.check_log.find_one({'id': v['id'],'date':{'$gt': datetime(now.year, now.month, now.day)}}):
            devices[i]['isCheck'] = True
            devices[i]['date'] = mongo.db.check_log.find_one({'id': v['id'],'date':{'$gt': datetime(now.year, now.month, now.day)}})['date'].strftime('%H:%M')
        else:
            devices[i]['isCheck'] = False
            devices[i]['date'] = '待检查'
    return jsonify({'data': devices})

@main.route('/check', methods=['POST'])
def check():
    params = json.loads(request.data.decode('utf-8'))
    id = params['id']
    print(id)
    mongo.db.check_log.insert_one({'id': int(id), 'date': datetime.now(), 'user': 'ww'})
    return jsonify({'message': 'ok'})
