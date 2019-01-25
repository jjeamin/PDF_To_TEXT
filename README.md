# pdf_to_text
pdf에서 text파일로 변환 후 번역하는 프로그램 입니다.

## library
- pdfminer
  + [튜토리얼](http://www.unixuser.org/~euske/python/pdfminer/programming.html)
  + [GitHub](https://github.com/euske/pdfminer/blob/master/tools/pdf2txt.py)
```  
$ pip install translate
```  
- tqdm
  + pdf -> text 변환 상태바
```  
$ pip install tqdm
```   
- 번역기
  + [translate](https://pypi.org/project/translate/)
```  
$ pip install translate
```  

## 함수

**clean_text_file** </br>
텍스트파일을 깨끗히 손질

**translation** </br>
번역.. pdf단어가 많으면 무료 API로는 한계가 온다 -> 해결방안 생각중

**isExistFile** </br>
이미 바꾼 txt파일이 존재하는지 여부

**pdf2txt** </br>
pdf -> text


## Read
- pdf에 비밀번호가 있을 경우 [Here](https://smallpdf.com/kr/unlock-pdf)
- 하루 최대 약 10000단어..
- txt파일은 손질하지 않고 저장이 됩니다

![one](./img/1.jpg)

![two](./img/2.jpg)

![three](./img/3.jpg)
