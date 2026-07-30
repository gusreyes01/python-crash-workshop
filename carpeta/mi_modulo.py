def saludar(name):
    if not isinstance(name, str) or not name.strip():
        raise ValueError("name must be a non-empty string")
    greeting = f"Hola, {name.strip()}"
    print(greeting)
    return greeting
