birth_year = float(input("დაბადების წელი: "))
if birth_year < 100:
    print("მტყუანს")
if birth_year >2027:
    print("მტყუანს")

birth_month = float(input("დაბადების თვე: "))
if birth_month > 12:
    print("მტყუანს")

birth_day = float(input("დაბადების დღე: "))
if birth_day > 32:
     print("მტყუანს")

current_year = float(input("მიმდინარე წელი: "))
if current_year <birth_year:
    print("მტყუანს")

current_month = float(input("მიმდინარე თვე: "))

if current_month > 12:
    print("მტყუანს")

current_day = float(input("მიმდინარე დღე: "))
if current_day > 32:
    print("მტყუანს")


else:
    print("თქვენი ასაკი არის:", current_year - birth_year, "წელი", current_month - birth_month, "თვე", current_day - birth_day, "დღე")
