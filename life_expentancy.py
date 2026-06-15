# Creative addition: After the year analysis, the program shows a simple
# text-based "life expectancy bar" comparing the chosen year's average to
# the global best, giving the user a quick visual sense of the gap.

filename = "life-expectancy.csv"

file = open(filename, "r", encoding="utf-8")
# with open("life-expectancy.csv", "r", encoding="utf-8") as file
next(file) 

overall_min_le = None
overall_max_le = None
overall_min_country = ""
overall_min_year = 0
overall_max_country = ""
overall_max_year = 0

all_records = [] 

for line in file:
    line = line.strip()
    if not line:
        continue
    parts = line.split(",")
    if len(parts) < 4:
        continue
    try:
        life_exp = float(parts[-1])
        year = int(parts[-2])
        country = ",".join(parts[:-3]).strip()
    except ValueError:
        continue

    all_records.append((country, year, life_exp))

    if overall_min_le is None or life_exp < overall_min_le:
        overall_min_le = life_exp
        overall_min_country = country
        overall_min_year = year

    if overall_max_le is None or life_exp > overall_max_le:
        overall_max_le = life_exp
        overall_max_country = country
        overall_max_year = year

file.close()

target_year = int(input("Enter the year of interest: "))
print(f"The overall max life expectancy is: {overall_max_le} from {overall_max_country} in {overall_max_year}")
print(f"The overall min life expectancy is: {overall_min_le} from {overall_min_country} in {overall_min_year}")
print()


year_total = 0
year_count = 0
year_min_le = None
year_max_le = None
year_min_country = ""
year_max_country = ""

for country, year, life_exp in all_records:
    if year == target_year:
        year_total += life_exp
        year_count += 1
        if year_min_le is None or life_exp < year_min_le:
            year_min_le = life_exp
            year_min_country = country
        if year_max_le is None or life_exp > year_max_le:
            year_max_le = life_exp
            year_max_country = country

if year_count == 0:
    print(f"No data found for {target_year}.")
else:
    year_avg = round(year_total / year_count, 2)
    print(f"\nFor the year {target_year}:")
    print(f"The average life expectancy across all countries was {year_avg}")
    print(f"The max life expectancy was in {year_max_country} with {year_max_le}")
    print(f"The min life expectancy was in {year_min_country} with {year_min_le}")

    # --- Creative feature: simple text progress bar ---
    # Shows how the year's average compares to the global best
    bar_length = 40
    filled = int((year_avg / overall_max_le) * bar_length)
    bar = "█" * filled + "░" * (bar_length - filled)
    percent = round((year_avg / overall_max_le) * 100, 1)
    print(f"\n  Progress toward global best ({overall_max_le} yrs):")
    print(f"  [{bar}] {percent}%")