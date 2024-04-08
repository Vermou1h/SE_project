from kivy.core.text import LabelBase

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
import app_function

LabelBase.register(name='Roboto',fn_regular='./STHeiti Medium.ttc')

# 定义不同的屏幕
class IntroScreen(Screen):
    pass


class GradeSelectionScreen(Screen):
    pass


class ExerciseScreen(Screen):
    def __init__(self, **kwargs):
        super(ExerciseScreen, self).__init__(**kwargs)
        self.page = 0  # 当前页码
        self.total_pages = 3  # 总页数

        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # 使用 ScrollView 包裹 GridLayout
        self.questions_scroll_view = ScrollView(size_hint=(1, None), size=(Window.width, Window.height * 0.8))
        self.questions_scroll_view.do_scroll_x = False  # 禁用水平滚动
        self.questions_layout = GridLayout(cols=1, spacing=10, size_hint_y=None, pos_hint={'center_x': 0.5,'center_y':0.5})
        self.questions_layout.bind(minimum_height=self.questions_layout.setter('height'))

        self.questions_scroll_view.add_widget(self.questions_layout)
        main_layout.add_widget(self.questions_scroll_view)

        # 控制按钮布局
        control_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        self.prev_btn = Button(text='上一页', on_press=self.prev_page)
        self.next_btn = Button(text='下一页', on_press=self.next_page)
        self.submit_btn = Button(text='提交', on_press=self.submit_answers)
        # 初始时“返回”按钮不显示
        self.back_btn = Button(text="返回", opacity=0, disabled=True, size_hint_y=None, height=50,
                               on_press=self.restart)

        # 添加按钮到布局
        control_layout.add_widget(self.prev_btn)
        control_layout.add_widget(self.next_btn)
        control_layout.add_widget(self.submit_btn)
        control_layout.add_widget(self.back_btn)

        main_layout.add_widget(control_layout)

        self.add_widget(main_layout)
        self.problems = []
        self.user_answers = {}
        self.populate_questions()

    def restart(self, instance):
        # 重置题目或其他状态
        # ...这里可以添加重置题目的代码或其他需要重置的状态...
        self.prev_btn.opacity = 1
        self.prev_btn.disabled = False
        self.next_btn.opacity = 1
        self.next_btn.disabled = False
        self.submit_btn.opacity = 1
        self.submit_btn.disabled = False

        # 显示“返回”按钮
        self.back_btn.opacity = 0
        self.back_btn.disabled = True
        # 切换到初始屏幕
        App.get_running_app().root.current = 'intro'
    def set_grade(self, grade):
        # 根据年级生成算式
        self.problems = app_function.generate_arithmetic_problems(grade, 10 ,1)  # 假设每个年级生成32个算式
        self.problems = self.problems[:30]
        self.page = 0  # 重置到第一页
        self.total_pages = len(self.problems) // 10  # 计算总页数
        self.populate_questions()
    def populate_questions(self):
        self.questions_layout.clear_widgets()
        # 计算当前页的算式范围
        start = self.page * 10
        end = start + 10
        for index, problem in enumerate(self.problems[start:end], start=start):
            question_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=60, pos_hint={'center_x': 0.5})
            equation_text = f"{problem.num1} {problem.operator} {problem.num2} = "
            equation_label = Label(text=equation_text, size_hint=(None, 1), width=300, font_size='24sp')

            # 将index传递给TextInput，然后使用一个具体的函数来处理文本更改
            answer_input = TextInput(text=self.user_answers.get(index, ''), multiline=False, size_hint=(None, 1),
                                     width=150, font_size='24sp')
            answer_input.bind(text=self.create_answer_input_callback(index))

            question_box.add_widget(equation_label)
            question_box.add_widget(answer_input)

            self.questions_layout.add_widget(question_box)

    def create_answer_input_callback(self, index):
        """生成一个闭包来捕获当前index并更新用户答案"""

        def update_answer(instance, value):
            self.user_answers[index] = value

        return update_answer

    def prev_page(self, instance):
        if self.page > 0:
            self.page -= 1
            self.populate_questions()

    def next_page(self, instance):
        if self.page < self.total_pages - 1:
            self.page += 1
            self.populate_questions()

    def submit_answers(self, instance):
        # 先清除之前的所有问题和答案，为显示比对结果做准备
        self.questions_layout.clear_widgets()
        count=0
        percentage=0
        for index, problem in enumerate(self.problems):
            user_answer = self.user_answers.get(index, "未作答")
            correct_answer = problem.answer
            if user_answer == correct_answer:
                count=count+1
        percentage=count/30*100
        question_text = f"你的正确率为{percentage}%!  你答对了{count}题，答错了{30-count}题。"
        result_label = Label(text=question_text, size_hint_y=None, height=70)
        self.questions_layout.add_widget(result_label)

        # 遍历所有问题，比对答案
        for index, problem in enumerate(self.problems):
            user_answer = self.user_answers.get(index, "未作答")
            correct_answer = problem.answer  # 假设每个problem对象有一个answer属性存储正确答案

            # 生成问题和答案的文本
            if user_answer == correct_answer:
                t = '做对啦！ :) '
            else:
                t ='做错啦！ :( '

            if user_answer == "未作答" :
                t = ' '
            question_text = f"{problem.num1} {problem.operator} {problem.num2} = {correct_answer} (正确答案) / 你的答案: {user_answer}     {t}"

            # 创建一个Label来显示比对结果
            result_label = Label(text=question_text, size_hint_y=None, height=100)
            self.questions_layout.add_widget(result_label)
        self.prev_btn.opacity = 0
        self.prev_btn.disabled = True
        self.next_btn.opacity = 0
        self.next_btn.disabled = True
        self.submit_btn.opacity = 0
        self.submit_btn.disabled = True

        # 显示“返回”按钮
        self.back_btn.opacity = 1
        self.back_btn.disabled = False

# 创建应用
class MathQuizApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(IntroScreen(name='intro'))
        sm.add_widget(GradeSelectionScreen(name='grade_selection'))
        sm.add_widget(ExerciseScreen(name='exercise'))

        return sm

    def handle_grade_selection(self, grade_text):
        # 定义年级文本到数字的映射
        grade_mapping = {
            '一年级上': 1,
            '一年级下': 2,
            '二年级上': 3,
            '二年级下': 4,
            '三年级上': 5,
            '三年级下': 6,
            '四年级上': 7,
            '四年级下': 8,
            '五年级上': 9,
            '五年级下': 10,
            '六年级上': 11,
            '六年级下': 12
        }

        # 根据年级文本获取对应的年级编号
        grade_num = grade_mapping.get(grade_text, 1)  # 默认为1，如果grade_text不在映射中

        # 调用set_grade方法设置年级，并生成相应的题目
        exercise_screen = self.root.get_screen('exercise')

        # 调用ExerciseScreen实例的set_grade方法
        exercise_screen.set_grade(grade_num)

        # 切换到ExerciseScreen
        self.root.current = 'exercise'

if __name__ == '__main__':
    MathQuizApp().run()
