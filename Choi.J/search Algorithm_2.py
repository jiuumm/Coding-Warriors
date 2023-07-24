#sol1
def solution(genres, plays):
    answer=[]
    data={}

    for song in range(len(genres)):
        genre=genres[song]

        if genre not in data:
            data[genre]=[(song, plays[song])]
        data[genre].append((song, plays[song]))

    genres_s=[]
    for genre in data.keys():
        genres_s.append((genre, sum([song[1] for song in data[genre]])))
    genres_s=sorted(genres_s, key=lambda x: -x[1])

    for genre, _ in genres_s:
        songs_s=sorted(data[genre], key=lambda x: -x[1])

        for song in songs_s[:2]:
            answer.append(song[0])
    return answer

#sol2
def solution(genres, plays):
    answer=[]
    data={}

    for song in range(len(genres)):
        genre=genres[song]
        count=plays[song]

        if genre not in data:
            data[genre]=[(song, count)]
        data[genre].append((song, count))   #(노래번호, 재생횟수) 형식

    #장르별 총 재생횟수 합산
    genres_s=sorted(data.keys(), key=lambda x: -sum(count for _, count in data[x]))

    #장르별 정렬 후 
    for genre in genres_s:
        songs_s=sorted(data[genre], key=lambda x: (x[1], -x[0]), reverse=True)
        for song in range(min(2, len(songs_s))):
            answer.append(songs_s[song][0])

    return answer
