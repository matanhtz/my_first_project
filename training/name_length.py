from training.digit_sum import Utilsfuncts

name = "Matan"
lastname = "Har tzvi"
name_length = len(name)
lastname_length = len(lastname)
if name_length < lastname_length:
    print("last name longer than lastname")

dignum = Utilsfuncts()
sum_of_digs = dignum.digit_sum(367)
print(sum_of_digs)