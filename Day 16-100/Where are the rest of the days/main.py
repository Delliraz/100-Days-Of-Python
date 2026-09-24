from prettytable import PrettyTable

table = PrettyTable()
table.align = "c"
table.field_names=["Pokemon Name", "Type"]
table.add_row(["Pikachu", "Electric"])
print(table)