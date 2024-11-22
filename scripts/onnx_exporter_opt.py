from pathlib import Path
from optimum.onnxruntime import ORTModelForSequenceClassification
import netron

model_name_or_path = "Alibaba-NLP/gte-multilingual-reranker-base"
revision = "4e88bd5dec38b6b9a7e623755029fc124c319d67"
model_original = ORTModelForSequenceClassification.from_pretrained(
    model_name_or_path,
    trust_remote_code=True,
    revision=revision,
)

save_path = Path("source_models/gte-reranker/onnx")
if not save_path.exists():
    save_path.mkdir(parents=True)

model_original.save_pretrained(save_path)

model_original.eval()

netron.start(save_path.joinpath("model.onnx"))
