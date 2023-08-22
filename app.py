import random
import string

# To change the length of password just change the length of k. e.g k=8
print("".join(random.choices(string.ascii_letters + string.digits + string.printable, k=12)))
