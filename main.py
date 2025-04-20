from ai_api import cz_api, ds_api, silconflow_api
from read_data import read_question, read_question_h
import json
import time
ainame = ["Qwen/Qwen2.5-Coder-7B-Instruct","Qwen/QwQ-32B","deepseek-ai/DeepSeek-R1","Pro/deepseek-ai/DeepSeek-V3","deepseek-ai/DeepSeek-V3","Pro/deepseek-ai/DeepSeek-R1"]
ainamenum = 0
prompt = "你是一个数学专家，请根据题目使用中文给出答案"
qp = "使用中文思考并回答问题："

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
    for m in ainame:
        print(str(ainame.index(m))+":"+m)
    ainamenum = input("请选择ai(输入索引)：")
    if ainamenum != None:
        ainamenum = int(ainamenum)
    lc = input("请选择语言(c/e)：")
    if lc == "e":
        prompt = "you are a math expert, please answer the question using English."
        qp = "use English to think and answer the question:"
    qn = input("请选择题目数量（1，200）：")
    qn = int(qn)
    if not (qn <= 200 and qn >= 1):
        qn = 1
    print("你选择的AI是：", ainame[ainamenum])
    print("你选择的语言是：", lc)
    print("你选择的题目数量是：", qn)
    check = input("是否开始？（y/n）")
    if check == "y":
        try:
            worklog[ainame[ainamenum]] = {}
            for i in range(qn):
                # question_ = read_question("./data/2010-2022_Math_I_MCQs.json", i)
                question_ = read_question_h(i)
                print(question_)
                response = silconflow_api(qp+question_[0], prompt, ainame[ainamenum])
                ai_answear = silconflow_api(response, "你是作答筛选机器人，旨在从文本中去除过程，筛选返回题目答案，只能回答字母或数字！！!（如A,B,C,D,92,68等）", "deepseek-ai/DeepSeek-V3")
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
        
        except Exception as e:
            print(f"An error occurred: {e}")
    
    else:
        print("已取消")




if __name__ == "__main__":
    main()