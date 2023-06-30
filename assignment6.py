def ds(roll_no, name):
    a = [roll_no, name]
    b = (roll_no, name)
    c = {roll_no, name}
    d = {
        'roll': roll_no,
        'name': name
    }
    print(f"""    
    {a}
    {b}
    {c}
    {d}
    """)
    a[0] = 32
    a[1] = 'Hello'

    b = (324, 'yoyoy')

    c.clear()
    c.update([324, 'lalalal'])

    d['roll'] = 34
    d['name'] = 'Hello'

    print(f"""    
    {a}
    {b}
    {c}
    {d}
    """)


ds(3242, 'lalalalalal')