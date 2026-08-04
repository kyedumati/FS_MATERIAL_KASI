"""SOLUTION — marks list menu (no def — Functions week later)."""

marks = []

while True:
    print("1 add  2 list  3 avg  4 toppers  5 quit")
    c = input("> ").strip()
    if c == "1":
        raw = input("mark: ").strip()
        if not raw.replace(".", "", 1).isdigit():
            print("Numbers only")
            continue
        value = float(raw)
        if value < 0 or value > 100:
            print("0–100 only")
            continue
        marks.append(value)
    elif c == "2":
        print(marks)
    elif c == "3":
        if len(marks) == 0:
            print("no marks")
        else:
            avg = round(sum(marks) / len(marks), 2)
            print(avg)
    elif c == "4":
        toppers = []
        for m in marks:
            if m >= 90:
                toppers.append(m)
        print(toppers)
    elif c == "5":
        break
    else:
        print("Invalid choice")
