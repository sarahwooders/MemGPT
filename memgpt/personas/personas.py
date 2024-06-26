import os

DEFAULT = 'sam'
GPT35_DEFAULT = 'sam_simple_pov_gpt35'


def get_persona_text(key=DEFAULT):
    filename = key if key.endswith('.txt') else f'{key}.txt'
    file_path = os.path.join(os.path.dirname(__file__), 'examples', filename)

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return file.read().strip()
    else:
        raise FileNotFoundError(f"No file found for key {key}, path={file_path}")
