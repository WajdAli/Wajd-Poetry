def checkio(num: int) -> str:
    if num % 3 == 0:
        return "Fizz"
    else:
        return str(num)


print("Example:")
print(checkio(3))

