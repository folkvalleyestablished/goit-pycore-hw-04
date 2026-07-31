def total_salary(path):
    salaries = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                name, salary = line.split(",")
                salaries.append(int(salary))

    except FileNotFoundError:
        print(f"Файл {path} не знайдено :(")
        return None, None
    except ValueError:
        print("В файлі щось не так з форматом, перевір дані")
        return None, None

    if len(salaries) == 0:
        print("У файлі немає жодного запису про зп")
        return None, None

    total = sum(salaries)
    average = total / len(salaries)

    return total, average


if __name__ == "__main__":
    total, average = total_salary("salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
