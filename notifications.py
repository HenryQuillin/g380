from streamlit.components.v1 import html


def setup_notifications(title, body, icon, url):
    # remove newlines and quotes in the body
    escaped_body = body.replace("\n", "\\n").replace("'", "\\'").replace('"', '\\"')
    # we need to use js to trigger a notification
    return f"""
    if (!("Notification" in window)) {{
        alert("This browser does not support desktop notification");
    }} else if (Notification.permission === "granted") {{
        var notification = new Notification("{title}", {{
            body: "{escaped_body}",
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
                    body: "{escaped_body}",
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


def show_notification(title, body, icon="https://img.icons8.com/?size=100&id=12452&format=png&color=000000.png",
                      url="http://localhost:8501/my_alerts"):
    notification_js = setup_notifications(title, body, icon, url)
    notification_html = f"<script>{notification_js}</script>"
    html(notification_html)


def create_notifications(articles):
    if articles:
        if len(articles) == 1:
            title = f"News Alert: {articles[0]['title']}"
            body = articles[0]['description'][:100].replace("\n", " ") + "..."
        else:
            title = f"News Alert: {articles[0]['title']}"
            body = f"+{len(articles) - 1} other news alerts"

        show_notification(title, body)