def solution(n, words):
    speak = [words[0]]
    count = 0
    for word in words[1:]:
        count += 1
        if word not in speak and speak[-1][-1] == word[0]:
            speak.append(word)
        else :
             return [count%n+1,count//n+1]
            
    return [0,0]