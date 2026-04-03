import pandas as pd

df = pd.read_csv("students.csv")

df["Середній бал"] = df[["предмет1", "предмет2", "предмет3", "предмет4", "предмет5"]].mean(axis=1)
print("Середній бал кожного студента:")
print(df[["ім'я", "прізвище", "Середній бал"]])

print("\nСередній бал групи по кожному предмету:")
subject_avgs = df[["предмет1", "предмет2", "предмет3", "предмет4", "предмет5"]].mean()
for subj, avg in subject_avgs.items():
    print(f"{subj}: {avg:.2f}")

df.to_csv("students_with_avg.csv", index=False)