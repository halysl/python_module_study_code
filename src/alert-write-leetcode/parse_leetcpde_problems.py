# -*- coding: utf-8 -*-
import os
import json
from datetime import datetime, timedelta
dir_name = os.path.dirname(os.path.abspath(__file__))


def get_info(file_name):
    with open(os.path.join(dir_name, file_name), "r") as f:
        data = json.load(f)
    return data["stat_status_pairs"]


def parse_info(more_data):
    base_url = "https://leetcode.com/problems/"
    difficulty_dict = {3: "困难", 2: "中等", 1: "简单", 0: "未知"}
    info_list = []
    for data in more_data:
        stat = data["stat"]
        if not data["paid_only"]:
            res = {
                "question_id": stat["question_id"],
                "question__title": stat["question__title"],
                "question__url": base_url + stat["question__title_slug"],
                "difficulty": difficulty_dict[
                    data.get("difficulty", {}).get("level", 0)
                    ],
                "level": data.get("difficulty", {}).get("level", 0)
            }
            info_list.append(res)
        else:
            continue
    info_list.sort(key=lambda x: x["level"])
    dt = datetime(2019, 8, 9, 0, 0, 0, 0)
    for info in info_list:
        today = dt.strftime("%Y%m%d")
        info["day"] = today
        if dt.weekday == 6:
            dt = dt + timedelta(days=2)
        else:
            dt = dt + timedelta(days=1)
    return info_list

if __name__ == "__main__":
    data = get_info("leetcode_all_problems.json")
    info_list = parse_info(data)
    with open(os.path.join(dir_name, "problem_list"), "w") as f:
        json.dump(info_list, f)
