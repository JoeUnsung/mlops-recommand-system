import datetime
import json
from os import path, makedirs


def json_to_str(v):
    try:
        json.loads(v)
        return json.dumps(v)
    except Exception:
        return v


def get_root_dir():
    return path.dirname(path.abspath(path.join(__file__, "..", "..")))


def init_dirs(*paths):
    for p in paths:
        makedirs(p, exist_ok=True)

def make_s3_dataset_path(
    base_dir, 
    dataset_name, 
    dataset_version, 
    base_date: 
    datetime.datetime
):
    return path.join(
        base_dir,
        dataset_name,
        f"v{dataset_version}",
        base_date.strftime("year=%Y"),
        base_date.strftime("month=%m"),
        base_date.strftime("day=%d"),
    )


def make_s3_model_output_path(base_dir, model_name, base_date: datetime.datetime):
    return path.join(
        base_dir,
        model_name,
        base_date.strftime("year=%Y"),
        base_date.strftime("month=%m"),
        base_date.strftime("day=%d"),
    )