from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI()

# Define a root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, its my first API!", "status": "success"}

# Define an endpoint to read user information
@app.get("/users/{user_id}")
def read_user(user_id: int, name: str = "Guest"):
    return {"user_id": user_id,
            "name": name,
            "welcome_message": f"Welcome {name}!"
    }

# Define an endpoint to create a new user
@app.post("/users/")
def create_user(user_data: dict):
    return {
        "status": "User created",
        "received_data": user_data
    }

# Define an endpoint to update user information
@app.put("/users/{user_id}")
def update_user(user_id: int, user_data: dict):
    return {
        "status": "User updated",
        "user_id": user_id,
        "received_data": user_data
    }

# Define an endpoint to delete a user
@app.delete("/users/{user_id}")
def delete_user(user_id: int, hard_delete: bool = False):
    return {
        "status": "User deleted" if hard_delete else "User soft-deleted",
        "user_id": user_id
    }