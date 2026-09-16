import streamlit as st
from joke_generator import JokeGenerator
import time

st.set_page_config(
    page_title="Random Joke Generator",
    page_icon="😂",
    layout="wide"
)

st.title("😂 مولد النكات العشوائي")
st.write("احصل على نكات عشوائية مضحكة من مصادر مختلفة حول العالم")

# تهيئة مولد النكات
generator = JokeGenerator()

# الشريط الجانبي
with st.sidebar:
    st.header("⚙️ الإعدادات")
    mode = st.radio(
        "اختر الوضع",
        ["نكتة واحدة", "عدة نكات", "نكتة من فئة", "مفاجأة"]
    )
    
    if mode == "عدة نكات":
        joke_count = st.slider("عدد النكات", 1, 10, 5)

# التبويبات الرئيسية
tab1, tab2, tab3 = st.tabs(["🎭 النكات", "📊 الإحصائيات", "ℹ️ عن التطبيق"])

with tab1:
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.header("الحصول على نكتة")
    
    with col2:
        if st.button("🔄 تحديث", key="refresh_btn"):
            st.rerun()
    
    if mode == "نكتة واحدة":
        st.subheader("نكتة عشوائية")
        if st.button("احصل على نكتة عشوائية", key="single_joke"):
            with st.spinner("⏳ جاري البحث عن نكتة مضحكة..."):
                joke = generator.get_random_joke()
                
                if 'error' not in joke:
                    st.success("✅ تم العثور على نكتة!")
                    
                    with st.container(border=True):
                        if joke.get('type') == 'single':
                            if 'joke' in joke:
                                st.write(f"**النكتة:** {joke['joke']}")
                            elif 'setup' in joke:
                                st.write(f"**الجزء الأول:** {joke['setup']}")
                                st.write(f"**الجزء الثاني:** {joke['punchline']}")
                        else:
                            st.write(f"**الجزء الأول:** {joke['setup']}")
                            st.write(f"**الجزء الثاني:** {joke['delivery']}")
                        
                        st.caption(f"📌 المصدر: {joke.get('source', 'Unknown')}")
                else:
                    st.error(f"❌ خطأ: {joke['error']}")
    
    elif mode == "عدة نكات":
        st.subheader(f"🎯 {joke_count} نكات عشوائية")
        if st.button(f"احصل على {joke_count} نكات", key="multiple_jokes"):
            with st.spinner(f"⏳ جاري البحث عن {joke_count} نكات مضحكة..."):
                jokes = generator.get_multiple_jokes(joke_count)
                
                for i, joke in enumerate(jokes, 1):
                    with st.container(border=True):
                        st.write(f"**النكتة #{i}**")
                        
                        if 'error' not in joke:
                            if joke.get('type') == 'single':
                                if 'joke' in joke:
                                    st.write(f"{joke['joke']}")
                                elif 'setup' in joke:
                                    st.write(f"{joke['setup']}")
                                    st.write(f"{joke['punchline']}")
                            else:
                                st.write(f"{joke['setup']}")
                                st.write(f"{joke['delivery']}")
                            
                            st.caption(f"📌 المصدر: {joke.get('source', 'Unknown')}")
                        else:
                            st.warning(f"❌ {joke['error']}")
    
    elif mode == "نكتة من فئة":
        st.subheader("نكتة من فئة محددة")
        
        categories = [
            'Programming',
            'Misc',
            'Knock-Knock',
            'General',
            'Spooky',
            'Dark'
        ]
        
        selected_category = st.selectbox(
            "اختر فئة النكتة",
            categories
        )
        
        if st.button(f"احصل على نكتة من فئة {selected_category}", key="category_joke"):
            with st.spinner(f"⏳ جاري البحث عن نكتة {selected_category}..."):
                joke = generator.get_category_joke(selected_category)
                
                if 'error' not in joke:
                    st.success("✅ تم العثور على نكتة!")
                    
                    with st.container(border=True):
                        if joke.get('type') == 'single':
                            st.write(f"**النكتة:** {joke.get('joke', '')}")
                        else:
                            st.write(f"**الجزء الأول:** {joke.get('setup', '')}")
                            st.write(f"**الجزء الثاني:** {joke.get('delivery', '')}")
                        
                        st.caption(f"📌 الفئة: {selected_category}")
                else:
                    st.error(f"❌ {joke['error']}")
    
    elif mode == "مفاجأة":
        st.subheader("🎲 مفاجأة! احصل على نكتة عشوائية تماماً")
        if st.button("اضغط للحصول على مفاجأة!", key="surprise_joke"):
            with st.spinner("🎲 يتم اختيار نكتة عشوائية..."):
                time.sleep(1)  # تأثير الانتظار
                
                joke = generator.get_random_joke()
                
                if 'error' not in joke:
                    st.balloons()  # تأثير بصري
                    st.success("✅ هناك نكتة مفاجأة لك!")
                    
                    with st.container(border=True):
                        if joke.get('type') == 'single':
                            if 'joke' in joke:
                                st.write(f"😂 {joke['joke']}")
                            elif 'setup' in joke:
                                st.write(f"**الجزء الأول:** {joke['setup']}")
                                time.sleep(1)
                                st.write(f"**الجزء الثاني:** 🎉 {joke['punchline']}")
                        else:
                            st.write(f"**الجزء الأول:** {joke['setup']}")
                            time.sleep(1)
                            st.write(f"**الجزء الثاني:** 🎉 {joke['delivery']}")
                        
                        st.caption(f"📌 المصدر: {joke.get('source', 'Unknown')}")
                else:
                    st.error(f"❌ {joke['error']}")

with tab2:
    st.header("📊 الإحصائيات والمعلومات")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("واجهات برمجية متاحة", 3, "APIs")
    
    with col2:
        st.metric("فئات نكات", 6, "Categories")
    
    with col3:
        st.metric("أوضاع مختلفة", 4, "Modes")
    
    st.subheader("مصادر النكات:")
    sources = [
        {"name": "Official Joke API", "url": "https://official-joke-api.appspot.com", "description": "مكتبة ضخمة من النكات الإنجليزية"},
        {"name": "JokeAPI", "url": "https://v2.jokeapi.dev", "description": "واجهة برمجية متقدمة للنكات مع فئات"},
        {"name": "icanhazdadjoke", "url": "https://icanhazdadjoke.com", "description": "متخصصة في Dad Jokes الكلاسيكية"},
    ]
    
    for source in sources:
        with st.container(border=True):
            st.write(f"**{source['name']}**")
            st.write(source['description'])
            st.caption(f"🔗 {source['url']}")

with tab3:
    st.header("ℹ️ عن هذا التطبيق")
    
    st.markdown("""
    ### 📝 وصف التطبيق
    تطبيق ويب تفاعلي لتوليد النكات العشوائية من عدة مصادر خارجية موثوقة.
    يجمع بين ثلاث واجهات برمجية مختلفة للحصول على نكات متنوعة ومضحكة.
    
    ### ✨ المميزات
    - 🎭 نكتة واحدة عشوائية
    - 📚 عدة نكات دفعة واحدة
    - 🏷️ نكات من فئات محددة
    - 🎲 وضع المفاجأة
    - 🌍 نكات بلغات مختلفة
    - ⚡ سرعة عالية في التحميل
    
    ### 🛠️ التكنولوجيا المستخدمة
    - **Streamlit**: واجهة ويب تفاعلية
    - **Requests**: للتواصل مع الواجهات البرمجية
    - **Python 3.8+**: لغة البرمجة
    
    ### 📊 واجهات برمجية خارجية
    1. **Official Joke API** - نكات عامة متنوعة
    2. **JokeAPI** - نكات مصنفة حسب الفئة
    3. **icanhazdadjoke** - Dad Jokes الكلاسيكية
    
    ### 👨‍💻 المطور
    تم تطويره بواسطة: **ahmedibc10**
    
    ### 📞 التواصل
    للإبلاغ عن أي مشاكل أو اقتراحات:
    👉 https://github.com/ahmedibc10/random-joke-generator/issues
    """)
    
    st.divider()
    
    st.info("""
    💡 **نصيحة**: استخدم وضع "المفاجأة" للحصول على تجربة أكثر متعة!
    """)