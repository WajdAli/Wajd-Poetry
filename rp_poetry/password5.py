# Taken from mission Acceptable Password IV

# Taken from mission Acceptable Password III
# Taken from mission Acceptable Password II
# Taken from mission Acceptable Password I
def is_acceptable_password(password: str) -> bool:
    cond1 = len(password) > 6
    cond2 = any(map(str.isdigit, password))
    cond3 = any(map(str.isalpha, password))
    cond4 = len(password) > 9
    cond5 = 'password' not in password.lower()
    if cond1 and ((cond2 and cond3) or cond4) and cond5:
        return True
    else:
        return False


print("Example:")
print(is_acceptable_password("short"))

