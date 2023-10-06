# Taken from mission Acceptable Password I

def is_acceptable_password(password: str) -> bool:
    if len(password) > 6 and any(map(str.isdigit, password)):
        return True
    else:
        return False


print("Example:")
print(is_acceptable_password("short"))

