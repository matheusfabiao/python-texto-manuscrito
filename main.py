import urllib.request
import string
import numpy as np
from PIL import Image
import cv2

char = string.ascii_lowercase
file_code_name = {}

width = 50
height = 0
newwidth = 0
arr = string.ascii_letters
arr = arr + string.digits + "+,.-? "
letss = string.ascii_letters


def getimg(case, col):
    global width, height, back
    try:
        url = (
            "https://raw.githubusercontent.com/Ankit404butfound/HomeworkMachine/master/Image/%s.png"
            % case
        )
        imglink = urllib.request.urlopen(url)
    except:
        url = (
            "https://raw.githubusercontent.com/Ankit404butfound/HomeworkMachine/master/Image/%s.PNG"
            % case
        )
        imglink = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imglink.read()))
    img = cv2.imdecode(imgNp, -1)
    cv2.imwrite(r"%s.png" % case, img)
    img = cv2.imread("%s.png" % case)
    img[np.where((img != [255, 255, 255]).all(axis=2))] = col
    cv2.imwrite("chr.png", img)
    cases = Image.open("chr.png")
    back.paste(cases, (width, height))
    newwidth = cases.width
    width = width + newwidth


def text_to_handwriting(string, rgb=[0, 0, 138], save_to: str = "pywhatkit.png"):
    """Convert the texts passed into handwritten characters"""
    global arr, width, height, back
    try:
        back = Image.open("zback.png")
    except:
        url = "https://raw.githubusercontent.com/Ankit404butfound/HomeworkMachine/master/Image/zback.png"
        imglink = urllib.request.urlopen(url)
        imgNp = np.array(bytearray(imglink.read()))
        img = cv2.imdecode(imgNp, -1)
        cv2.imwrite("zback.png", img)
        back = Image.open("zback.png")
    rgb = [rgb[2], rgb[1], rgb[0]]
    count = -1
    lst = string.split()
    for letter in string:
        if width + 150 >= back.width or ord(letter) == 10:
            height = height + 227
            width = 50
        if letter in arr:
            if letter == " ":
                count += 1
                letter = "zspace"
                wrdlen = len(lst[count + 1])
                if wrdlen * 110 >= back.width - width:
                    width = 50
                    height = height + 227

            elif letter.isupper():
                letter = "c" + letter.lower()
            elif letter == ",":
                letter = "coma"
            elif letter == ".":
                letter = "fs"
            elif letter == "?":
                letter = "que"

            getimg(letter, rgb)

    back.save(f"{save_to}")
    back.close()
    back = Image.open("zback.png")
    width = 50
    height = 0
    return save_to

txt1 = '''
A modalidade dos contratos de locação é regulada pelo Código Civil Brasileiro de 2002 e pela Lei de Inquilinato (Lei nº 8.245/1991). Essas normas estabelecem as regras e direitos relacionados à locação de imóveis, abrangendo tanto locadores (proprietários) quanto locatários (inquilinos).

Segundo o Código Civil, a locação é um contrato bilateral, consensual e oneroso. Por meio desse contrato, o locador se compromete a ceder o uso e gozo de um imóvel ao locatário, mediante o pagamento de um valor estipulado como aluguel. O imóvel objeto da locação pode ter finalidades residenciais, comerciais ou mistas.
'''

txt2 = '''
Para que um contrato de locação seja válido, é necessário que estejam presentes os elementos essenciais, como o consentimento das partes, o objeto lícito (o imóvel) e o pagamento do aluguel. Além disso, existem características importantes da locação, como ser um contrato consensual (não requer formalidades especiais), oneroso (envolve pagamento de aluguel) e bilateral (com obrigações recíprocas).

As modalidades de locação mais comuns são: por tempo determinado, por tempo indeterminado, residencial, comercial e mista. Cada modalidade possui suas particularidades em relação ao prazo, uso do imóvel e direitos e deveres das partes.
'''

txt3 = '''
O contrato de locação deve conter informações relevantes, como a identificação das partes, descrição do imóvel, valor do aluguel, prazo de vigência, forma de reajuste do aluguel, obrigações e direitos das partes, entre outros detalhes específicos.

Quanto às benfeitorias realizadas pelo locatário no imóvel, elas podem ser indenizáveis se forem necessárias, úteis ou voluptuárias e estiverem autorizadas pelo locador. As benfeitorias necessárias são aquelas voltadas à conservação do imóvel, enquanto as úteis proporcionam melhorias no uso do imóvel. Já as benfeitorias voluptuárias têm finalidade estética ou de luxo. A indenização por benfeitorias depende de autorização prévia do locador e de acordo entre as partes.
'''

txt4 = '''
É possível ceder o contrato de locação a terceiros mediante autorização do locador, e o contrato pode ser extinto por diferentes razões, como o término do prazo, denúncia vazia, rescisão por descumprimento contratual, denúncia motivada, acordo entre as partes, desapropriação ou morte de uma das partes.

A Lei de Inquilinato é a legislação específica que regula as relações entre locadores e locatários, abordando questões como reajuste do aluguel, garantias locatícias, despesas de manutenção do imóvel, entre outros aspectos relevantes. É importante consultar tanto o Código Civil quanto a Lei de Inquilinato para obter informações completas sobre os direitos e deveres das partes envolvidas em um contrato de locação.
'''

text_to_handwriting(txt4, save_to="parte-4.png")