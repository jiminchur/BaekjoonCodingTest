def solution(babbling):
    valid_sounds = ["aya", "ye", "woo", "ma"]
    
    def is_valid_word(word):
        prev_sound = ""
        i = 0
        while i < len(word):
            matched_sound = None
            for sound in valid_sounds:
                if word[i:].startswith(sound):
                    if sound == prev_sound: # 연속해서 같은 발음이 나오는 경우
                        return False
                    matched_sound = sound
                    prev_sound = sound
                    i += len(sound)
                    break
            if not matched_sound: # 유효한 발음과 매치되지 않는 경우
                return False
        return True
    
    count = 0
    for word in babbling:
        if is_valid_word(word):
            count += 1
    
    return count
