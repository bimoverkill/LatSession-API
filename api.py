from api import app


if __name__ == "__main__":
    app.debug = True
    app.env = "development"
    app.run()