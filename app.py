import gradio as gr
import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoModel

# download internlm2 to the base_path directory using git tool
base_path = './huatuo2'
os.system(f'git clone https://code.openxlab.org.cn/yinjiuzui/huatuo2.git {base_path}')
os.system(f'cd {base_path} && git lfs pull')

tokenizer = AutoTokenizer.from_pretrained(base_path,trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(base_path,trust_remote_code=True, torch_dtype=torch.float16).cuda()

def chat(message,history):
    for response,history in model.stream_chat(tokenizer,message,history,max_length=2048,top_p=0.7,temperature=1):
        yield response

gr.ChatInterface(chat,
                 title="健康咨询中医Chat",
                 description="""
中医是中国传统文化的重要组成部分，拥有几千年的历史。中医强调整体观念和辩证施治，通过望、闻、问、切四诊合参，结合中药、针灸、推拿等多种治疗手段，以调节人体阴阳平衡，达到治病防病的目的。中医理论体系包括阴阳五行、气血津液、脏腑经络等，具有深厚的哲学基础和独特的诊疗方法。现代中医在传承的基础上不断发展，结合现代科技手段，致力于为人类健康提供更全面的服务。通过中医，可以更好地理解人体与自然的和谐关系，促进身心健康，提升生活质量。
                 """).queue(1).launch()
