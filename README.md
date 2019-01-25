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

![1](https://user-images.githubusercontent.com/39845657/51756315-0c369400-2104-11e9-8955-9979a52e15e3.JPG)
<img width="200" src=https://user-images.githubusercontent.com/39845657/51756315-0c369400-2104-11e9-8955-9979a52e15e3.JPG>
![2](https://user-images.githubusercontent.com/39845657/51756321-1062b180-2104-11e9-92e4-315d5c49e6d4.JPG)
![3](https://user-images.githubusercontent.com/39845657/51756322-1062b180-2104-11e9-9bad-08b01cd33a59.JPG)
