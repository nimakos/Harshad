# coding=utf-8

#Προσθέτει τα στοιχεία κάθε αριθμού ο οποίος βρίσκεται στο range
def add_digits(a):
    s_digits = list(str(a))
    dsum = 0
    for i in s_digits:
        dsum += int(i)
    return dsum

#Πολ/ζει τα ψηφία κάθε αριθμού ο οποίος βρίσκεται στο range
def prod_digits(a):
    s_digits = list(str(a))
    p = 1
    for i in s_digits:
        p = p * int(i)
    return p

# Επιστρέφει αποτέλεσμα όταν το υπόλοιπο της διαίρεσης δεν είναι ισο με 0
def is_harshad(a):
  return not a % add_digits(a)

def product(a):
    if prod_digits(a) > 0:  # Μόνο αν συναντήσεις θετικό αριθμό να επιστρέψεις αποτέλεσμα (γιατί μπορεί να υπαρχει και 0)
        return not a % prod_digits(a)


#Τσεκάρει τις τιμές που επιστρέφει η συνάρτηση με αυτές που έχουμε στο range
data = filter(is_harshad, range(1, 1001))
data_prod = filter(product, range(1, 1001))

#Τυπώνει τα αποτελέσματα
print data
print data_prod

