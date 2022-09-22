full_text = input("Insert the string:\n")

global charToRemove
charToRemove = "a"

result = ""

occurred_flag = False
for ch in full_text:
    if ch == charToRemove and occurred_flag == False:
        occurred_flag = True
        continue
    else:
        result += ch

print (result)