import os
base_path = './model'
os.system(f'git clone https://code.openxlab.org.cn/MrCat/CatMediHealer_internlm.git {base_path}')
os.system(f'cd {base_path} && git lfs pull')
os.system('streamlit run app.py --server.address=0.0.0.0 --server.port 7860')
