"""Hello World module."""


def hello(name: str | None = None) -> str:
    """Return a hello world greeting.
    
    Args:
        name: Optional name to greet. If None, returns 'Hello, World!'.
    
    Returns:
        A greeting string.
    """
    if name:
        return f"Hello, {name}!"
    return "Hello, World!"


if __name__ == "__main__":
    print(hello())
