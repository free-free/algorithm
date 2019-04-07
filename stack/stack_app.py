


from stack import ArrayStack, LinkTableStack



def check_parentheses(string):

    st = LinkTableStack()
    is_valid = True
    for s in string:
        if s == '(':
            st.push(s)
        if s == ')':
            st.pop()

    if st.top() is not None:
        is_valid = False
    return is_valid


if __name__ == '__main__':
    print(check_parentheses('((1+3)*(4+3))'))
    print(check_parentheses('((1+3)*(4+3)'))


