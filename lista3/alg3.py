def reverter_string_loop(s):
    return ''.join([s[i] for i in range(len(s) - 1, -1, -1)])

def reverter_string_slice(s):
    return s[::-1]
