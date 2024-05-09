from kivy.core.text import LabelBase
from kivy_garden.graph import Graph, LinePlot
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
import app_function
from kivy.uix.popup import Popup

from kivy.graphics import Rectangle, Color
LabelBase.register(name='Roboto',fn_regular='./STHeiti Medium.ttc')

# 定义不同的屏幕
class LoginScreen(Screen):


    def check_credentials(self):
        username = self.ids.username_input.text  # 通过 ids 访问
        password = self.ids.password_input.text  # 通过 ids 访问
        # 这里添加验证逻辑
         # 假设的用户名和密码
        self.manager.current = 'intro'



class IntroScreen(Screen):
    pass

import random

class ErrorLogScreen(Screen):
    def on_enter(self):
        # This method is called when you navigate to the ErrorLogScreen
        self.load_problems()

    def load_problems(self):
        # Generate 10 random arithmetic problems with random operations and numbers
        operations = ['+', '-', '*']
        self.problems = [
            f"{random.randint(1, 20)} {random.choice(operations)} {random.randint(1, 20)} = ?"
            for _ in range(20)
        ]
        problems_grid = self.ids.problems_grid
        problems_grid.clear_widgets()  # Clear previous problems
        for problem in self.problems:
            problems_grid.add_widget(Label(text=problem, size_hint_y=None, height=70,font_size='50'))

    def clear_problems(self):
        # Clear the displayed problems
        self.ids.problems_grid.clear_widgets()

    def show_development_popup(self):
        popup = Popup(title='错题分类',
                      content=Label(text='此功能尚在开发中！'),
                      size_hint=(None, None), size=(400, 200))
        popup.open()


class StatsScreen(Screen):
    def on_enter(self):
        # 清除旧数据
        random.seed(42)
        self.ids.stats_layout.clear_widgets()

        # 清除图表数据
        self.ids.stats_graph.plots = []

        # 重新创建图表数据
        correct_counts = [random.randint(15, 30) for _ in range(10)]
        correct_rates = [count / 30 * 100 for count in correct_counts]

        for i, (count, rate) in enumerate(zip(correct_counts, correct_rates), start=1):
            label = Label(text=f"您第{i}次做题时，答对了{count}道题，正确率为{rate:.1f}%", size_hint_y=None, height=40)
            self.ids.stats_layout.add_widget(label)

        # 重新添加图表
        plot = LinePlot(line_width=1.5, color=[1, 0, 0, 1])
        plot.points = [(i + 1, rate) for i, rate in enumerate(correct_rates)]
        self.ids.stats_graph.add_plot(plot)

    def on_leave(self):
        # 当离开屏幕时清除图表
        self.ids.stats_graph.plots = []
        self.ids.stats_layout.clear_widgets()


class NoteScreen(Screen):
    pass
class GradeSelectionScreen(Screen):
    pass


class ExerciseScreen(Screen):
    def __init__(self, **kwargs):
        super(ExerciseScreen, self).__init__(**kwargs)
        with self.canvas.before:
            # 设置背景颜色，可选
            Color(1, 1, 1, 0.3)  # RGBA，这里是白色
            # 添加背景图像，确保图像文件路径正确
            self.bg = Rectangle(source='bg.png', size=self.size, pos=self.pos)

        self.bind(size=self._update_bg, pos=self._update_bg)
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
        self.print_btn = Button(text='打印习题', on_press=self.print_question)
        # 初始时“返回”按钮不显示
        self.back_btn = Button(text="返回", opacity=0, disabled=True, size_hint_y=None, height=50,
                               on_press=self.restart)

        # 添加按钮到布局
        control_layout.add_widget(self.prev_btn)
        control_layout.add_widget(self.next_btn)
        control_layout.add_widget(self.submit_btn)
        control_layout.add_widget(self.back_btn)
        control_layout.add_widget(self.print_btn)
        main_layout.add_widget(control_layout)

        self.add_widget(main_layout)
        self.problems = []
        self.user_answers = {}
        self.populate_questions()
    def _update_bg(self, *args):
        self.bg.size = self.size
        self.bg.pos = self.pos
    def restart(self, instance):
        # 重置题目或其他状态
        # ...这里可以添加重置题目的代码或其他需要重置的状态...
        self.prev_btn.opacity = 1
        self.prev_btn.disabled = False
        self.print_btn.opacity = 1
        self.print_btn.disabled = False
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
        self.problems = app_function.generate_arithmetic_problems(grade, 8 ,1)  # 假设每个年级生成32个算式
        self.problems = self.problems[:30]
        self.page = 0  # 重置到第一页
        self.total_pages = len(self.problems) // 10  # 计算总页数
        self.user_answers = {}  # 清空之前的答案
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
    def print_question(self, instance):
        # 切换到开发中的屏幕
        self.manager.current = 'development'
    def submit_answers(self, instance):
        # 先清除之前的所有问题和答案，为显示比对结果做准备
        self.questions_layout.clear_widgets()
        count = 0
        total_questions = len(self.problems)

        # 遍历所有问题，比对答案
        for index, problem in enumerate(self.problems):
            user_answer = self.user_answers.get(index, "未作答！")
            correct_answer = problem.answer  # 假设每个problem对象有一个answer属性存储正确答案

            # 尝试将用户答案转换为与correct_answer相同的类型
            try:
                # 假设correct_answer是数字，尝试将用户答案转换为float
                user_answer_float = float(user_answer)
                if user_answer_float == correct_answer:
                    count += 1
                    answer_text = '做对啦！ : )'
                else:
                    answer_text = '做错啦！ : ('
            except ValueError:
                answer_text = ' : ('

        accuracy_text = f"你的正确率为{count / 30 * 100:.2f}%! 你答对了{count}题，答错了{30 - count}题。"
        accuracy_label = Label(text=accuracy_text, size_hint_y=None, height=80)
        self.questions_layout.add_widget(accuracy_label)
        info_label = Label(text='已经自动将错题倒入错题库！', size_hint_y=None, height=80)
        self.questions_layout.add_widget(info_label)
        for index, problem in enumerate(self.problems):
            user_answer = self.user_answers.get(index, "未作答")
            correct_answer = problem.answer  # 假设每个problem对象有一个answer属性存储正确答案

            # 尝试将用户答案转换为与correct_answer相同的类型
            try:
                # 假设correct_answer是数字，尝试将用户答案转换为float
                user_answer_float = float(user_answer)
                if user_answer_float == correct_answer:
                    count += 1
                    answer_text = '做对啦！ : )'
                else:
                    answer_text = '做错啦！ : ('
            except ValueError:
                answer_text = ' : ('

            question_text = f"{problem.num1} {problem.operator} {problem.num2} = {correct_answer} (正确答案) / 你的答案: {user_answer} {answer_text}"
            result_label = Label(text=question_text, size_hint_y=None, height=100)
            self.questions_layout.add_widget(result_label)
        # 修改按钮状态
        self.prev_btn.opacity = 0
        self.prev_btn.disabled = True
        self.next_btn.opacity = 0
        self.next_btn.disabled = True
        self.submit_btn.opacity = 0
        self.submit_btn.disabled = True
        self.back_btn.opacity = 1
        self.back_btn.disabled = False


# 创建应用
class DevelopmentScreen(Screen):
    pass

class MathQuizApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(IntroScreen(name='intro'))
        sm.add_widget(GradeSelectionScreen(name='grade_selection'))
        sm.add_widget(ExerciseScreen(name='exercise'))
        sm.add_widget(ErrorLogScreen(name='error_log'))
        sm.add_widget(StatsScreen(name='stats'))
        sm.add_widget(NoteScreen(name='note'))
        sm.add_widget(DevelopmentScreen(name='development'))
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
