
def process(arr, len):
    min_i = max_i = pos_num = neg_num = zero = 0

    for i in range(0,len):
        if arr[min_i] > arr[i]:
            min_i = i
        if arr[max_i] < arr[i]:
            max_i = i
        if arr[i] > 0:
            pos_num+=1
        elif arr[i] < 0:
            neg_num += 1
        else:
            zero+=1

    print(f"Minimum and maximum elements: {arr[min_i]} and {arr[max_i]}\n")

    print(f"Positive numbers: {pos_num}\nNegative numbers: {neg_num}\n"
          f"Zero numbers: {zero}\n")

    arr[max_i], arr[min_i] = arr[min_i], arr[max_i]

    print(arr)

def main():
    numb_list = []

    print("Please, input an amount of real numbers: ", end='')

    try:
        length = int(input())
        for i in range(0,length):
            numb_list.append(float(input()))
    except:
        print("some error")
        exit()

    process(numb_list, length)


if __name__ == "__main__":
    main()
