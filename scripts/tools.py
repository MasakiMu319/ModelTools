from pathlib import Path
from transformers import AutoModel, AutoTokenizer

model_name_or_path = Path("./Conan-embedding/")
tokenizer = AutoTokenizer.from_pretrained(
    model_name_or_path, trust_remote_code=True, local_files_only=True
)
model = AutoModel.from_pretrained(
    model_name_or_path,
    trust_remote_code=True,
    local_files_only=True,
)
tokenized_input = tokenizer(
    ["This is an input test text"],
    return_tensors="pt",
)

input_names = tokenizer.model_input_names
print(f"{input_names=}")
# output_names = model.output_names
# input_axes = model.input_axes
# output_axes = model.output_axes
# print(f"{input_names=}\n {output_names=}\n {input_axes=}\n {output_axes=}")
