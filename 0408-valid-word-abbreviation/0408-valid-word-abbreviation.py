class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        word_index = 0
        abbr_index = 0
        
        while word_index < len(word) and abbr_index < len(abbr):
            if abbr[abbr_index].isnumeric():
                if abbr[abbr_index] == '0':
                    return False
                    
                num = 0
                while abbr_index < len(abbr) and abbr[abbr_index].isnumeric():
                    num = num * 10 + int(abbr[abbr_index])
                    abbr_index += 1
                
                word_index += num
            else:
                if word[word_index] != abbr[abbr_index]:
                    return False
                abbr_index += 1
                word_index += 1
            
        return word_index == len(word) and abbr_index == len(abbr)