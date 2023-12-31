# Taken from mission Acceptable Password II

# Taken from mission Acceptable Password I
def is_acceptable_password(password: str) -> bool:
    cond1 = len(password) > 6
    cond2 = any(map(str.isdigit, password))
    cond3 = any(map(str.isalpha, password))
    if cond1 and cond2 and cond3:
        return True
    else:
        return False


print("Example:")
print(is_acceptable_password("short"))

