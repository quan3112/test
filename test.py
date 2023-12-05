x=float(input('nhập số kw tiêu thụ'))
if x<=50:
    print(x*1.678)
else:
    if x<=100:
        print(x*1.678+(x-50)*1.734)
    else:
        print(x*50+x*50+(x-100*2.111))