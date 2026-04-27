'''
running the first api
breakdown of the entire code with what does what

1. We are starting by importing fastapi package
2. we create instance of a class which represents the class
3. we are defining a route using @app.get("/") decorator, this route listent to
http get requests at the root URL
4. The read_root() function is the handler for this route, when the root url is accesses
it returns a dictonary with message: {"message":"Hello,FastAPI here"}

'''

from fastapi import FastAPI

#create an instance of the FastAPI class

app = FastAPI()

#define the route
@app.get("/")
def read_root():
  return {"message":"Hello,FastAPI here"}