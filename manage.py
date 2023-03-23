from flaskr import create_app


if __name__=="__main__":
    app = create_app()
    # db.create_all()
    app.run(debug=True)