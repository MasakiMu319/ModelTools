from pathlib import Path
from optimum.onnxruntime import ORTModelForFeatureExtraction
import netron

model_name_or_path = "TencentBAC/Conan-embedding-v1"
model_original = ORTModelForFeatureExtraction.from_pretrained(
    model_name_or_path,
    trust_remote_code=True,
    export=True,
    provider="CPUExecutionProvider",
)

save_path = Path("source_models/conan-embedding/onnx")
if not save_path.exists():
    save_path.mkdir(parents=True)

model_original.save_pretrained(save_path)

netron.start(f"{save_path.joinpath("model.onnx")}")
