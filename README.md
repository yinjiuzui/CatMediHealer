# CatMediHealer_internlm
  中文文化中，猫常常被视为拥有某种神秘力量的生物，能够带来好运，也象征着保护和治愈。结合 Medi 和 Healer ，CatMediHealer旨在传达出这是一个融合了中医智慧与现代大数据技术的医疗大模型，不仅能够深入挖掘和理解中医的复杂知识体系，还能为现代医疗提供智能化的辅助诊断和治疗建议，就如同一位拥有猫一般敏锐直觉的中医治疗专家。

## 代办事项
- [ ] 模型自我认知训练
- [ ] 加入RAG和Agent
- [ ] 开源数据集

## 环境配置
```bash
git clone https://github.com/yinjiuzui/CatMediHealer_internlm.git
cd CatMediHealer_internlm

conda create --name CatMediHealer_internlm python=3.10 -y
conda activate CatMediHealer_internlm

# install packages
pip install transformers==4.35.2
pip install streamlit==1.24.0
pip install sentencepiece==0.1.99
pip install accelerate==0.24.1
```
