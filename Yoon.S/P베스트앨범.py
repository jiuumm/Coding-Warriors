#풀이1
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

#풀이2
def solution(genres, plays):
    answer = []
    data = {genre: [] for genre in genres} # 장르를 key로 한 딕셔너리 data 생성
    for z in zip(genres, plays, range(len(genres))): # 장르, 재생 횟수, 고유 번호
        data[z[0]].append([z[1] , z[2]]) # 재생 횟수와 고유 번호를 리스트로 value로 할당
        
    genres_s = sorted(list(data.keys()), key = lambda x: sum(map(lambda y: y[0], data[x])), reverse = True)
    # 장르를 총 재생 횟수대로 정렬한 새로운 리스트 생성
    
    for genre in genres_s:
        songs_number = [song[1] for song in sorted(data[genre], key = lambda x: (x[0], -x[1]), reverse = True)]
        # 장르 별 노래들을 재생 횟수와 고유 번호 순으로 정렬하고, 정렬된 고유 번호들로만 새로운 리스트 생성
        answer += songs_number[:min(len(songs_number), 2)] # answer에 2보다 더 짧으면 리스트 길이만큼, 더 길면 2개 추가
    
    return answer
