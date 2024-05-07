def solution(genres, plays):
    # Step 1: 각 장르별로 노래의 재생 횟수 합산
    genre_play_counts = {}
    for i in range(len(genres)):
        if genres[i] not in genre_play_counts:
            genre_play_counts[genres[i]] = plays[i]
        else:
            genre_play_counts[genres[i]] += plays[i]
    
    # Step 2: 재생 횟수 합산된 장르들을 내림차순으로 정렬
    sorted_genres = sorted(genre_play_counts.keys(), key=lambda x: genre_play_counts[x], reverse=True)
    
    # Step 3: 각 장르별로 노래들을 재생 횟수 내림차순, 고유 번호 오름차순으로 정렬
    genre_song_dict = {}
    for i in range(len(genres)):
        if genres[i] not in genre_song_dict:
            genre_song_dict[genres[i]] = [(plays[i], i)]
        else:
            genre_song_dict[genres[i]].append((plays[i], i))
    for genre in genre_song_dict:
        genre_song_dict[genre] = sorted(genre_song_dict[genre], key=lambda x: (-x[0], x[1]))
    
    # Step 4: 각 장르별로 노래를 최대 2개씩 선택
    answer = []
    for genre in sorted_genres:
        selected = genre_song_dict[genre][:2]
        for song in selected:
            answer.append(song[1])
    
    return answer