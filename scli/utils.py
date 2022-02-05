from importlib import import_module

__all__ = [
    "import_string",
]


def import_string(path):
    try:
        module_path, class_name = path.rsplit(".", 1)
    except ValueError as err:
        raise ImportError(
            "{} doesn't look like a module path".format(path)
        ) from err

    try:
        module = import_module(module_path, class_name)
        return getattr(module, class_name)
    except AttributeError as err:
        raise ImportError(
            'Module "{}" does not define a "{}" attribute/class'.format(module_path, class_name)
        ) from err
