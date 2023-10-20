def backward_string(val: str) -> str:
    """
    Reverse the given string.

    Args:
        val (str): The input string to reverse.

    Returns:
        str: The reversed string.
    """
    return val[::-1]

# Example usage:
if __name__ == "__main__":
    print("Example:")
    reversed_str = backward_string("val")
    print(reversed_str)
