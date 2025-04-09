# FastAPI se import kar rahe hain, taaki hum API bana sakein
from fastapi import FastAPI # type: ignore
from pydantic import BaseModel # type: ignore # request validation ke liye

# FastAPI ka ek instance bana rahe hain
app = FastAPI()


names = ["Ali", "Bilal", "Usman"]

# Yeh ek GET request ka endpoint define kar raha hai jo root ("/") pe chalega
@app.get("/")
def get_function():  # Ek function define kiya jo execute hoga jab yeh endpoint hit hoga
   
    return names  # Yeh function ek JSON response return karega


class Data(BaseModel):  
    name: str          
    age: int          

@app.post("/data")                    # URL
def add_data(data: Data):             # URL par jane se ye function chal jaye ga.
    
    return {
      "message" : f"Data received: Name: {data.name}, Age: {data.age}"
  } # Json Object
    
    
@app.delete("/data/{item_id}")  # Item ko delete karne ka endpoint
def delete_data(item_id: int):
  
    return {"message": f"Item with ID {item_id} deleted successfully"}


@app.put("/data/{item_id}")
def update_data(item_id: int, data: Data):
 
    return {
      "message": f"Item with ID {item_id} updated to Name: {data.name}, Age: {data.age}"
  }   
