"""
One-time script: export best.pt → best.onnx
Run this LOCALLY (where torch is installed) before deploying to Render.

Usage:
    python export_onnx.py
"""
from ultralytics import YOLO

model = YOLO("best.pt")
model.export(format="onnx", imgsz=640, simplify=True, opset=17)
print("\n✅  Exported → best.onnx  (commit this to git)")
