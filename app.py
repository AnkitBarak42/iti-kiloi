import streamlit as st
import streamlit.components.v1 as components
import os

# ── Page config ──────────────────────────────────────────────
st.set_page_config(
    page_title="ITI Kiloi — Placement System",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Hide ALL Streamlit chrome so it looks like a standalone app ──
st.markdown("""
<style>
  #MainMenu, header, footer,
  [data-testid="stToolbar"],
  [data-testid="stDecoration"],
  [data-testid="stStatusWidget"],
  section[data-testid="stSidebar"] { display: none !important; }

  .stApp { overflow: hidden !important; }

  .block-container {
    padding: 0 !important;
    margin: 0 !important;
    max-width: 100% !important;
  }

  /* Remove the top gap Streamlit adds */
  .stApp > div:first-child { margin-top: 0 !important; }
</style>
""", unsafe_allow_html=True)

# ── Load the HTML app ─────────────────────────────────────────
html_path = os.path.join(os.path.dirname(__file__), "index.html")

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Remove service-worker registration — it won't work inside an iframe
html = html.replace(
    'if("serviceWorker" in navigator) navigator.serviceWorker.register("sw.js").catch(()=>{});',
    '/* Service worker disabled in hosted mode */'
)

# Remove install-banner JS (beforeinstallprompt doesn't fire in iframes)
html = html.replace(
    "window.addEventListener(\"beforeinstallprompt\",e=>{",
    "window.addEventListener(\"__disabled_beforeinstallprompt\",e=>{"
)

# ── Render full-page iframe ───────────────────────────────────
# Uses screen height via JS trick; fallback 900px
components.html(
    f"""
    <script>
      // Tell parent iframe to resize to full viewport height
      const h = window.screen.height;
      window.frameElement && (window.frameElement.style.height = h + 'px');
    </script>
    {html}
    """,
    height=950,
    scrolling=False,
)
