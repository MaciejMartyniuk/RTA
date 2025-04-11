from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

@app.get("/api/v1.0/predict")
def predict(x: Optional[float] = Query(0), y: Optional[float] = Query(0)):
    x = x or 0
    y = y or 0
    total = x + y
    prediction = 1 if total > 5.8 else 0
    return {
        "features": {"x": x, "y": y, "sum": total},
        "prediction": prediction
    }
