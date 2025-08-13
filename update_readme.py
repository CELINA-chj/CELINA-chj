import random
from datetime import datetime

# 메뉴판
menu_items = [
    ("☕ Coffee", "Keeps me coding past midnight", "💻 Commit × 1"),
    ("🥐 Croissant", "Buttery, flaky, and made with love", "🐍 Python lesson"),
    ("🍰 Cheesecake", "Sweet and rich, like a perfect API", "📚 1 chapter study"),
    ("🍫 Choco Cookie", "Debugging fuel", "🔧 Fixed 3 bugs"),
    ("🍵 Green Tea Latte", "Calm energy for debugging", "💡 1 solved bug"),
    ("🥯 Bagel", "Simple but satisfying", "📦 1 finished feature"),
]

# 추천 프로젝트
projects = [
    ("🍞 Cost Calculator Web App", "재료 원가 계산 웹앱", "https://github.com/CELINA-chj/cost-calculator"),
    ("🍪 Cookie Clicker Clone", "디저트 클릭 게임", "https://github.com/CELINA-chj/cookie-clicker"),
    ("☕ Coffee Timer", "완벽한 브루잉 타이머 앱", "https://github.com/CELINA-chj/coffee-timer"),
    ("🍰 Recipe Manager", "빵과 디저트 레시피 관리 앱", "https://github.com/CELINA-chj/recipe-manager"),
    ("🥖 Bakery POS System", "빵집 판매·결제 시스템", "https://github.com/CELINA-chj/bakery-pos"),
]

# 오늘 날짜
today = datetime.now().strftime("%Y-%m-%d")

# 랜덤 선택
today_menu = random.sample(menu_items, 4)
today_projects = random.sample(projects, 3)

# README 내용 생성
readme_content = f"""
# Bakery Jin 🍞🥐
**Backend Developer in Training | Full-time Baker at Heart**

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
> 오늘의 추천 프로젝트

"""

for name, desc, link in today_projects:
    readme_content += f"- [{name}]({link}) — {desc}\n"

readme_content += """

---

## 📬 Contact
- 📧 Email: your.email@example.com
- 💼 LinkedIn: https://linkedin.com/in/username
- 📝 Blog: https://yourblog.com

---

⭐️ From [Bakery Jin](https://github.com/CELINA-chj)
☕ Coffee + Code + Croissant = The Perfect Day
"""

# README.md에 저장
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

print("README.md updated for Bakery Jin!")
