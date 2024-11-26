from pathlib import Path
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import netron


# model name or ID in hugging face.
model_name_or_path = Path("./Conan-embedding/")
# where to save the model.
save_path = model_name_or_path.joinpath("onnx")


# load the model and tokenizer.
tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
model = AutoModelForSequenceClassification.from_pretrained(
    model_name_or_path,
    # we need to trust the remote code to export the model.
    trust_remote_code=True,
    # identify the output data type of the model.
    local_files_only=True,
)

if not save_path.exists():
    save_path.mkdir(parents=True)

# dummy input data for the model.
model_input = tokenizer(
    "This is an input test text",
    return_tensors="pt",
)
print(f"Input: {model_input}")
input_names = [key for key in model_input.keys()]

dynamic_axes = {name: {0: "batch_size", 1: "sequence"} for name in input_names}

model_output = model(**model_input)
output_names = [
    key
    for key in list(model_output.__dict__.keys())
    if model_output.__dict__[key] is not None
]
print(f"Output names: {output_names}")
for key in output_names:
    dynamic_axes[key] = {0: "batch_size", 1: "sequence"}

result = torch.onnx.export(
    model=model,
    args=tuple(model_input.values()),
    f=save_path.joinpath("model.onnx"),
    input_names=list(model_input.keys()),
    output_names=output_names,
    opset_version=17,
    dynamic_axes=dynamic_axes,
    verbose=True,
    verify=True,
    profile=True,
    report=True,
)

print(f"Model saved at: {save_path}")
tokenizer.save_pretrained(f"{save_path}")

# visualize the model.
netron.start(f"{save_path.joinpath("model.onnx")}")
