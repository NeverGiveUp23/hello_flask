from flask import Flask, render_template  # Import Flask to allow us to create our app



app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/play/<int:num>/<string:color>')          # The "@" decorator associates this route with the function immediately following
def boxes(num,color):
  return render_template("index.html", num = num,color = color ) 
  

@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
  users_info = [
    {'first_name' : 'Michael', 'last_name' : 'Jordan', 'full_name' : 'Micheal Jordan'},
    {'first_name' : 'John', 'last_name' : 'Supsupin', 'full_name' : 'John Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen', 'full_name' : 'Mark Guillen '},
    {'first_name' : 'KB', 'last_name' : 'Tonel', 'full_name' : 'KB Tonel'}
]
  return render_template("lists.html", users = users_info)



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.



