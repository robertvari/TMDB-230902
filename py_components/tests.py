def slice_long_text(text, max_length):
    if len(text) > max_length:
        return f"{text[:max_length]}..."
    return text

print(slice_long_text("Creation of the Gods I: Kingdom of Storms", 20))