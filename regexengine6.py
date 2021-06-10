def same_length_comp(regex, string, itarete=False, escape=False):
    if regex == "":
        return True 
    if string == "":
        if regex == "$":
            return True
        else:
            return False
    if regex[0] == "\\":
        return same_length_comp(regex[1:], string, escape=True)
    if regex[0] in ("?", "*", "+") and not escape:
        return same_length_comp(regex[1:], string)       
    if regex[0] == string[0]:
        if  len(regex) > 1 and regex[1] in ("*", "+") and not escape: 
            return same_length_comp(regex, string[1:], itarete=True)
        else:
            return same_length_comp(regex[1:], string[1:], escape=False)
    if regex[0] == ".":
        if  len(regex) > 2 and regex[1] in ("*", "+") and not escape:
            if string[0] != regex[2]: 
                return same_length_comp(regex, string[1:], itarete=True)
            else:
                pass
        else:
            return same_length_comp(regex[1:], string[1:], escape=False)
    if len(regex) > 1:
        if regex[1] in ("?", "*") and not escape or regex[1] in ("+") and not escape and itarete:
            return same_length_comp(regex[2:], string)
    escape=False
    return False 

def regex_func(regex, string):
    if regex == "":
        return True
    if regex[0] == "^":
        return same_length_comp(regex[1:], string)
    for i in range(len(string)):
        if same_length_comp(regex, string[i:]):
            return True
    return False

def match_func(input):
    input = input.strip("'")
    regex, string = input.split("|")
    output = regex_func(regex, string)
    return output

print(match_func(input()))
