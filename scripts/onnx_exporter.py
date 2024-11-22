from pathlib import Path
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import netron

model_name_or_path = "Alibaba-NLP/gte-multilingual-reranker-base"
revision = "4e88bd5dec38b6b9a7e623755029fc124c319d67"

tokenizer_original = AutoTokenizer.from_pretrained(model_name_or_path)
model_original = AutoModelForSequenceClassification.from_pretrained(
    model_name_or_path,
    trust_remote_code=True,
    # torch_dtype=torch.float32,
    revision=revision,
)
model_original = model_original.float()

save_path = Path("./source_models/gte-reranker/onnx")

if not save_path.exists():
    save_path.mkdir(parents=True)
dummy_model_input = tokenizer_original(
    "This is a test for ONNX Runtime!", return_tensors="pt"
)

model_original.eval()

result = torch.onnx.export(
    model_original,
    tuple(dummy_model_input.values()),
    f=f"{save_path}/model.onnx",
    input_names=["input_ids", "attention_mask"],
    output_names=["logits"],
    dynamic_axes={
        "input_ids": {0: "batch_size", 1: "sequence"},
        "attention_mask": {0: "batch_size", 1: "sequence"},
        "logits": {0: "batch_size", 1: "sequence"},
    },
    do_constant_folding=True,
    opset_version=17,
    verbose=True,
)
# let's also save the tokenizer

tokenizer_original.save_pretrained(f"{save_path}")

netron.start(f"{save_path.joinpath("model.onnx")}")
