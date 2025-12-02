from flask import Flask

app = Flask("hello-world")

@app.route("/") 
def hello():
    print("hello world")
    return "hello"

#print(help(app.route))

@app.route("/goodbye", methods=["GET", "POST"]) 
def goodbye():
    print("goodbye world")
    return "goodbye"

def main():
    app.run()

if __name__ == "__main__":
    main()