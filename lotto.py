# 로또번호 생성기 &  당첨 확인기
# 컴퓨터가 로또번호 6개 당첨번호 지정
# 사용자가 6개를 선택
# 컴퓨터가 입력받은 번호와 당첨 번호를 비교, 등수개산
# 사용자는 로또번호를 체크박스를 통해 선택한다
# /choice_lotto -> 1~45 숫자 체크박스 선택하는 화면,당첨확인 버튼
# /check_lotto -> 선택번호 [...] 확인등수: xx등

import math
from flask import Flask
from flask import request
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
        <h1>로또번호 생성기</h1>
        <a href="/choice_lotto">로또번호 생성기</a>
        '''


@app.route('/choice_lotto')
def choice_lotto():
    checkboxes = ''
    for i in range(1, 46):
        checkboxes += f'<label><input type="checkbox" name="lotto" value="{i}"> {i}</label><br>'

    return f'''
        <h1>로또번호 선택</h1>
        <form action="/check_lotto">
            {checkboxes}
            <button type="submit">당첨 확인</button>
        </form>
    '''



@app.route('/check_lotto')
def check_lotto():
    user_num = request.args.getlist('lotto', type=int)
    if len(user_num) != 6:
        return '로또 번호는 6개를 선택해야 합니다.'
    
    com_num = random.sample(range(1, 46), 6)
    com_num.sort()
    user_num.sort()
    
    matched_numbers = []
    for num in user_num:
        if num in com_num:
            matched_numbers.append(num)
    match_count = len(matched_numbers)
    matched_numbers = ', '.join(map(str, matched_numbers)) if matched_numbers else '없음'
    
    if match_count == 6:
        rank = '1등'
    elif match_count == 5:
        rank = '2등'
    elif match_count == 4:
        rank = '3등'
    elif match_count == 3:
        rank = '4등'
    elif match_count == 2:
        rank = '5등'
    else:
        rank = '꽝'

    return f'''
        <h1>로또 결과</h1>
        <p>당첨 번호: {com_num}</p>
        <p>내가 선택한 번호: {user_num}</p>
        <p>일치하는 번호: {matched_numbers}</p>
        <p>당첨 등수: {rank}</p>
    '''

if __name__ == '__main__':
    app.run(debug=True)