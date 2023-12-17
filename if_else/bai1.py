x = int(input('Nhap nam'))
if x % 4 ==0:
    if x % 100 ==0:
        if x % 400 !=0:
            print(x,'không phải là Nam nhuan')
    else:
        print(x,' phai nam nhuan')
else:
  print(x,'Khong phai nam nhuan')