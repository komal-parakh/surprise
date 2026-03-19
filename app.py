import streamlit as st
from datetime import datetime

# ---------- CONFIG ----------
st.set_page_config(page_title="For You 💙", layout="centered")

# ---------- STYLE + ANIMATIONS ----------
st.markdown("""
<style>
.home-box {
    background: white;
    padding: 30px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
    animation: fadeIn 1.2s ease-in-out;
    }
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
    }
body {
    background-color: #EEF4FF;
    overflow-x: hidden;
}

/* titles */
.title {
    text-align: center;
    font-size: 32px;
    font-weight: 600;
}
.subtitle {
    text-align: center;
    color: #4A90E2;
}

/* buttons */
.stButton>button {
    background-color: #4A90E2;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 180px;
}
.stButton>button:hover {
    background-color: #6FA8FF;
    transform: scale(1.05);
    transition: 0.2s;
}

/* navbar */
div[role="radiogroup"] {
    justify-content: center;
    margin-bottom: 20px;
}

/* image hover */
img:hover {
    transform: scale(1.05);
    transition: 0.3s;
}

/* 💖 floating hearts */
.heart {
    position: fixed;
    bottom: -10px;
    color: #4A90E2;
    animation: floatUp 6s linear infinite;
    opacity: 0.6;
}
@keyframes floatUp {
    0% {transform: translateY(0);}
    100% {transform: translateY(-100vh);}
}

/* ✉️ envelope */
.envelope {
    background: #4A90E2;
    color: white;
    padding: 15px;
    border-radius: 10px;
    margin: 10px 0;
    cursor: pointer;
    transition: 0.3s;
}
.envelope:hover {
    transform: scale(1.03);
    background: #6FA8FF;
}
.letter {
    background: white;
    color: black;
    padding: 15px;
    border-radius: 10px;
    margin-top: 5px;
    animation: fadeIn 0.5s ease-in-out;
}
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(-10px);}
    to {opacity: 1; transform: translateY(0);}
}
</style>
""", unsafe_allow_html=True)

# 💖 floating hearts HTML
st.markdown("""
<div class="heart" style="left:10%">💙</div>
<div class="heart" style="left:30%">💙</div>
<div class="heart" style="left:50%">💙</div>
<div class="heart" style="left:70%">💙</div>
<div class="heart" style="left:90%">💙</div>
""", unsafe_allow_html=True)

# ---------- SESSION ----------
if "page" not in st.session_state:
    st.session_state.page = "login"

# envelope states
for i in range(4):
    if f"open_{i}" not in st.session_state:
        st.session_state[f"open_{i}"] = False

# ---------- PASSWORD ----------
PASSWORD = "ILOVEYOU"

# ---------- LOGIN ----------
if st.session_state.page == "login":
    st.markdown('<p class="title">Only for the birthday boy 🎂</p>', unsafe_allow_html=True)
    password = st.text_input("Enter password", type="password")

    if st.button("Unlock"):
        if password == PASSWORD:
            st.session_state.page = "dashboard"
        else:
            st.error("Wrong password 😢")

# ---------- MAIN ----------
elif st.session_state.page == "dashboard":

    # 🎶 music
    st.markdown("### 🎶 Play this first 😏")
    audio_file = open("music.mp3", "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mp3")
    # 🔝 navbar
    menu = st.radio(
        "",
        ["🏠 Home", "📷 Gallery", "🎥 Video", "💌 Letters", "⏳ Time", "❤️ Final"],
        horizontal=True
    )

    # ---------- HOME ----------
    if menu == "🏠 Home":
        import time
        text = "Hey you… 💙"
        placeholder = st.empty()
        for i in range(len(text)):
            placeholder.markdown(f"<h2 style='text-align:center'>{text[:i+1]}</h2>", unsafe_allow_html=True)
            time.sleep(0.05)
        st.markdown('<p class="title">Hey idiot… yeah you ❤️</p>', unsafe_allow_html=True)
        st.markdown('<p class="subtitle">I made this… so you better explore properly 😏</p>', unsafe_allow_html=True)
    
    # ---------- STORY ----------
    elif menu == "📷 Gallery":
        st.markdown('<p class="title">Our Gallery 📖</p>', unsafe_allow_html=True)

        images = [
            "photo1.jpg","1.JPEG","2.JPEG",
            "3.JPEG","4.JPEG","5.JPEG",
            "6.JPEG","7.JPG","8.JPG"
        ]

        cols = st.columns(3)
        for i, img in enumerate(images):
            with cols[i % 3]:
                st.image(img, use_container_width=True)

    # ---------- VIDEO ----------
    elif menu == "🎥 Video":
        st.markdown('<p class="title">This is us 🎥</p>', unsafe_allow_html=True)
        st.video("video.mov")
        st.markdown('<p class="subtitle">Look how cute we are (mostly me)</p>', unsafe_allow_html=True)

    # ---------- 💌 ENVELOPES ----------
    elif menu == "💌 Letters":
        st.markdown('<p class="title">Open When 💌</p>', unsafe_allow_html=True)

        st.markdown("""
        <style>
        .envelope-container {
            perspective: 1000px;
            margin-bottom: 20px;
        }

        .envelope {
            position: relative;
            width: 100%;
            height: 120px;
            background: #0047AB;
            border-radius: 10px;
            cursor: pointer;
            overflow: hidden;
        }

        /* flap */
        .flap {
            position: absolute;
            width: 100%;
            height: 60px;
            background: #0047AB;
            top: 0;
            left: 0;
            transform-origin: top;
            transition: transform 0.6s;
            clip-path: polygon(0 0, 100% 0, 50% 100%);
            z-index: 2;
        }

        .open .flap {
            transform: rotateX(180deg);
        }

        /* letter */
        .letter {
            position: absolute;
            width: 90%;
            left: 5%;
            bottom: 10px;
            background: white;
            color: black;
            padding: 15px;
            border-radius: 10px;
            transform: translateY(100%);
            transition: transform 0.6s;
            z-index: 1;
        }

        .open .letter {
            transform: translateY(0);
        }

        .title-text {
            color: white;
            text-align: center;
            padding-top: 45px;
            font-weight: 600;
        }
        </style>
        """, unsafe_allow_html=True)

        letters = [
        ("When you're sad", """I know you don’t always show it… and that fine. But I just want you to know—you don’t have to handle everything alone.
        I’m always here for you, no matter what. On your worst days, your quiet days, your “leave me alone” days… I’m still not going anywhere. I love you motu ji.
        And you know the worst part you look like chomu but cutu when you are sad. umm honestly i love your look but that doesnt mean you have and you look better
        in smile. So no sad you, only happy and funny you.
        Jii, majak tak thik hai but whenever you are sad just call me or even text me if call not possible, I ll always love to hear whats wrong.💙"""
        ),
        ("When you miss me", """I miss you too… probably I admit that a lot.  Sometimes in the smallest moments, I just randomly think of you and smile like if this idiot was here
        we would have been doing this and that.So if you’re missing me, miss me please. And just know somewhere I’m doing the same… and wishing I could be right there annoying you in person 😏💙"""
        ),
        ("When you can’t sleep","""I wish I could be there with you in those moments… just talking about random things until you fall asleep. And cuddle with you.
        I really want to do that, probably dying to do that.I’d probably be telling you something stupid ofc I talk to much, and you’d pretend to be annoyed—but we both know you like it. 
        So for now, just close your eyes and imagine I’m there… because I would be, if I could 💙"""
        ),
        ("When you feel insecure","""You have no idea how amazing you actually are. Like genuinely. The way you think, the way you care, even the way you annoy me—it all just makes you… you.
        And I wouldn’t change that for anything. So next time you doubt yourself, just remember: I see you differently… and to me, you’re more than enough ❤️. And do not doubt yourself.
        I love the person you are, your nature, and honestly your heart."""
        )
        ]

        for i, (title, content) in enumerate(letters):
            if st.button(f" {title}", key=f"env_btn_{i}"):
                st.session_state[f"open_{i}"] = not st.session_state.get(f"open_{i}", False)

            state = "open" if st.session_state.get(f"open_{i}", False) else ""

            st.markdown(f"""
            <div class="envelope-container">
                <div class="envelope {state}">
                    <div class="flap"></div>
                    <div class="title-text">{title}</div>
                    <div class="letter" style="line-height:1.6; font-size:15px;">{content}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    # ---------- TIME ----------
    elif menu == "⏳ Time":
        st.markdown('<p class="title">Time with you ❤️</p>', unsafe_allow_html=True)

        start_date = datetime(2024, 1, 1)  # CHANGE
        now = datetime.now()

        diff = now - start_date

        st.markdown(f"""
        <p class="subtitle">
        💙 {diff.days} days <br>
        since you became my favorite person
        </p>
        """, unsafe_allow_html=True)


    # ---------- FINAL ----------
    elif menu == "❤️ Final":
        st.markdown('<p class="title">Happy Birthday ❤️</p>', unsafe_allow_html=True)
        st.markdown('<p class="subtitle">I cant promise to fix your problems but I can promise you wont have to face them all alone</p>', unsafe_allow_html=True)
        st.markdown("""
        <p class="subtitle">
        You’re my favorite person… don’t let it get to your head 😏<br><br>
        I love you. Like a lot. Unfortunately 💙
        </p>
        """, unsafe_allow_html=True)
        
