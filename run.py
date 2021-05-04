# press on '+' next to "1:powershell" (Terminal)
# $env:FLASK_APP = "run.py"
# python -m flask run

from forum import app

if __name__ == "__main__":
    app.run()
