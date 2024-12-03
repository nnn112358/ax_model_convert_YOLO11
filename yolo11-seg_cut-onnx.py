import onnx
import os

def extract_onnx_model(input_path, output_path):
   
	input_names = ["images"]
	output_names = [
		"/model.23/Concat_1_output_0",
		"/model.23/Concat_2_output_0", 
		"/model.23/Concat_3_output_0",
		"/model.23/cv4.0/cv4.0.2/Conv_output_0",
		"/model.23/cv4.1/cv4.1.2/Conv_output_0",
		"/model.23/cv4.2/cv4.2.2/Conv_output_0",
		"output1"
	]

	onnx.utils.extract_model(input_path, output_path, input_names, output_names)

# Usage
os.chdir('./model')
extract_onnx_model("yolo11n-seg.onnx", "yolo11n-seg-cut.onnx")
extract_onnx_model("yolo11s-seg.onnx", "yolo11s-seg-cut.onnx")
extract_onnx_model("yolo11m-seg.onnx", "yolo11m-seg-cut.onnx")



