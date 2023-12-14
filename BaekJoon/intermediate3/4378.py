# 4378

##import sys
##
##kb = {'1':'`', '2':'1', '3':'2', '4':'3', '5':'4', '6':'5', '7':'6', '8':'7', '9':'8', '0':'9', '-':'0', '=':'-',
##      "W":"Q", 'E':'W', 'R':'E', 'T':'R', 'Y':'T', 'U':'Y', 'I':'U', 'O':'I', 'P':'O', '[':'P', ']':'[', "\\":']',
##      'S':'A', 'D':'S', 'F':'D', "G":'F', 'H':'G', 'J':'H', 'K':'J', 'L':'K', ';':'L', "'":';',
##      'X':'Z', 'C':'X', 'V':'C', 'B':'V', 'N':'B', 'M':'N', ',':'M', '.':',', '/':'.',
##      " ":" "}
##
##ipt = sys.stdin.readline().replace("\n", "")
##
##new = ""
##for letter in ipt:
##    new += kb[letter]
##
##print(new)



#
# sol2) someone's code
#
def te_ach(error_str):
    correct_str = ""
    
    keyboard_corr_dict = {
        "1": "`", "2": "1", "3": "2", "4": "3", "5": "4", "6": "5", "7": "6", "8": "7", "9": "8", "0": "9", "-": "0", "=": "-",
        "w": "q", "e": "w", "r": "e", "t": "r", "y": "t", "u": "y", "i": "u", "o": "i", "p": "o", "[": "p", "]": "[", "\\": "]",
        "s": "a", "d": "s", "f": "d", "g": "f", "h": "g", "j": "h", "k": "j", "l": "k", ";": "l", "'": ";",
        "x": "z", "c": "x", "v": "c", "b": "v", "n": "b", "m": "n", ",": "m", ".":",", "/": ".", " ": " "
    }
            
    return keyboard_corr_dict[error_str.lower()].upper()


if __name__ == "__main__":
    while True:
        try:
            for type_word in input():
                print(te_ach(type_word), end='')
            print()
        except:
            break
