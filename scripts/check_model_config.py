import onnxruntime as ort
from transformers import AutoTokenizer


tokenizer = AutoTokenizer.from_pretrained(
    "./Conan-embedding/",
    trusgt_remote_code=True,
    local_files_only=True,
)

max_length = 9

inputs = tokenizer(
    ["你好北京"],
    return_tensors="np",
)
print(inputs)

ort_session = ort.InferenceSession(
    path_or_bytes="./Conan-embedding/onnx/model.onnx",
    providers=["CPUExecutionProvider"],
)

outputs = ort_session.run(
    ["last_hidden_state"],
    dict(inputs),
)

print(outputs)
