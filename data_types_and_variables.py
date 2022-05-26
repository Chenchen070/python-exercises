# 1. You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it), and Hercules (1 day, you don't know yet if they're going to like it). If price for a movie per day is 3 dollars, how much will you have to pay?
x = (3+5+1) * 3
print (x)

# 2. Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.
x = 400*6 + 380*4 + 350*10
print (x)

# 3. A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule.
class_not_full = True
class_schedule_not_conflict = True
student_can_be_enrolled = class_not_full and class_schedule_not_conflict

print (student_can_be_enrolled)

# 4. A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.
premium_member = True
buy_more_than_2 = True
offer_valid = True
offer_applied = (premium_member or buy_more_than_2) and offer_valid
print (offer_applied)

# 5. Continue working in your data_types_and_variables.py file. Use the following code to follow the instructions below:
username = 'codeup'
password = 'notastrongpassword'

# Create a variable that holds a boolean value for each of the following conditions:
# the password must be at least 5 characters
# the username must be no more than 20 characters
# the password must not be the same as the username
# bonus neither the username or password can start or end with whitespace

username = 'codeup'
password = 'notastrongpassword'

p_length = len(password) > 5
print(p_length)

u_length = len(username) < 20
print(u_length)

match = password != username
print(match)

start_or_end_with_whitespace = username[0] == " " or username[-1] == " "
print(start_or_end_with_whitespace)
start_or_end_with_whitespace = username == username.strip()

start_or_end_with_whitespace_1 = password[0] == " " or password[-1] == " "
print(start_or_end_with_whitespace_1)
start_or_end_with_whitespace_1 = password == password.strip()

username_is_good = u_length and match and start_or_end_with_whitespace
password_is_good = p_length and match and start_or_end_with_whitespace_1

all_good = username_is_good and password_is_good
print(all_good)