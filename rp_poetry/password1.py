def is_acceptable_password(password: str) -> bool:
    if len(password) <= 6:
        return False
    else:
        return True


print("Example:")
print(is_acceptable_password("short"))

