def non_empty(function):
    def wrapper():
        result = function()

        return list(filter(lambda el: bool(el), result))

    return wrapper

@non_empty
def get_pages():
 return ['chapter1', '', 'contents', '', 'line1']

print(get_pages())