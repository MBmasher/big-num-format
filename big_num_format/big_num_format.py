import math
import os
import decimal


def round_str(string_num, decimal_points):
    if len(string_num.split(".")) == 1:
        return string_num

    if len(string_num.split(".")) <= decimal_points:
        return string_num

    whole_part, decimal_part = string_num.split(".")

    digits = whole_part + decimal_part
    if int(decimal_part[decimal_points]) < 5:
        return string_num[: 2 + len(whole_part) + decimal_points]
    else:
        decimal_index = len(whole_part) + decimal_points - 1


def get_name(magnitude_over_3, shorten=False):
    if magnitude_over_3 == 0:
        return ""

    filename = ""
    if shorten:
        filename = os.path.join(os.path.dirname(__file__), "symbols.txt")
    else:
        filename = os.path.join(os.path.dirname(__file__), "words.txt")

    names_file = open(filename, "r")
    names_lines = [i.split("\n")[0] for i in names_file.readlines()]

    if magnitude_over_3 == 1:
        return names_lines[0]

    small_units_names = names_lines[1].split(",")
    big_units_names = [i.split("_")[0] for i in names_lines[2].split(",")]
    tens_names = [i.split("_")[0] for i in names_lines[3].split(",")]

    if not shorten:
        big_units_flags = []
        tens_flags = []

        for big_units, tens in [
            (names_lines[2].split(",")[i], names_lines[3].split(",")[i])
            for i in range(9)
        ]:
            big_units_append = ""
            tens_append = ""

            big_units_split = big_units.split("_")
            tens_split = tens.split("_")

            if len(big_units_split) > 1:
                big_units_append = big_units_split[1]

            if len(tens_split) > 1:
                tens_append = tens_split[1]

            big_units_flags.append(big_units_append)
            tens_flags.append(tens_append)

    magnitude_units_digit = (magnitude_over_3 - 1) % 10
    magnitude_tens_digit = math.floor((magnitude_over_3 - 1) / 10)

    units_name = ""
    tens_name = ""
    exception_char = ""

    # Use second line of names file when magnitude is under 11
    if magnitude_over_3 < 11:
        units_name = small_units_names[magnitude_units_digit - 1]
    else:
        # Use fourth line for the tens digits of the magnitude
        tens_name = tens_names[magnitude_tens_digit - 1]

        # Use third line for the units digits of the magnitude
        if magnitude_units_digit > 0:
            units_name = big_units_names[magnitude_units_digit - 1]

            if not shorten:
                # Add exception character to join the two words if needed.
                exception_char = "".join(
                    set(big_units_flags[magnitude_units_digit - 1])
                    & set(tens_flags[magnitude_tens_digit - 1])
                )

                # Strange exception case:
                # "tre" has the "x" flag but uses the character "s"

                if units_name == "tre" and "x" in tens_flags[magnitude_tens_digit - 1]:
                    exception_char = "s"

    names_file.close()

    return units_name + exception_char + tens_name


def format_num(number, shorten=False, precision=0, decimal_precision=2):
    decimal_number = decimal.Decimal(number)

    if abs(decimal_number) >= 1e303:
        raise ValueError("Number is bigger than or equal to 1e303.")

    negative = decimal_number < 0

    numbers_list = []
    rounded_number_string = "{:.0f}".format(decimal_number)

    magnitude = len(rounded_number_string) - 1
    magnitude_over_3 = math.floor(magnitude / 3)

    min_index = 0
    max_index = (magnitude + 1) % 3

    if max_index == 0:
        max_index = 3

    decimal_number_string = "{:.{}f}".format(decimal_number, decimal_precision + 1)
    decimal_number_string = "".join(decimal_number_string.split("."))

    last_index = 0
    if precision <= 0:
        last_index = -precision
    else:
        last_index = magnitude_over_3 - precision + 1

    last_index = min(max(last_index, 0), magnitude_over_3)
    decimal_point_index = (magnitude_over_3 - last_index) * 3 + max_index
    decimal_number_string = (
        decimal_number_string[:decimal_point_index]
        + "."
        + decimal_number_string[decimal_point_index:]
    )

    print(decimal_number_string)

    decimal_number_string = "{:.{}f}".format(
        decimal.Context(prec=decimal_precision + magnitude).create_decimal(
            decimal.Decimal(decimal_number_string)
        ),
        decimal_precision,
    )

    print(decimal_number_string)

    for i in range(magnitude_over_3, last_index - 1, -1):
        if i == last_index:
            max_index = len(decimal_number_string)
        sub_number_string = decimal_number_string[min_index:max_index].strip("0")

        min_index = max_index
        max_index += 3
        if len(sub_number_string) == 0:
            continue

        if sub_number_string[-1] == ".":
            sub_number_string = sub_number_string[:-1]

        number_name = get_name(i, shorten)

        if sub_number_string[0] != "0":
            numbers_list.append(sub_number_string + " " * (1 - shorten) + number_name)

    if len(numbers_list) == 1:
        return numbers_list[0]

    final_number = ""
    if shorten:
        final_number = " ".join(numbers_list)
    else:
        final_number = ", ".join(numbers_list[:-1])
        final_number += " and " + numbers_list[-1]

    return final_number.strip()
