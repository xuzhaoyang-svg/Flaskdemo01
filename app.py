from flask import Flask

# 使用flask类创建一个APP对象
# __name__：代表当前app.py这个模块
# __name__作用：1.出现bug，可以帮助我们快速定位；2.对于寻找模板文件，有一个相对路径
app = Flask(__name__)

# 创建一个路由和视图函数映射
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
