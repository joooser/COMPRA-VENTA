from application import init_app
from config import config


if __name__ == '__main__':
    configuration = config['development']
    app = init_app(configuration)
    app.run()