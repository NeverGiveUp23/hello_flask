from flask import Flask, render_template, session  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
  if 'countdown' not in session:
      session['countdown'] = 0
      session['countdown'] += 1
  return render_template("index.html", session=['countdown']) 
  




if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.



