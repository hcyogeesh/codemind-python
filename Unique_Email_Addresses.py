def num_unique_emails(emails):
    unique_emails = set()
    for email in emails:
        local, domain = email.split('@')
        local = local.replace('.','')
        plus_index = local.find('+')
        if plus_index != -1:
            local = local[:plus_index]
        unique_emails.add(local + '@' + domain)
    return len(unique_emails)

n = int(input())
emails = []
for i in range(n):
    email = input()
    emails.append(email)
print(num_unique_emails(emails))
