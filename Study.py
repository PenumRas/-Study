def get_cats_info(path):
    try:
        with open(path, "r") as fh:
            lines = [el.strip() for el in fh.readlines()]
            cat_info = []
            for line in lines:
                id, name, age = line.split(",")
                cats = {
                    "id": id.strip(),
                    "name": name.strip(),
                    "age": age.strip()
                }
                cat_info.append(cats)
        return cat_info
    except FileNotFoundError:
        print(f"file at path{path} not found")
        return []
    except IOError:
        print(f"some error in read path{path}")
        return []


cats_info = get_cats_info("cats_file.txt")
print(cats_info)
