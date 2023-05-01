list_of_tuples = [('IT_VLAN', 320),
                  ('Mngmt_VLAN', 99),
                  ('User_VLAN', 1010),
                  ('DB_VLAN', 11)]

srt = sorted(list_of_tuples, key=lambda key: key[1])

print(srt)
