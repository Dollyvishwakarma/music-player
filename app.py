import streamlit as st
import yt_dlp

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Aj Music Pro", layout="wide")

# ---------------- CSS (Spotify Style) ----------------
st.markdown("""
    <style>
    .stApp { background-color: #121212; color: white; }
    .profile-img { border-radius: 50%; width: 120px; height: 120px; border: 3px solid #1DB954; box-shadow: 0 4px 20px rgba(29, 185, 84, 0.5); }
    .stButton>button { border-radius: 20px; background-color: #282828; color: white; border: 1px solid #1DB954; transition: 0.3s; width: 100%; }
    .stButton>button:hover { background-color: #1DB954; color: black; }
    </style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
c1, c2, c3 = st.columns([1,1,1])
with c2:
    st.markdown(f'<center><img src="https://i.postimg.cc/rpd79wYM/IMG-20220517-WA0009.jpg" class="profile-img"></center>', unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Aj Pro Player</h2>", unsafe_allow_html=True)

st.write("---")

# ---------------- MOOD SHORTCUTS ----------------
st.subheader("Explore Moods")
m1, m2, m3, m4 = st.columns(4)
mood_search = ""
if m1.button("🔥 Party Hits"): mood_search = "Latest Punjabi Party Songs"
if m2.button("🎸 Sad Vibes"): mood_search = "Hindi Sad Songs"
if m3.button("💪 Gym Beast"): mood_search = "Punjabi Gym Workout Songs"
if m4.button("🌙 Relaxing"): mood_search = "Lo-fi Hindi Chill"

# ---------------- SEARCH BAR ----------------
user_query = st.text_input("", placeholder="Gaana ya Singer ka naam likhein...", value=mood_search)

# ---------------- FUNCTION TO DISPLAY SONGS ----------------
def display_songs(query):
    ydl_opts = {
        'quiet': True,
        'default_search': 'ytsearch6',
        'skip_download': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            results = ydl.extract_info(query, download=False)['entries']

            for song in results:
                video_id = song.get('id')
                title = song.get('title')
                uploader = song.get('uploader')
                thumbnail = song.get('thumbnail')

                st.markdown("### 🎵 " + title)
                st.markdown(f"<small style='color:gray'>{uploader}</small>", unsafe_allow_html=True)
                st.image(thumbnail, use_container_width=True)

                # ---------------- YOUTUBE EMBED PLAYER ----------------
                st.markdown(
                    f"""
                    <iframe width="100%" height="80"
                    src="https://www.youtube.com/embed/{video_id}"
                    frameborder="0"
                    allow="autoplay; encrypted-media">
                    </iframe>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown("---")

        except Exception:
            st.error("YouTube se data load nahi ho raha. Thodi der baad try karein.")

# ---------------- RUN FUNCTION ----------------
if user_query:
    display_songs(user_query)
else:
    st.info("Gaana search karein aur enjoy karein!")
