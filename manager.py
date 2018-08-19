"""
    Created by ZZXUN on 2018/8/6
"""

from app import create_app

__author__ = "ZZXUN"

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81, threaded=True)
