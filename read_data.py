
def read_question(address,num):
    import json
    with open(address, 'r', encoding='utf-8') as f:
        searchf = json.load(f)
    relist = [searchf["example"][num]["question"], searchf["example"][num]["answer"][0]]
    return relist
