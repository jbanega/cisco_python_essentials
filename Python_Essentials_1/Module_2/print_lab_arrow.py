# Print lab
print("Original")
print()
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
print()


# Arrow reducing the number of print function invocations
print("Only one function invocation ")
print()
print("    *", "   * *", "  *   *", " *     *",
"***   ***", "  *   *", "  *   *", "  *****", sep="\n")
print()


# Duplicating the arrow (side by side)
print("Side by side")
print()
spacing = 4*" "
arrow = ["    *", "   * *", "  *   *", " *     *",
"***   ***", "  *   *", "  *   *", "  *****"]
for x in arrow:
    print(x + spacing + ("\t"+x))
print()


# Making arrow twice as large
print("Double size")
print()
big_arrow = 9*" " + "*" + "\n"
for i in range(7):
    big_arrow += (7-(i-1))*" " + "*" + ((2*i)+1)*" " + "*" + "\n"
big_arrow += " " + 5*"*" + 7*" " + 5*"*" + "\n"
big_arrow += (5*" " + "*" + 7*" " + "*" + "\n")*6
big_arrow += 5*" " + 9*"*"
print(big_arrow)