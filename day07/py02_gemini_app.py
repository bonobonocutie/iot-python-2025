# Tkinter를 클래스화
from tkinter import * # tkinter 모듈에 있는 모든 클래스, 함수, 변수 등을 다 쓰겠다
from tkinter.messagebox import * # 모듈 밑에 있는 모듈을 from tkinter import *로 가져올 수 없음
from tkinter.scrolledtext import *
from tkinter.font import *
import google.generativeai as genai

genai.configure(api_key='AIzaSyD-kN9Q1QooTpgu71kA0qM0Ay02MqAMni4')
model = genai.GenerativeModel('gemini-1.5-flash')


class window(Tk):
    def __init__(self):
        super().__init__() # 부모객체도 같이 초기화
        self.title('제미나이 챗봇 v2.0')
        self.geometry('730x450')
        self.iconbitmap('./image/chatbot.ico')
        # 클래스 작업할 땐 self... 유심히
        self.protocol('WM_DELETE_WINDOW', self.onClosing)
        
        self.initWindow() # 윈도우 화면 초기화 멤버 함수(메서드)

    def initWindow(self):
        self.myFont = Font(family='NanumGothic', size=10)
        self.boldFont = Font(family='NanumGothic', size=10, weight=BOLD, slant=ITALIC)

        self.inputFrame = Frame(self, width=730, height=30, bg='#EFEFEF')
        self.inputFrame.pack(side=BOTTOM, fill=BOTH)

        self.textMessage = Text(self.inputFrame, width=85, height=1, wrap=WORD, font=self.myFont)
        self.textMessage.bind('<Key>', self.keypress)
        self.textMessage.pack(side=LEFT, padx=30)

        self.buttonSend = Button(self.inputFrame, text='전송', bg='green', fg='white', 
                            font=self.myFont, command=self.responseMessage)
        self.buttonSend.pack(side=RIGHT, padx=20, pady=2)

        self.textResult = ScrolledText(self, wrap=WORD, bg='#000000', fg='white', font=self.myFont) # #bg='black'
        self.textResult.pack(fill=BOTH, expand=True)

        self.textResult.tag_configure('user', font=self.boldFont, foreground='yellow')
        self.textResult.tag_configure('ai', font=self.myFont, foreground='skyblue')
        self.textResult.tag_configure('error', font=self.myFont, foreground='red')

        self.textMessage.focus_set()

        self.protocol('WM_DELETE_WINDOW', self.onClosing)

    def keypress(self, event):
        if event.char == '\r':
            self.responseMessage()

    def responseMessage(self):
        # showinfo('실행', 'API를 실행합니다!')
        inputText = self.textMessage.get('1.0', END).strip()

        self.textMessage.delete('1.0', END)

        if inputText:
            try: 
                self.textResult.insert(END, '유저: ', BOLD)
                self.textResult.insert(END, f'{inputText}\n\n', 'user') # 'user' 텍스트 아큐먼트

                ai_response = model.generate_content(inputText)
                response = ai_response.text

                self.textResult.insert(END, '챗봇: ', 'bold')
                self.textResult.insert(END, f'{response}\n\n', 'ai') # 'ai' 텍스트 아규먼트
                
            except Exception as e:
                self.textResult.insert(END, f'Error: {e}\n\n', 'error')

            finally: 
                self.textResult.see(END) # 스크롤텍스트 마지막위치로 스크롤 다운


    def onClosing(self):
        if askyesno('종료확인', '종료하시겠습니까?'):
            self.destroy() # 완전 종료


if __name__ == '__main__':
    print('Tkinter 클래스 시작!')
    app = window() # Tkinter 클래스 객체 생성
    app.mainloop()