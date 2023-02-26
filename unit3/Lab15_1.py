def safe_int(arg):
    try:
        return int(arg)
    except:
        return None

print(safe_int(1))
print(safe_int(2.5))
print(safe_int("jazda"))