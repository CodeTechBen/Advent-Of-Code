import re


def get_text(filepath: str) -> list[str]:
    """Gets the filepath of the input and returns it as a list of strings, each string represents a different passport."""
    with open(filepath) as f:
        return f.read().split("\n\n")


def is_valid_passport(passport: str) -> bool:
    """
    Checks if a passport is valid by ensuring all required fields are present.
    Required fields: byr, iyr, eyr, hgt, hcl, ecl, pid.
    """
    required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

    fields = re.findall(r'(\w{3}):', passport)
    if required_fields.issubset(fields):
        return True


def solution_1(passports: list[str]) -> int:
    """
    Counts the number of valid passports in the input list.
    """
    return len([passport for passport in passports if is_valid_passport(passport)])


if __name__ == "__main__":
    # text = [
    #     'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm',
    #     'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929',
    #     'hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm',
    #     'hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in'
    # ]

    text = get_text('input.txt')

    valid_passports = solution_1(text)
    print(f"Number of valid passports: {valid_passports}")
