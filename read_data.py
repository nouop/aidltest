
def read_question(address,num):
    import json
    with open(address, 'r', encoding='utf-8') as f:
        searchf = json.load(f)
    relist = [searchf["example"][num]["question"], searchf["example"][num]["answer"][0]]
    return relist

def read_question_h(inum):
    import pandas as pd
    df = pd.read_csv("data/AIME_Dataset_1983_2024.csv",encoding="utf-8")
    q = df['Question']
    a = df['Answer']

    relist = [q[inum], a[inum]]
    return relist


