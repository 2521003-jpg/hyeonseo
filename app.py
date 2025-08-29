Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import streamlit as st

# 🎵 예시 음악 데이터
TRACKS = [
    {
        "title": "Lo-Fi Rain Window",
        "artist": "Chillhop Collective",
        "mood": "우울",
        "situation": "비 오는 날",
        "place": "실내",
        "image": "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?q=80&w=800"
    },
    {
        "title": "Sunrise Bossa",
...         "artist": "Nova Bossa",
...         "mood": "기쁨",
...         "situation": "아침 준비",
...         "place": "해변",
...         "image": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?q=80&w=800"
...     },
...     {
...         "title": "Midnight City Ride",
...         "artist": "Synthwave Lane",
...         "mood": "설렘",
...         "situation": "밤 산책",
...         "place": "도심",
...         "image": "https://images.unsplash.com/photo-1491555103944-7c647fd857e6?q=80&w=800"
...     },
... ]
... 
... st.set_page_config(page_title="Mood Music Recommender", layout="wide")
... st.title("🎵 감정·상황 기반 음악 추천")
... 
... # 1️⃣ 사용자 입력
... mood = st.selectbox("지금 기분은?", ["우울", "기쁨", "설렘"])
... situation = st.selectbox("상황은?", ["비 오는 날", "아침 준비", "밤 산책"])
... place = st.selectbox("장소는?", ["실내", "해변", "도심"])
... 
... # 2️⃣ 추천 로직
... def recommend_tracks(tracks, mood, situation, place):
...     return [t for t in tracks if t["mood"]==mood and t["situation"]==situation and t["place"]==place]
... 
... recommended = recommend_tracks(TRACKS, mood, situation, place)
... 
... # 3️⃣ 결과 출력
... if recommended:
...     for t in recommended:
...         st.subheader(f"{t['title']} - {t['artist']}")
...         st.image(t["image"], use_column_width=True)
... else:
