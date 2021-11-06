def capitalize(text):
    if not isinstance(text, str):
        raise ValueError('Need string to capitalize')
    return text.upper()

