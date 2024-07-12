from collections import deque
# 創建一個空的隊列
snack_queue = deque() 
# 向隊列中加入學生
snack_queue.append("Jason")
snack_queue.append("Angus")
snack_queue.append("SCPAngus615")
print(f"初始隊列:{snack_queue}")
first_student = snack_queue.popleft()
# 第一位學生購買點心並離開隊列
print(f"{first_student} 已經點心並離開隊列.")
print(f"現在的隊列:{snack_queue}")