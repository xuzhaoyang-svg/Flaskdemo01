from flask import Flask

# 使用flask类创建一个APP对象
# __name__：代表当前app.py这个模块
# __name__作用：1.出现bug，可以帮助我们快速定位；2.对于寻找模板文件，有一个相对路径
app = Flask(__name__)

# 创建一个路由和视图函数映射
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

# 1. debug模式（热部署）
# 1.1 开启debug模式后，只要修改代码后保存，就会自动重新加载，不需要手动重启项目
# 1.2 可以直接在浏览器上看到bug信息

# 2. 修改host
# 让局域网中其他设备访问到项目

# 3. 修改端口号
# 如果5000端口被占用可以修改用其他端口


if __name__ == '__main__':
    app.run(debug=True)
