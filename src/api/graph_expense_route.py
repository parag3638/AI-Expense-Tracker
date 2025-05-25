from fastapi import APIRouter, File, UploadFile, HTTPException
import shutil
import os
import uuid
from src.chain.graphstate import graph

router = APIRouter()

@router.post("/expenses/upload-graph")
async def upload_expense_via_graph(file: UploadFile = File(...)):
    try:
        # Save uploaded image to a temporary file
        temp_dir = "/tmp"
        os.makedirs(temp_dir, exist_ok=True)
        temp_path = os.path.join(temp_dir, f"{uuid.uuid4().hex}.jpg")
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Define initial graph state
        initial_state = {
            "image_location": temp_path
        }

        # Invoke LangGraph pipeline
        result = graph.invoke(initial_state)

        return {"status": "success", "data": result}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
