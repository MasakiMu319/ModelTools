import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_path = "source_models/reader-lm-0.5b"


model_original = AutoModelForCausalLM.from_pretrained(
    model_path, trust_remote_code=True
)
tokenizer_original = AutoTokenizer.from_pretrained(model_path)


save_path = "source_models/reader-lm-0.5b/onnx"
dummy_model_input = tokenizer_original(
    "This is a test for ONNX Runtime!", return_tensors="pt"
)

model_original.eval()

result = torch.onnx.export(
    model_original,
    tuple(dummy_model_input.values()),
    f"{save_path}/model.onnx",
    output_names=["logits", "last_hidden_state"],
    dynamic_axes={
        "input_ids": {0: "batch_size", 1: "sequence"},
        "attention_mask": {0: "batch_size", 1: "sequence"},
        "logits": {0: "batch_size", 1: "sequence"},
        "last_hidden_state": {0: "batch_size", 1: "sequence"},
    },
    do_constant_folding=True,
    opset_version=17,
    verbose=True,
)
# let's also save the tokenizer

tokenizer_original.save_pretrained(f"{save_path}")
