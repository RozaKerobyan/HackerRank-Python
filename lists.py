if __name__ == '__main__':
    N = int(input())
    n_list = []

    for i in range (N):
        answer = input().split()
        option = answer[0]
        if option == "append":
            n_list.append(int(answer[1]))
        elif option == "pop":
            n_list.pop()
        elif option == "print":
            print(n_list)
        elif option == "sort":
            n_list.sort()
        elif option == "remove":
            n_list.remove(int(answer[1]))
        elif option == "reverse":
            n_list.reverse()
        elif option == "insert":
            index = int(answer[1])
            k = int(answer[2])
            n_list.insert(index, k)
