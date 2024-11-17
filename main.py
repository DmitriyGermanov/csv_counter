import csv
from collections import Counter
file_path = "threats.csv"

measures_counter = Counter()
with open(file_path, encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        measures = row["Меры защиты"].split(";")
        measures_counter.update(measure.strip() for measure in measures)

sorted_measures = sorted(measures_counter.items(), key=lambda x: x[1], reverse=True)
output_data = []
for measure, score in sorted_measures:
    output_data.append({
        "Код меры": measure,
        "Количество баллов": score,
    })

output_file = "sorted_measures.csv"
with open(output_file, "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=output_data[0].keys())
    writer.writeheader()
    writer.writerows(output_data)

print(f"Результаты сохранены в {output_file}")
