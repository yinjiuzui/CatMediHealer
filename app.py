import gradio as gr
import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# 设置基础路径
base_path = os.path.abspath('CatMediHealer_internlm')

# 检查目录是否存在，如果存在，则跳过克隆步骤
if not os.path.exists(base_path):
    os.system(f'git clone https://code.openxlab.org.cn/MrCat/CatMediHealer_internlm.git {base_path}')
    os.chdir(base_path)
    os.system('git lfs pull')

# Ensure you are in the correct directory if needed
os.chdir(base_path)

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("/home/xlab-app-center/CatMediHealer_internlm", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("/home/xlab-app-center/CatMediHealer_internlm", trust_remote_code=True, torch_dtype=torch.float16).cuda()

def chat(message, history):
    for response, history in model.stream_chat(tokenizer, message, history, max_length=2048, top_p=0.7, temperature=1):
        yield response

gr.ChatInterface(chat,
                 title="猫灵通识",
                 description="""
中文文化中，猫常常被视为拥有某种神秘力量的生物，能够带来好运，也象征着保护和治愈。结合 Medi 和 Healer ，CatMediHealer旨在传达出这是一个融合了中医智慧与现代大数据技术的医疗大模型，不仅能够深入挖掘和理解中医的复杂知识体系，还能为现代医疗提供智能化的辅助诊断和治疗建议，就如同一位拥有猫一般敏锐直觉的中医治疗专家。
                 """).queue(1).launch()
