import csv

def average_height(filename):
    total_height = 0.0
    count = 0

    infile = open(filename, 'r')
    reader = csv.reader(infile)

    next(reader)
    for row in reader:
        if len(row) < 4:
            continue
        print (f"Gender:{row[0]}, Height:{row[1]}, Weight:{row[2]}, BMI:{row[3]}")
        total_height += float(row[1].strip())
        count += 1

    infile.close()

    if count > 0:
        avg_height = total_height / count
        print(f"\nAverage height of {count} people is {avg_height}")

def add_bmi_record(filename):
    print("\nAdd your information")
    gender = input("Enter gender:").strip()
    height = input("Enter height(cm):").strip()
    weight = input("Enter weight(kg):").strip()
    bmi = input("Enter BMI:").strip()

    outfile = open(filename, 'a', newline='')
    writer = csv.writer(outfile)
    writer.writerow([gender, height, weight, bmi])
    outfile.close()

    print ("Verifying updated file...")
    verify_file = open(filename, 'r')
    print (verify_file)
    verify_file.close()

average_height('bmi.csv')
add_bmi_record('bmi.csv')