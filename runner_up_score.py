if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    arr = set(arr)
    old_max = max(arr)
    arr.remove(old_max)
    runner_up = max(arr)
    print(runner_up)
