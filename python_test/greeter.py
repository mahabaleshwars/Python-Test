"""Simple greeter module for testing purposes."""


def greet(name="World"):
    """Generate a greeting message.
    
    Args:
        name: Name to greet (default: "World")
        
    Returns:
        Greeting message string
    """
    return f"Hello, {name}!"


def farewell(name="World"):
    """Generate a farewell message.
    
    Args:
        name: Name to say goodbye to (default: "World")
        
    Returns:
        Farewell message string
    """
    return f"Goodbye, {name}!"
