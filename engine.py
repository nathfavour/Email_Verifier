from verify_email import verify_email

with open('email_list.txt', "r") as f:
    emails = f.read().splitlines()

for email in emails:
    is_valid = verify_email(email)
    if is_valid:
        print(f"{email} is valid!")
        with open('results.txt', 'a') as f:
            f.write(email)
            f.write("\n")
            f.close()
    else:
        print(f"{email} is Invalid!!!")
        with open('invalid.txt', 'a') as f:
            f.write(email)
            f.write("\n")
            f.close()