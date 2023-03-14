from fastapi import FastAPI, Response
from Model.User import User

app = FastAPI()

users = []

@app.get("/users")
def getUsers():
    return users


@app.post("/users")
def addUser(user: User, response: Response):
    users.append(user)
    response.status_code = 200
    return user

@app.get("/users/{user_id}")
def getUser(user_id: int, response: Response):
    for user in users:
        if user.id == user_id:
            response.status_code = 200
            return user
    response.status_code = 404
    return {"error": "User not found"}


@app.delete("/users/{user_id}")
def deleteUser(user_id: int, response: Response):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            response.status_code = 200
            return {"message": "User deleted"}
    response.status_code = 404
    return {"error": "User not found"}