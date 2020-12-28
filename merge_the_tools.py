def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    if n % k == 0:
        parts = int(n / k)
        for i in range(parts):
            temp = string[i * k: (i + 1) * k]
            result = ""
            for j in temp:
                if j not in result:
                    result = result + j
            print(result)
    else:
        print("n is not multiple of k.")

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)