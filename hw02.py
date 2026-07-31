def get_cats_info(path):
    cats_info = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue

                parts = line.split(",")
                cat_id, name, age = parts

                cat = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }
                cats_info.append(cat)

    except FileNotFoundError:
        print(f"Не можу знайти файл {path}")
    except ValueError:
        print("В файлі неправильний формат даних")

    return cats_info


if __name__ == "__main__":
    cats_info = get_cats_info("cats_file.txt")
    print(cats_info)
