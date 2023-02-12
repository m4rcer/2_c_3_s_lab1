def pre_process(a=0.97):
    def decorator(function):
        def wrapper(*args, **kwargs):
            s = args[0]

            for i in range(1, len(s)):
                s[i] = s[i] - a * s[i-1]

            return function(s)
        return wrapper
    return decorator

@pre_process(a=0.93)
def plot_signal(s):
 for sample in s:
    print(sample)


signal = [1,2,3,4,5,6,7,8,9,10]

plot_signal(signal)