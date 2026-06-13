import streamlit as st
import recommender   # ✅ FIX: no direct import

st.set_page_config(page_title="AI Learning Recommender")

st.title("🎓 Personalized Learning Recommendation System")

# User Inputs
interest = st.selectbox(
    "Select Interest",
    ["AI", "Web Dev", "Programming", "Data Science"]
)

level = st.selectbox(
    "Select Level",
    ["Beginner", "Intermediate", "Advanced"]
)

if st.button("Get Recommendations"):

    # Course Recommendations
    st.subheader("📚 Recommended Courses")
    results = recommender.recommend_courses(interest, level)

    if not results:
        st.warning("No courses found. Try another combination.")
    else:
        for course in results:
            st.write(f"**{course['course_name']}**")
            st.write(f"[Go to Course]({course['link']})")
            st.write("---")

    # Learning Path
    st.subheader("🧠 Learning Path")
    path = recommender.generate_learning_path(interest, level)
    st.text(path)