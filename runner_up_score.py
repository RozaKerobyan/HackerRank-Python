if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr_list = []
    
for i in arr:
    arr_list.append(i)

runner_up = set(arr_list)
old_max = max(arr_list)
runner_up.remove(old_max)
new_max = max(runner_up)
print(new_max)
