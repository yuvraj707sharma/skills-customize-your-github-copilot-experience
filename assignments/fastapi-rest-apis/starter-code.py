from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

# Initialize FastAPI application
app = FastAPI(title="Item Management API")

# Define data models
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

# In-memory data storage
items_db = {}
next_item_id = 1

# TODO: Implement GET endpoint for root path
# Should return a welcome message

# TODO: Implement POST endpoint to create items
# Should accept Item data and store it with an auto-incremented ID

# TODO: Implement GET endpoint to retrieve all items
# Should return a list of all stored items

# TODO: Implement GET endpoint to retrieve a specific item by ID
# Should return 404 if item not found

# TODO: Implement PUT endpoint to update an item
# Should update existing item data or return 404

# TODO: Implement DELETE endpoint to remove an item
# Should delete the item or return 404

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
