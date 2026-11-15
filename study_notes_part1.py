sample_notes = [
    "IMPORTANT: Complete Python homework\n",
    "TODO: Revise file handling concepts\n",
    "NOTE: read(n) previews characters\n",
    "IMPORTANT: Submit assignment today\n",
    "SKIP: This line is not needed\n",
    "NOTE: readlines() stores lines in a list\n",
    "TODO: Practise loops with files\n",
]

file = open("class-notes.txt", "w")
file.writelines(sample_notes)
file.close()
print("Sample file 'class-notes.txt' created.")

print("\nPART 1: Preview with read(40)")
file = open("class-notes.txt", "r")
print(file.read(40))
file.close()

print("\nPART 2: readlines()")
file = open("class-notes.txt", "r")
lines = file.readlines()
file.close()

print("Total lines:", len(lines))
for number, line in enumerate(lines, start=1):
    print(number, "->", line.strip())

print("\nPART 3: Loop line by line")
file = open("class-notes.txt", "r")
for line in file:
    print("Reading:", line.strip())
file.close()

print("\nPART 4: Filter with a condition")
kept = 0
skipped = 0

file = open("class-notes.txt", "r")
for line in file:
    if line.startswith("SKIP"):
        print("Skipped:", line.strip())
        skipped += 1
    else:
        print("Kept:", line.strip())
        kept += 1
file.close()

print("Total kept:", kept)
print("Total skipped:", skipped)

print("\nPART 5: Copy selected lines to a new file")
file = open("class-notes.txt", "r")
lines = file.readlines()
file.close()

copied = 0
organized_file = open("organized-notes.txt", "w")
for line in lines:
    if line.startswith("IMPORTANT") or line.startswith("TODO"):
        organized_file.write(line)
        copied += 1
organized_file.close()

print("Lines copied:", copied)

print("\nPART 6: Organized notes")
file = open("organized-notes.txt", "r")
for line in file:
    print(line.strip())
file.close()