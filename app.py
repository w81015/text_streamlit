import streamlit as st
import requests

st.title("Google 搜尋結果爬蟲")
st.write("輸入關鍵字，查看前 10 筆搜尋結果。")

# 使用者輸入查詢字串
query = st.text_input("請輸入搜尋關鍵字", "")

# 點擊按鈕觸發請求
if st.button("搜尋"):
    if query.strip():
        with st.spinner("爬取中，請稍候..."):
            # 向 Render 的 API 發送請求
            api_url = "https://your-render-url.onrender.com/scrape"  # 替換為你的 Render URL
            response = requests.post(api_url, json={"query": query})

            if response.status_code == 200:
                results = response.json().get('results', [])
                if results:
                    st.success("搜尋結果：")
                    for result in results:
                        st.write(f"### [{result['title']}]({result['link']})")
                else:
                    st.warning("未找到相關結果。")
            else:
                st.error("爬蟲服務錯誤，請稍後再試！")
    else:
        st.warning("請輸入搜尋關鍵字。")
