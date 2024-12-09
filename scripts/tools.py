#!/usr/bin/env python3

from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("stabilityai/stablelm-2-1_6b")
model = AutoModelForCausalLM.from_pretrained(
    "stabilityai/stablelm-2-1_6b",
    torch_dtype="auto",
)

model.cpu()
inputs = tokenizer(
    """
给定一个句子，描述用户在询问什么。
句子：“每天早上7点设置一个闹钟”
描述：用户在询问每天早上7点设置一个闹钟
句子：“你能给我展示一下制作巧克力曲奇饼干的分步说明吗？”
描述：用户在询问巧克力曲奇饼干的食谱
句子：“你能告诉我现在几点了吗？”
描述：用户在询问当前时间
句子：“今天需要带雨衣吗？”
描述：
""",
    return_tensors="pt",
).to("cpu")

import time

start = time.time()
tokens = model.generate(
    **inputs,
    max_new_tokens=10,
    length_penalty=-1,
    repetition_penalty=1.2,
    num_beams=3,
)
print(time.time() - start)
print(tokenizer.decode(tokens[0], skip_special_tokens=True))
