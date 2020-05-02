from datetime import date, timedelta
import os
import json
from functools import wraps


def json_cache(cache_directory: str):
    def json_cache_decorator(getter_func):
        @wraps(getter_func)
        def json_cached_getter(*args, **kwargs):
            try:
                os.makedirs(f"{cache_directory}/cache/")
            except FileExistsError:
                # directory already exists
                pass

            arguments = list(args) + list(kwargs.values())
            call = "-".join(map(str, arguments))
            cache_name = f"{cache_directory}/cache/{call}.json"

            try:
                if date.fromtimestamp(os.path.getctime(cache_name)) == date.today():
                    print('Cache hit!')
                    return json.loads(open(cache_name).read())
            except FileNotFoundError:
                pass

            print('Cache miss!')
            data = getter_func(*args, **kwargs)
            open(cache_name, "w").write(json.dumps(data))
            return data

        return json_cached_getter

    return json_cache_decorator
