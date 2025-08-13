name: Auto Update

on:
  schedule:
    - cron: "0 0 * * *"  # 매일 00:00 UTC 실행
  workflow_dispatch:     # 수동 실행 버튼도 생성

jobs:
  run-script:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.x"

      - name: Install dependencies
        run: pip install -r requirements.txt || true

      - name: Run script
        run: python auto_update.py
