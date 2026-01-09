import streamlit as st
import yt_dlp

# Page configuration
st.set_page_config(
    page_title="My Private Music Player",
    page_icon="🎵"
)

st.title("🎧 My Personal Ad-Free Music Player")
st.write("Bollywood, Punjabi, ya English gaane search karein aur sunein.")

# Search bar
search_query = st.text_input(
    "Gaane ka naam likhein (e.g. 'Sidhu Moose Wala' ya 'Arijit Singh'):"
)

if search_query:
    try:
        # yt-dlp options
        ydl_opts = {
            'format': 'bestaudio/best',
            'noplaylist': True,
            'quiet': True,
            'default_search': 'ytsearch1',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(search_query, download=False)
            video_info = info['entries'][0]

            audio_url = video_info['url']
            title = video_info['title']
            thumbnail = video_info.get('thumbnail', '')

        # Display Results
        st.subheader(f"🎶 Playing: {title}")

        if thumbnail:
            st.image(thumbnail, width=300)

        # Audio Player
        st.audio(audio_url, format="audio/mp3")
        st.success("Gaana load ho gaya hai. Enjoy! 🎉")

    except Exception as e:
        st.error(f"Kuch galti hui: {e}")

st.divider()
st.caption("Made for personal use — No Ads, No Tracking.")
