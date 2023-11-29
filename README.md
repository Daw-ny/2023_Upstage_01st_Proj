# 🔜 First Project : 끝말잇기 with python

## Abstract
> 파이썬으로 할 수 있는 프로그램을 구현해본다.

<h3> 🛑 Role & Rule </h3>

> ## 1. 끝말잇기 규칙
> - 플레이어는 입력 기회를 총 3번 부여받습니다.
> - 중복된 단어를 입력할 시 기회를 1회 잃습니다.
> - 두 글자 이상인 단어를 입력하지 않을 시 기회를 1회 잃습니다.
> - 표준국어대사전을 기준으로 없는 단어일 경우 기회를 1회 잃습니다.
> - 처음 턴에 한방단어를 입력할 경우 기회를 1회 잃습니다.
> - 기회 3회 모두 잃을 경우 플레이어의 패배입니다.
>
>
> ## 2. 주의사항
> - 시작할 때 첫 단어가 없는 단어로 나오게 되면 다시 실행해 주시기 바랍니다.
> - 끝나는 단어가 모두 나왔을 때 무한루프로 걸릴 수 있음을 인지해 주시기 바랍니다.
> - 두음법칙 기준에 맞춰 허용될 수 있음을 안내드립니다.
> - 각자의 커스텀에 연결할 경우 이미 저장되어 있는 파일을 각자의 경로를 통해 저장해 주시기 바랍니다. 인식이 안될 수 있습니다.
> - ipynb 파일로 저장되어 있는 딕셔너리를 확인할 수 있습니다. 

<h3> 📽️ Project Intro </h3>

<table>
  <tr>
    <td> <div align=center> <b> Subject </b> </div> </td>
    <td> 파이썬 프로그래밍을 활용하여 각자 만들고 싶은 기능을 선택하여 직접 구현해보기 </td>
  </tr>
  <tr>
    <td> <div align=center> <b> Processing </b> </div> </td>
    <td> 1. 끝말잇기의 규칙이 어떤 것이 있는지 파악하기 </br>
         2. 규칙에 맞춰 진행하되 어떠한 프로세스로 진행할 것인지 계획 </br>
         3. 실행하는 알고리즘 구조를 탄탄하게 잡기
  </td>
  </tr>
  <tr>
    <td> <div align=center> <b> Develop Enviroment </b> </div> </td>
    <td> <tt>Tool</tt>: Open AI, VS Code</td>
  </tr>
  <tr>
    <td> <div align=center> <b> Algorithm </b> </div> </td>
    <td> <tt>image</tt>: 아이디어 브레인 스토밍, 조직도 생성 <a href="https://boardmix.com/"> </td>
  </tr>
</table>

<h3> 📆 Project Procedure </h3>

>  자세한 진행 내용은 [velog](https://velog.io/@wise_head/첫번째-프로젝트-끝말잇기)에서 확인하실 수 있습니다.

<h3> 📂 Project Structure </h3>

> - personal_project
>> 2.crawling.ipynb
>> - 실습때 사용한 코드입니다. 각종 실습 내용이 들어 있습니다.
>>
>> crawling_word.pickle
>> - 크롤링하여 쓸 수 있는 단어를 저장해 두었습니다. 이로써 속도를 개선할 수 있습니다.
>>
>> oneturn.pickle
>> - 한방단어를 dictionary형태로 모아뒀습니다.
>>
>> word.pickle
>> - 사용하였던 단어를 모두 모아뒀습니다.
>>
>> 끝말잇기.py
>> - 코드가 작동하는 메인 파일이며 각종 코드와 함수가 담겨있습니다.
>>
>> 한글_단어_크롤링.ipynb
>> - 크롤링 샘플 코드가 담겨있으며, pickle파일 생성시 활용하였습니다.

<h3> ⚙️ Architecture </h3>
<table>
  <tr>
    <td> <div align=center> <b> 분류 </b> </div> </td>
    <td> <div align=center> <b> 내용 </b> </div> </td>
  </tr>
  <tr>
    <td> <div align=center> <b> 구현 패키지 </b> </div> </td>
    <td> <tt>collections</tt>, <tt>requests</tt>, <tt>json</tt>, <tt>hgtk</tt>, <tt>pickle</tt> </td>
  </tr>
  <tr>
    <td> <div align=center> <b> 데이터 </b> </div> </td>
    <td> 표준대국어사전 API </td>
  </tr>
</table>

