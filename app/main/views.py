import json
from flask import render_template, session, redirect, url_for, request, send_from_directory, jsonify, flash
from flask_login import current_user, login_required
from . import main
from datetime import datetime
from .. import db
from .forms import InputData
from ..models import tblRole, tblUser, Permission
from ..decorators import admin_required, permission_required



@main.route('/board', methods=['GET','POST'])
def index():
    """
    尚未结束的停水
    """
    return render_template('index.html')


@main.route('/add', methods=['GET','POST'])
@login_required
def addData():
    form = InputData()
    typelist = tblType.query.order_by('id').all()
    try:
        ed = datetime.strptime(form.enddate.data,'%Y-%m-%d %H:%M:%S')
    except:
        ed = None
    if request.method == 'POST':
        print(request.form.get('id'))
        if request.form.get('id'):  # 存在id，则根据id编辑记录
            print('update')
            inputdata = tblData.query.get(request.form.get('id'))
            inputdata.startdate=form.startdate.data
            inputdata.enddate = ed
            inputdata.address = form.address.data
            inputdata.area = form.area.data.replace('\r',' ').replace('\n' ,' ')
            inputdata.type_id = form.type_id.data
            inputdata.user_id = current_user.id
            flash('编辑信息成功')
        else: # id为空，则新增记录
            print('add')
            inputdata=tblData(startdate=form.startdate.data,
            enddate=ed,
            address=form.address.data,
            area=form.area.data.replace('\r',' ').replace('\n' ,' '),
            type_id=form.type_id.data,
            user_id=current_user.id)
            flash('输入信息成功')
        db.session.add(inputdata)
        return redirect(url_for('main.addData'))
    return render_template('add.html',form=form, typelist=typelist)

@main.route('/tblJSON/')
@login_required
def tblJSON():
    """
    逆序、分页查询停水信息列表，JSON格式
    """
    return '''{"code":0,"msg":"","count":%d,"data":%s}''' %(tblData.query.count(), tblData.query.order_by(db.desc(tblData.id)).offset(int(request.args.get('limit'))*(int(request.args.get('page'))-1)).limit(request.args.get('limit')).all())


@main.route('/admin')
@login_required
@admin_required
def for_admins_only():
    """
    admin管理员页面
    """
    return "For Administrator!"


@main.route('/moderator')
@login_required
@permission_required(Permission.MODERATE_COMMENTS)
def for_moderators_only():
    return "For comment moderators!"