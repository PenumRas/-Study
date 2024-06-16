
def total_salary(path):
    try:
        with open(path, "r", encoding="UTF-8") as fh:
            lines = [el.strip() for el in fh.readlines()]
            names = []
            sallaries = []

            for line in lines:
                name, sallary = line.split(",")
                names.append(name.strip())
                sallaries.append(int(sallary.strip()))
            total_salary: int = 0

            for el in sallaries:
                total_salary += el
            average = total_salary / len(sallaries)

            return total_salary, average

    except (IndentationError, FileNotFoundError, TypeError):
        print("Try to use correct path or Name")
total, average = total_salary(("Salary.txt"))
print(f"Занальна сума заробітної плати: {total}, Середня заробітня плата:{average}")
