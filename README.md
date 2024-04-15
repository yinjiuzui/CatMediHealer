# CatMediHealer_internlm
  中文文化中，猫常常被视为拥有某种神秘力量的生物，能够带来好运，也象征着保护和治愈。结合 Medi 和 Healer ，CatMediHealer旨在传达出这是一个融合了中医智慧与现代大数据技术的医疗大模型，不仅能够深入挖掘和理解中医的复杂知识体系，还能为现代医疗提供智能化的辅助诊断和治疗建议，就如同一位拥有猫一般敏锐直觉的中医治疗专家。

## 代办事项
- [ ] 模型自我认知训练
- [ ] 加入RAG和Agent
- [ ] 开源数据集

## 环境配置
```bash
git clone https://github.com/rlawjdghek/StableVITON
cd StableVITON

conda create --name StableVITON python=3.10 -y
conda activate StableVITON

# install packages
pip install torch==2.0.0+cu117 torchvision==0.15.1+cu117 torchaudio==2.0.1 --index-url https://download.pytorch.org/whl/cu117
pip install pytorch-lightning==1.5.0
pip install einops
pip install opencv-python==4.7.0.72
pip install matplotlib
pip install omegaconf
pip install albumentations
pip install transformers==4.33.2
pip install xformers==0.0.19
pip install triton==2.0.0
pip install open-clip-torch==2.19.0
pip install diffusers==0.20.2
pip install scipy==1.10.1
conda install -c anaconda ipython -y
```
