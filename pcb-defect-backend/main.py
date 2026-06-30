import os

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import base64
import cv2
import numpy as np

from ultralytics import YOLO

# ================= APP =================
app = FastAPI(
    title="CircuitGuard AI Backend",
    description="Batch PCB Defect Detection API",
    version="1.0.0"
)
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ================= CORS =================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # tighten in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ================= MODEL LOAD =================
# Prefer ONNX (lightweight, Render-friendly) → fallback to .pt (local dev)
ONNX_PATH = "best.onnx"
PT_PATH   = "best.pt"

if os.path.exists(ONNX_PATH):
    MODEL_PATH = ONNX_PATH      # uses onnxruntime – ~60 MB RAM
else:
    MODEL_PATH = PT_PATH         # uses torch – ~800 MB RAM

model = YOLO(MODEL_PATH)
class_names = model.names

CONFIDENCE = 0.25
IOU = 0.45


# ================= HEALTH CHECK =================
@app.get("/")
def root():
    return {"status": "CircuitGuard AI backend running"}


# ================= BATCH DETECTION =================
@app.post("/detect-batch")
async def detect_batch(
    files: List[UploadFile] = File(...)
):
    results_payload = []

    for file in files:
        contents = await file.read()

        # -------- decode image --------
        np_img = np.frombuffer(contents, np.uint8)
        img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

        if img is None:
            continue

        # -------- inference --------
        results = model.predict(
            img,
            conf=CONFIDENCE,
            iou=IOU,
            verbose=False
        )
        r = results[0]

        detections = []

        if r.boxes is not None:
            for box in r.boxes:
                x1, y1, x2, y2 = box.xyxy[0].tolist()

                detections.append({
                    "class_name": class_names[int(box.cls[0])],
                    "confidence": round(float(box.conf[0]), 4),
                    "bbox": [
                        round(float(x1), 1),
                        round(float(y1), 1),
                        round(float(x2), 1),
                        round(float(y2), 1),
                    ]
                })

        # -------- annotated image --------
        annotated_img = r.plot()   # BGR
        _, buffer = cv2.imencode(".png", annotated_img)
        encoded_img = base64.b64encode(buffer).decode("utf-8")

        results_payload.append({
            "filename": file.filename,
            "annotated_image": encoded_img,
            "detections": detections
        })

    return results_payload


# ================= ENTRY POINT =================
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)

