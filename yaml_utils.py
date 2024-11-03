from ruamel.yaml import YAML
from fire import Fire


def update_yaml_value(file_path, key_path, new_value):
    """
    更新YAML文件中指定路径的值

    Args:
        file_path: YAML文件路径
        key_path: 要更新的键的路径，用点号分隔（例如：'parent.child.key'）
        new_value: 新的值
    """
    yaml = YAML()
    # 保留注释和格式
    yaml.preserve_quotes = True

    # 读取YAML文件
    with open(file_path, "r", encoding="utf-8") as file:
        data = yaml.load(file)

    # 分割键路径
    keys = key_path.split(".")
    current = data

    # 遍历到倒数第二层
    for key in keys[:-1]:
        current = current[key]

    # 更新最后一个键的值
    current[keys[-1]] = new_value

    # 写回文件
    with open(file_path, "w", encoding="utf-8") as file:
        yaml.dump(data, file)


# 使用示例
# file_path = "config.yml"
# key_path = "post.math.enable"  # 例如要修改 database.host 的值
# new_value = True

if __name__ == "__main__":
    Fire(update_yaml_value)
