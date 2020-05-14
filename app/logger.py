def log(msg, new_line=True):
    if not new_line:
        print(msg, end="")
    else:
        print(msg)