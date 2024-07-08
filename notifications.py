# notifications.py

from streamlit.components.v1 import html

def create_notification_js(title, body, icon, url):
    return f"""
    if (!("Notification" in window)) {{
        alert("This browser does not support desktop notification");
    }} else if (Notification.permission === "granted") {{
        var notification = new Notification("{title}", {{
            body: "{body}",
            icon: "{icon}"
        }});
        notification.onclick = function(event) {{
            event.preventDefault();
            window.open("{url}", "_blank");
        }}
    }} else if (Notification.permission !== "denied") {{
        Notification.requestPermission().then(function (permission) {{
            if (permission === "granted") {{
                var notification = new Notification("{title}", {{
                    body: "{body}",
                    icon: "{icon}"
                }});
                notification.onclick = function(event) {{
                    event.preventDefault();
                    window.open("{url}", "_blank");
                }}
            }}
        }});
    }}
    """

def show_notification(title, body, icon="https://img.icons8.com/?size=100&id=12452&format=png&color=000000.png", url="http://localhost:8501/News"):
    notification_js = create_notification_js(title, body, icon, url)
    notification_html = f"<script>{notification_js}</script>"
    html(notification_html)