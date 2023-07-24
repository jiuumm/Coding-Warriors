# sorted(정렬할 데이터, key 파라미터)

def solution(genres, plays):
    answer = []
    data = {}
    
    for song in range(len(genres)): # 노래의 개수만큼 반복
        genre = genres[song] # 해당 노래의 장르
        
        if genre in data: # 이미 장르를 추가했다면
            data[genre].append((song, plays[song])) # 고유 번호와 재생 횟수를 value에 배열로 추가
        else: # 추가가 안 됐다면
            data[genre] = [(song, plays[song])] # 고유 번호와 재생 횟수를 value에 배열로 넣기
    
    genres_s = [] # 장르 별 총 재생 횟수 리스트
    for genre in data.keys():
        genres_s.append((genre, sum([song[1] for song in data[genre]]))) # 장르와 총 재생 횟수를 배열로 추가
    genres_s = sorted(genres_s, key = lambda x: -x[1]) # 총 재생 횟수대로 정렬
    
    for genre, _ in genres_s:
        songs_s = sorted(data[genre], key = lambda x: -x[1]) # 노래들을 재생 횟수대로 정렬
        
        for song in songs_s[:2]:
            answer.append(song[0])
    
    return answer
