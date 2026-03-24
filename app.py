from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    """主頁面路由，返回 Hello 頁面"""
    return render_template('index.html')

@app.route('/api/hello')
def api_hello():
    """API 路由，返回 JSON 格式的 Hello 訊息"""
    return {'message': 'Hello from oden!', 'status': 'success'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)