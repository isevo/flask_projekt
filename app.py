from flask import Flask, redirect, url_for, render_template, request,abort,make_response
app=Flask(__name__,static_url_path='')



@app.route("/")
def index():
   resp = make_response("Cookies")
   resp.set_cookie("flavor", "chocolate chip")
   author="YELLOWSTONE"
   return render_template("index.html",author=author)


@app.route("/about/")
def about():
   return render_template("about.html")

@app.route('/result',methods = ['POST', 'GET'])
def result():
   author="YELLOWSTONE"
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result) 

@app.route("/login")
def login():
   return render_template("login.html")    



@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500




if __name__ == "__main__":
    app.run(debug=True)


       
