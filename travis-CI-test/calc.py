def multiply(*num):
    prod = 1
    for n in num:
        prod *= n
    return prod

if __name__ == "__main__":
    print(multiply(1,2,3,4,5,6))  # 720