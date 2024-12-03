import onnx
import os

def extract_onnx_model(input_path, output_path):
   
   input_names = ["images"]
   output_names = [
       "/model.23/Concat_output_0",
       "/model.23/Concat_1_output_0", 
       "/model.23/Concat_2_output_0"
   ]

   onnx.utils.extract_model(input_path, output_path, input_names, output_names)

# Usage
os.chdir('./model')
extract_onnx_model("yolo11n.onnx", "yolo11n-cut.onnx")
extract_onnx_model("yolo11s.onnx", "yolo11s-cut.onnx")
extract_onnx_model("yolo11m.onnx", "yolo11m-cut.onnx")



