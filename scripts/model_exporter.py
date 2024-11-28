from os import PathLike
from pathlib import Path
from torch import onnx
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers.models.auto.auto_factory import _BaseAutoModelClass
import netron


class ONNXExporter:
    def __init__(self, model: _BaseAutoModelClass, tokenizer: AutoTokenizer):
        self.model = model
        self.tokenizer = tokenizer

    @property
    def dummy_input(self):
        return self.tokenizer(
            "This is a dummy input text",
            return_tensors="pt",
        )

    @property
    def model_output(self):
        return self.model(**self.dummy_input)

    @property
    def input_names(self):
        return self.tokenizer.model_input_names

    @property
    def output_names(self):
        output_dict = self.model_output.__dict__
        return [key for key in list(output_dict.keys()) if output_dict[key] is not None]

    @property
    def input_axes(self):
        dynamic_axes = {}
        for name in self.input_names:
            dynamic_axes[name] = {0: "batch_size", 1: "sequence"}
        return dynamic_axes

    @property
    def output_axes(self):
        dynamic_axes = {}
        for name in self.output_names:
            dynamic_axes[name] = {0: "batch_size"}
        return dynamic_axes

    def export(self, save_path: str | PathLike):
        save_path = Path(save_path) if isinstance(save_path, str) else save_path
        if not save_path.exists():
            save_path.mkdir(parents=True)

        self.model.eval()

        return onnx.export(
            model=self.model,
            args=tuple(self.dummy_input.values()),
            f=save_path.joinpath("model.onnx"),
            input_names=self.input_names,
            output_names=self.output_names,
            dynamic_axes=self.input_axes | self.output_axes,
            opset_version=19,
            verbose=True,
            verify=True,
        )

    def save_tokenizer(self, save_path: str | PathLike):
        save_path = Path(save_path) if isinstance(save_path, str) else save_path

        if not save_path.exists():
            save_path.mkdir(parents=True)

        self.tokenizer.save_pretrained(save_path)


if __name__ == "__main__":
    model_name_or_path = Path("./source_models/gte-multilingual-base")
    save_path = model_name_or_path.joinpath("onnx")
    model = AutoModelForTokenClassification.from_pretrained(
        model_name_or_path,
        trust_remote_code=True,
        local_files_only=True,
    )
    tokenizer = AutoTokenizer.from_pretrained(
        model_name_or_path,
        trust_remote_code=True,
        local_files_only=True,
    )
    onnx_exporter = ONNXExporter(model=model, tokenizer=tokenizer)

    onnx_result = onnx_exporter.export(save_path=save_path)
    onnx_exporter.save_tokenizer(save_path=save_path)

    netron.start(str(save_path.joinpath("model.onnx")))
