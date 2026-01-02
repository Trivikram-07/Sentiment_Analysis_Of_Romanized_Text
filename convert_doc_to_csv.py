from docx import Document
import csv

input_doc = "major project data.docx"   # your doc file
output_csv = "data.csv"

doc = Document(input_doc)
lines = [p.text.strip() for p in doc.paragraphs if p.text.strip()]

rows = []

i = 0
while i < len(lines):
    line = lines[i]

    # Expecting:  "NEG: some text here"
    if ":" in line:
        label, text = line.split(":", 1)
        label = label.strip()
        text = text.strip()

        # skip next line because it's the language-tag line
        if i + 1 < len(lines):
            next_line = lines[i+1]
            if all(x in ["te", "en", "univ"] for x in next_line.split()):
                i += 2
            else:
                i += 1
        else:
            i += 1

        rows.append([label, text])
    else:
        i += 1

# write to CSV
with open(output_csv, "w", newline="", encoding="utf8") as f:
    writer = csv.writer(f)
    writer.writerow(["label", "text"])
    writer.writerows(rows)

print("Created data.csv with", len(rows), "rows.")
