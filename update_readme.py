import random
from datetime import datetime

# 여러 종류의 빵 ASCII 아트
bread_arts = [
    r"""
       ______
     /        \
    |  ☕🥐  |
     \ ______ /
     //      \\
    ((        ))
     \\______/
    """,
    r"""
     ______
    /      \
   |  🥖   |
    \______/
    //    \\
   ((      ))
    \\____//
    """,
    r"""
      ,,,,,,
     | o  o |
    (   ∆   )
     | --- |
      '"""'
    """,
    r"""
      _______
     /       \
    |  🍰   |
     \_______/
     //     \\
    ((       ))
     \\_____//
    """,
    r"""
     ______
    /      \
   |  🥯   |
    \______/
    //    \\
   ((      ))
    \\____//
    """
]

# 메뉴판
menu_items = [
    ("☕ Coffee", "Keeps me coding past midnight", "💻 Commit × 1"),
    ("🥐 Croissant", "Buttery, flaky, and made with love", "🐍 Python lesson"),
    ("🍰 Cheesecake", "Sweet and rich, like a perfect API", "📚 1 chapter study"),
    ("🍫 Choco Cookie", "Debugging fuel", "🔧 Fixed 3 bugs"),
    ("🍵 Green Tea Latte", "Calm energy for debugging", "💡 1 solved bug"),
    ("🥯 Bagel", "Simple but satisfying", "📦 1 finished feature")
]

# 프로젝트 추천(링크의 본인아이디 꼭 바꾸기!)
projects = [
    ("🍞 Cost Calculator Web App", "제빵사들을 위한 재료 원가 계산 웹앱", "https://github.com/CELINA-chj/cost-calculator"),
    ("🍪 Cookie Clicker Clone", "디저트를 클릭해서 포인트를 모으는 귀여운 게임", "https://github.com/CELINA-chj/cookie-clicker"),
    ("☕ Coffee Timer", "완벽한 브루잉을 위한 타이머 앱", "https://github.com/CELINA-chj/coffee-timer"),
    ("🍰 Recipe Manager", "빵과 디저트 레시피 관리 앱", "https://github.com/CELINA-chj/recipe-manager"),
    ("🥖 Bakery POS System", "빵집 전용 판매·결제 시스템", "https://github.com/CELINA-chj/bakery-pos")
]

today = datetime.now().strftime('%Y-%m-%d')
today_menu = random.sample(menu_items, 4)
today_projects = random.sample(projects, 3)
today_bread_art = random.choice(bread_arts)

readme_content = f"""
<h1 align="center">☕ Welcome to Hyejin's Coding Café 🥐</h1>
<h3 align="center">Backend Developer in Training | Full-time Baker at Heart</h3>

<pre align="center">
{today_bread_art}
</pre>

---

## 📝 Today's Special ({today})
| 메뉴 | 설명 | 가격 |
|------|------|------|
"""

for name, desc, price in today_menu:
    readme_content += f"| {name} | {desc} | {price} |\n"

readme_content += """

---

## 🌟 Today's Recommendation
> 오늘의 추천 프로젝트는 셰프의 자랑이에요! 🥖✨

"""

for name, desc, link in today_projects:
    readme_content += f"- [{name}]({link}) — {desc}\n"

readme_content += """

---

## 📬 Contact the Chef
- 📧 Email: your.email@example.com
- 💼 LinkedIn: https://linkedin.com/in/username
- 📝 Blog: https://yourblog.com

---

⭐️ From [Hyejin's Coding Café](https://github.com/CELINA-chj)  
☕ Coffee + Code + Croissant = The Perfect Day
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

print("README.md updated with today's fresh menu and random bread art!")
