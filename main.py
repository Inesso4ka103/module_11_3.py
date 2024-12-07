def introspection_info(obj):
    type_obj = type(obj).__name__
    attributes = dir(obj)
    methods = [method for method in attributes if callable(getattr(obj, method))]
    module = obj.__class__.__module__
    info = {'type': type_obj, 'attributes': attributes, 'methods': methods, 'module': module}
    return info

number_info = introspection_info(42)
print(number_info)

list_info = introspection_info([134, 'balance', 5.6])
print(list_info)

string_info = introspection_info('Hello, World!')
print(string_info)


    