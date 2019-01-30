# CSS

20190117



### 크기단위 - 상대값

- `%`  - 같은 h1이라도 상속에 따라 크기 다를 수 있음
- `em` 
- `rem` (root) 어딜가나 1rem은 같은 값, 보통 rem을 많이 쓴다
- `viewport` 반응형 할 때 씀



---



### 색상 표현 단위

- `HEX`
- `RGB`
- `RGBA` : RGB + 투명도



---



### Selector

부모, 부모 자식

- `*` 전체 select
- `.` 클래스 selector
- `#` id selector

> 우선 순위 : id > class > tag > *
>
> 같은 태그에 여러개 먹여도 위 순위대로

**하나의 태그에 클래스 여러개 먹이면 css 파일에서 가장 밑에 있는 애로 먹여짐**



> <!-- <u>span태그와 div 태그</u> :
>
> 둘 다 의미는 없지만 마크업을 해야 css를 적용시킬 수 있기 때문에 사용함
>
> 컴퓨터니까 특정한 곳을 지정해야 함
>
> 따라서 선택자가 필요하고 선택자를 잡기 위해서 마크업이 필요-->



---





기본 루트 픽셀 : 16px

em vs rem



---



### 반응형 viewport

- `vh` : 높이의 1/100
- `vw` :  너비의 1/100



---



### bold 하는 3가지 방법

- css - font-weight: bold;
- <strong>
- <b>

><u>달라지는 점이 뭘까?</u>
>
>tag를 통해 특정 부분을 강조 혹은 볼드체라는 것을 명시! 따라서 단순 볼드체를 하기 위해 strong 태그를 남발하는 경우에는 브라우저가 모든 볼드체를 강조하게 됨
>
>> strong 태그 남발하면 안됨!

따라서, 기본으로 선택자 볼드체를 쓰고 강조가 필요한 부분에 strong 사용                          



---



### Selector 심화

##### A. 형제 선택자 (거의 안쓰인다)

> h1 + p : h1의 형제인 p 셀렉

##### B. 그룹 선택자

> h1, p : h1와 p 셀렉

##### C. 자식 선택자

> ol > li : 직계 자식인 li 셀렉

##### D. 자손 선택자

> ul li : ul 밑의 li 셀렉

##### E. nth-of-type(#)

> ul li:nth-of-type(2) : ul 밑의 li 중 2번째 셀렉



Emmet!!!!!!!!!!!!!! Emmet cheat sheet



---



### display type

- block
  - 항상 새로운 라인에서 시작.
  - 화면 크기 전체의 가로폭을 차지 (width: 100%)
  - block 레벨 요소 내에 inline레벨 요소를 포함할 수 있다
  - 대표적 : 
- inline
  - 새로운 라인에서 시작하지 않음, 문장의 중간에 들어갈 수 있음
  - content의 너비만큼 가로폭을 차지
  - width, height, margin-top, margin-bottom 프로퍼티 지정 불가
  - 상, 하 여백은 line-height로 지정
  - 대표적 : span, a, strong, img, br
- inline-block
  - block과 inline  레벨 요소의 특징을 모두 가짐
  - inline레벨 요소처럼 한 줄에 표시 되면서 block에서의 width, height, margin(top, bottom) 속성을 모두 지정할 수 있다.
- None
  - 해당 요소를 화면에 표시하지 않는다. (공간조차 사라진다)



---



### visibility Property

- visible
  - 해당 요소를 보이게 한다. (기본값)
- hidden
  - 해당 요소를 안 보이게 한다. (공간은 존재한다.)
  - display - None과 차이!



---



### box model

- ```
  기본적으로 width 는 부모의 영향을 받는다.
  div 가 body 의 50% 이므로, p 태그의 영역도 50%.
      <div>
          <p>100% !</p>
      </div>
      <div style="width: 50%">
          <p>50% !</p>
      </div>
  ```

- ```
  box-sizing: (기본값 contents-box)
  box-sizing: border-box > 보더 기준으로 사이즈 맞춤
  ```

- ```css
  .margin-50 {
      margin: 50px 50px 50px 50px;
      /* top right bottom left 시계방향 */
  }
  .margin-50 {
      margin: 25px 50px 25px;
      /* top right&left bottom */
  }
  .margin-50 {
      margin: 25px 25px;
      /* top&bottom left&right */
  }
  .margin-50 {
      margin: 50px;
      /* top&bottom&left&right */
  }
  ```

- ```
  margin: auto; > 오른쪽 왼쪽 반반 나눠줌
  margin-left: auto; > 왼쪽에 남은 너비를 붙인다. (오른쪽정렬)
  ```

- ```CSS
  css는 무조건 사각형으로 시작!
  circle만드려면 사각형 만든 후 border-radius 값 줘서 깎아야 함
  .circle {
      width: 200px;
      height: 200px;
      background-color: darkgoldenrod;
      border-radius: 50%;
  }
  ```







### position

부모 relative로 주고 자식들은 absolute 주면 편하다

fixed : 브라우저 모양 기준으로 바뀜

z-index : 숫자 클 수록 위로(맨 위로/맨 아래로), 부모의 z-index 상속받음



- static

  - 기본값

- relative

  - 현재 위치에서 상하좌우 상대적으로 움질일 수 있게 된다.
  - position  적용 전(static일 때)기준으로 움직임.
  - 움직인 후 원래 있었던 공간이 유지됨.

- absolute

  - 기본 레이어 관계에서 벗어난다. (집 나간 자식. 붕 뜬다)
  - 공간을 유지하지 않기 때문에 다른 도형들도 새로운 자리로 움직이게 된다.
  - 움직인 후 원래 있었던 공간이 사라진다.
  - 부모 영역을 벗어나 자유롭게 어디든 위치할 수 있다.
  - 부모에 static 이외의 position 프로퍼티가 지정되어 있을 경우에만 부모를 기준으로 위치하게 된다. 만약 부모, 조상이 모두 static이면 document body를 기준으로 위치하게 된다.

- fixed

  - absolute랑 동일하게 움직이지만 스크롤이 생길 때 움직이지 않고 고정되어 있다.

  - > TIP: 부모에게 position: relative를 줘서 자식이 absolute를 받을 때 기준점을 부모로 인식하도록 하는 것이 편하다.







## workshop

#### nth-child(n)

- 모든 자식의 순서에서 찾음
- 해당하는 태그의 순서



#### nth-of-type(n)

- 해당하는 자식 태그 요소에서의 순서를 찾음
- 부모 속성에서 특정태그를 가진 자식 속성에서 몇 번째에 해당하는지