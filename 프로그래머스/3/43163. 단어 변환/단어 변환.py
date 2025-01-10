from collections import deque

def dfs ():
    return null

def solution(begin, target, words):
    if target not in words :
        return 0
    
    queue = deque([(begin,0)])
    visited = set()
    words_set = set(words)
    
    while queue :
        current_word, count = queue.popleft()
        
        if current_word == target :
            return count
        
        for i in range(len(current_word)):
            for char in "abcdefghijklmnopqrstuvwxyz" :
                next_word = current_word[:i] + char + current_word[i+1:]
                if next_word in words_set and next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word,count+1))
                    
    return 0