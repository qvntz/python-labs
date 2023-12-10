def _generate_latex_table(matrix):
    table = "\\begin{tabular}{" + " |".join(["l"] * len(matrix[0])) + " }\n"
    table += "\\hline\n"

    for row in matrix:
        table += " & ".join(row) + " \\\\ \\hline\n"

    table += "\\end{tabular}"
    return table


def _save_to_tex_file(tex_string, filename="table.tex"):
    with open(filename, "w") as file:
        file.write(tex_string)


def create_table(matrix):
    for i, row in enumerate(matrix):
        matrix[i] = list(map(str, row))
    table = _generate_latex_table(matrix)
    _save_to_tex_file(table)


# create_table([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
