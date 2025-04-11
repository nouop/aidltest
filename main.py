from ai_api import cz_api, ds_api, silconflow_api
from read_data import read_question
import json
import time
ainame = ["Qwen/Qwen2.5-Coder-7B-Instruct","Qwen/QwQ-32B","deepseek-ai/DeepSeek-R1","Pro/deepseek-ai/DeepSeek-V3","deepseek-ai/DeepSeek-V3","Pro/deepseek-ai/DeepSeek-R1"]
ainamenum = 0
worklog = {}


def save_to_json(data, filename):
    try:
        with open(filename, 'r',encoding='utf-8') as file:
            json_data = json.load(file)
            if list(data.keys())[0] in json_data:
                json_data[list(data.keys())[0]].update(data[list(data.keys())[0]])
            else:
                json_data.update(data)



        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(json_data, json_file)
        print(f"Data successfully written to {filename}")
    except Exception as e:
        print(f"An error occurred while writing to JSON: {e}")


def main():
    worklog[ainame[ainamenum]] = {}
    for i in range(1, 3):
        question_ = read_question("./data/2010-2022_Math_I_MCQs.json", i)
        print(question_)
        response = silconflow_api(question_[0], "你是一个数学专家，请根据题目给出答案", ainame[ainamenum])
        ai_answear = silconflow_api(response, "你是作答筛选机器人，旨在从文本中去除过程，筛选返回题目答案，只能回答字母或数字！！!（如A,B,C,D,92等）", "deepseek-ai/DeepSeek-V3")
        print(response)
        print(ai_answear)
        if ai_answear.strip() == question_[1]:
            worklog[ainame[ainamenum]][str(i+1)] = True
            print("正确")
        else:
            worklog[ainame[ainamenum]][str(i+1)] = False
            print("错误")
    save_to_json(worklog, "worklog.json")
    print(worklog)
        

if __name__ == "__main__":
    main()