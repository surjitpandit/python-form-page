import streamlit as st 

name = st.text_input("ENTER YOUR NAME")
fname = st.text_input("ENTER YOUR FATHER NAME")

adr = st.text_area("ENTER YOUR ADDRESS NAME")

classdata = st.selectbox("ENTER YOUR class :",(1,2,3,4,5,6,7,8,9,10))

button = st.button("DONE")
if button:
    st.markdown(f"""YOUR NAME IS :{ name}
Father Name : {fname}
address : {adr}
claas : {classdata}""")
    
    # def local_css(file_name):
    # with open(file_name) as f:
    #     st.markdown(f"<procss>{f.read()}</procss>", unsafe_allow_html=True)


# local_css("procss/pro.css")

with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")


    contact_form = """
    <form action="https://formsubmit.co/surjitpandit13@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
