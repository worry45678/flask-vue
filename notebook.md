
### 学习内容

* 装饰器的定义和使用

1. flask通用
    1. 注册蓝本以及路由前缀 `app.register_blueprint(auth_blueprint, url_prefix='/auth')`
    2. app上下文管理器 main/__init__.py
    即可在templates模板中调用该常量
    ```
    # 用于模板中调用Permission
    @main.app_context_processor
    def inject_permissions():
    return dict(Permission=Permission)
    ```
    3. jinja2模板的include方法
    `{% include '_posts.html' %}`直接应用_posts.html中的内容
    
2. flask_login 管理已登陆用户的用户会话
    1. `from flask_login import UserMixin`用户模型实现方法  
        `class User(UserMixin,db.Model)`
    2. `from flask_login import LoginManger`登陆管理app/__init__.py:
        ```
        login_manager = LoginManager()
        login_manager.session_protection = 'strong' # 保护强度
        login_manager.login_view = 'auth.login' # 登陆页面的端点
        ```
        要求实现回调函数，如下app/models.py：
        ```
        from . import login_manager

        @login_manager.user_loader
        def load_user(user_id):
            return User.query.get(int(user_id))
        ```
    3. 保护路由，未登陆用户返回login页面
        ```
        from flask.ext.login import login_required
        @app.route('/secret')
        @login_required
        def secret():
            return 'Only authenticated users are allowed!'
        ```
    4. jinja模板中可以使用*current_user* 来调用当前用户的对象，*current_user.is_authenticated*用来验证是否登陆成功
    5. 登录，登出用户
        ```from flask_login imort login_user,logout_user,login_required
        login_user(user, remember_me=True) # 以用户对象user登陆
        logout_user() # 登出当前用户
        ```
    6. 数据模式之间的关系
        current_user._get_current_object() 获取当前用户的真正对象
        创建数据库对象的实例时，可以直接用关系数据库的实例带入创建的对象中。参见blogs.py的blogs()代码。
    7. 分页显示
        `Post.query.order_by(Post.timestamp.desc()).paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'], error_out=False)`

3. werkzeug 计算密码散列值并进行核对
    1. `generate_password_hash(password, method=pbkdf2:sha1, salt_length=8)` **返回密码的散列值**
    2. `check_password_hash(hash, password)` 比较散列值和输入的密码，正确则返回True
    3. 用户模型中添加验证方法：  
    ```
    from werkzeug.security import generate_password_hash,check_password_hash, class User(db.Model):

    password_hash = db.Column(db.String(128))
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
        def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    ```
4. javascript
    1. [解决ie缓存的问题](https://www.cnblogs.com/artech/archive/2013/01/03/cache-4-ie.html)  
     `$.ajaxSetup({ cache: false }); `