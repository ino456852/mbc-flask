# Flask 웹 프레임워크의 필요한 모듈 임포트
from flask import Flask, request, redirect

# Flask 앱 인스턴스 생성
app = Flask(__name__)

# 메모리에 저장할 할 일 목록 리스트
tasks = []

# 고유한 task ID 생성을 위한 카운터
task_id_counter = 1

# 루트 URL 접속 시 출력되는 기본 페이지
@app.route('/')
def hello_world():
    return '''
        <h1>할일관리</h1>
        <a href="/todo_main">할일관리</a>
        '''

# 할 일 목록과 추가 폼을 포함하는 메인 페이지
@app.route('/todo_main')
def todo_main():
    # 기본 HTML 구조 시작
    html = '''
        <!DOCTYPE html>
        <html lang="ko">
        <head>
        <meta charset="UTF-8">
        <title>할 일 관리</title>
        </head>
        <body>

        <h2>📋 할 일 목록</h2>

        <!-- 할 일 추가 폼 -->
        <form action="/todo_add" method="post">
            <label>
            새 할 일:
            <input type="text" name="task" required>
            </label>
            <button type="submit">추가</button>
        </form>

        <hr>

        <ul>
        '''
    # 할 일 목록을 반복해서 HTML로 나열
    for task in tasks:
        html += f'''
            <li>
            <!-- 삭제 요청을 보내는 폼 (숨겨진 ID 포함) -->
            <form action="/todo_del" method="post" style="display:inline;">
                <input type="hidden" name="task_id" value="{task['id']}">
                <button type="submit">완료</button>
            </form>
            {task['text']}
            </li>
            '''
    # HTML 닫기
    html += '''
        </ul>

    </body>
    </html>
    '''
    return html

# 할 일 추가 처리
@app.route('/todo_add', methods=['POST'])
def todo_add():
    global task_id_counter  # 전역 변수 수정 허용
    task_text = request.form.get('task')  # 폼에서 전달된 할 일 텍스트 가져오기
    if task_text:
        # 새로운 할 일을 리스트에 추가
        tasks.append({'id': task_id_counter, 'text': task_text})
        task_id_counter += 1  # 다음 할 일을 위한 ID 증가
    # 작업 후 성공 메시지를 포함한 HTML 반환
    return redirect('/todo_main')
    return '''
        <h3>등록 성공</h3>
        <a href="/todo_main">메인</a>
    '''

# 할 일 삭제 처리
@app.route('/todo_del', methods=['POST'])
def todo_del():
    task_id = int(request.form.get('task_id'))  # 삭제할 할 일 ID 가져오기
    global tasks  # 전역 리스트 수정 허용
    # 해당 ID를 가진 할 일을 제외한 새 리스트 생성
    tasks = [task for task in tasks if task['id'] != task_id]
    # tasks.pop(task_id-1)
    # 작업 후 완료 메시지를 포함한 HTML 반환
    return redirect('/todo_main')
    return '''
        <h3>완료</h3>
        <a href="/todo_main">메인</a>
    '''

# Flask 애플리케이션 실행 (디버그 모드 켜짐)
if __name__ == '__main__':
    app.run(debug=True)
