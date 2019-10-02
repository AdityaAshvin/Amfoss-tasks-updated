try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

x = pytesseract.image_to_string(Image.open('./Home/Desktop/cap.png'))
f = int(x[0:1])
l = int(x[2:3])
if '/' in x:
    div = f/l
    print(div)
elif '+' in x:
    su = f+l
    print(su)
elif '-' in x:
    sub = f-l
    print(sub)
elif '*' in x:
    mul = f*l
    print(mul)

    



