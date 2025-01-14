def introspection_info(obj):

    info = {
        'type': type(obj).__name__,
        'attributes': [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")],
        'methods': [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")],
        'module': getattr(obj, "__module__", None)
    }

    if hasattr(obj, "__doc__"):
        info['doc'] = obj.__doc__.strip() if obj.__doc__ else "None"

    if hasattr(obj, "__class__"):
        info['class_name'] = obj.__class__.__name__

    return info

if __name__ == "__main__":
    number_info = introspection_info(42)
    print("Информация о числе 42:", number_info)

    string_info = introspection_info("Привет")
    print("Информация о строке 'Привет':", string_info)


    class MyClass:

        def __init__(self, name):
            self.name = name

        def greet(self):
            return f"Hello, {self.name}!"


    my_obj = MyClass("Мой Мир")

    custom_obj_info = introspection_info(my_obj)
    print("Информация о пользовательском объекте:", custom_obj_info)
