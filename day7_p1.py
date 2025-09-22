def isBalanced(s):
    st=[]
    for c in s:
        if c == '(' or c=='{' or c=='[':
            st.append(c)
        else:
            if not st:
                return False
            top=st.pop()
            if (top=='(' and c!=')') or (top=='{' and c!='}') or (top=='[' and c!=']'):
                return False
    return len(st)==0
print(isBalanced("()[{]"))

    
    
            
        