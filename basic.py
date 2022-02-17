
def max_element(arr):
    ans = arr[0]
    for i in range(1,10):
        if int(ans) < int(arr[i]):
            ans = arr[i]
    print("Max element is: {}\n".format(ans))

def pros_zero_elements(arr):
    pros, start_i = 1, 0

    while( arr[start_i] != 0):
        start_i+=1
    start_i += 1

    while(arr[start_i] != 0):
        pros *= arr[start_i]
        start_i += 1

    print("Multiplication result between zero elements = ", pros, "\n")

def reconstructing(user_array):
    newN, new_arr, l = 10, [33, 0, 28, -16, -3, 74, 0, -39, 99, 0], 0
    r = newN-1

    for i in range (0, 10):
        if( i % 2 == 0):
            new_arr[r] = user_array[i]
            r-=1
        if( i % 2 != 0):
            new_arr[l] = user_array[i]
            l+=1

    view(new_arr)

def view(arr):
    print("Reconstructed array:")
    for i in range(0,10):
        print(arr[i], " ", end = '')

def main():
    user_array = [33, 0, 28, -16, -3, 74, 0, -39, 99, 0]

    max_element(user_array)

    pros_zero_elements(user_array)

    reconstructing(user_array)

if __name__ == "__main__":
    main()