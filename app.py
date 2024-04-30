from flask import Flask

from routers.routers import router
from routers.project_routers import router as project

app = Flask(__name__)


app.register_blueprint(router)
app.register_blueprint(project)


if __name__ == '__main__':
    app.run()
