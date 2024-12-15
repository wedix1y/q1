import streamlit as st
def house(password):
    count_spec_symbol = 0
    count_numbers = 0
    count_upper = 0
    for symbol in password:
        if symbol in '!@#$%^&*()_+;:?-=|':
            count_spec_symbol += 1
        if symbol in 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
            count_upper += 1
        if symbol in '0123456789':
            count_numbers += 1
    if len(password) < 7:
        st.text('пароль должен содержать как минимум 7 символов')
    elif len(password) > 40:
        st.text('пароль должен содержать максимум 40 символов')
    elif '_' not in password:
        st.text('пароль должен содержать символ "_"')
    elif '9' not in password:
        st.text('пароль должен содержать цифру"9"')
    elif 'Q' not in password:
        st.text('пароль должен содержать букву "Q"')
    elif '1799' not in password:
        st.text('пароль должен содержать год рождения Пушкина')
    elif 'T' not in password:
        st.text('пароль должен содержать 20 букву английского алфавита')
    elif '1240' not in password:
        st.text('пароль должен содержать год Невской битвы')
    elif '@' in password:
        st.text('пароль не должен содержать символ "@"')

    elif count_spec_symbol < 2:
        st.text('пароль должен содержать как минимум 2 символа')
    elif count_numbers < 5:
        st.text('пароль должен содержать как минимум 5 цифр')
    elif count_upper < 6:
        st.text('пароль должен содержать как минимум 6 заглавных букв')

    else:
        st.text('поздравляю, пароль создан')

st.markdown("<h1 style='text-align: center; color: pink;'>Password game</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white;'>"
"I am here to help you to create the strongest password in the world</p>", unsafe_allow_html=True)

w = st.text_input('enter a password', max_chars=35)
house(w)



