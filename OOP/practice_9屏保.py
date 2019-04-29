'''
    tkinter 项目实战 - 屏保
    项目分析：
        屏保可以自己启动，也可以手动启动
        一旦敲击键盘或着移动鼠标后，或者其他的引发事件，则停止
        如果屏保是一幅画，则没有画框
        图形的动作是随机的，具有随机性，可能包括颜色、大小、运动方向，变形等
        整个世界的构成是：
            - ScreenSaver
                - 需要一个canvas,大小与屏幕一致，没有边框

            - Ball
                - 颜色、大小、多少、运动方向，变形与随机
                - 球能动，可以被调用
'''
import  random
import  tkinter


class RandomBall():
    '''
    定义运动的球的类
    '''
    def __init__(self, canvas, scrnwidth, scrnheight):
        '''
        :param canvas:画布，所有的内容都应该在画布上呈现出来，此处通过此变量传入
        :param scrnwidth: 屏幕的宽
        :param scrnheight: 屏幕的高
        '''
        # 球出现的初始位置要随机，此处位置表示的圆心
        # xpos表示位置的x坐标
        self.canvas = canvas
        self.xpos = random.randint(60, int(scrnwidth) - 60)
        # ypos表示位置的y坐标
        self.ypos = random.randint(60, int(scrnheight) - 60)
        # while True:
        #     if self.xpos != 0 and self.ypos!= 0:
        #         break
        #     else:
        #         self.xpos = random.randint(10, int(scrnwidth) - 20)
        #         self.ypos = random.randint(10, int(scrnheight) - 20)
        # # 定义球运动的速度
        # 模拟运动，不断擦掉原来的话，然后在一个新的地方再重新绘制
        # 此处xvelocity模拟x周方向运动
        self.xvelocity = random.randint(6, 12)
        # 同理yvelocity模拟x周方向运动
        self.yvelocity = random.randint(6, 12)
        # 定义屏幕的大小
        self.scrnwidth = scrnwidth
        # 定义屏幕的高度
        self.scrnheight = scrnheight
        # 球的大小随机
        # 此处球的大小用半径使用
        self.radius = random.randint(40, 70)
        # 定义颜色
        # RGB表示法：三个数字，每个数字的值是0-255之间，表示红绿蓝三个颜色的大小
        # 在某些系统中，之间用英文单词表示也可以，比如red,green,
        # 此处用lambda表达式
        c = lambda: random.randint(0, 255)
        self.color = '#%02x%02x%02x'%(c(), c(), c())
    def creat_ball(self):
        '''
        用构造函数定义的变量值，在canvas上画一个球
        '''
        # tkinter没有画圆形函数
        # 只有一个画椭圆函数，画椭圆要先定义两个坐标
        # 在一个长方形内画椭圆，我们只需要定义长方形左上角和右下角就好
        # 求两个坐标的方法是：已知圆心的坐标，则圆心的坐标减去半径能求出左上角坐标
        #                     圆心的坐标加上半径就能求出右下角的坐标
        x1 = self.xpos - self.radius
        y1 = self.ypos - self.radius
        x2 = self.xpos + self.radius
        y2 = self.ypos + self.radius
        # 在有两个对角坐标的前提下，可以进行画圆
        # fill表示填充颜色
        #outline是外围边框颜色
        self.item = self.canvas.create_oval(x1, y1, x2, y2, fill = self.color, outline = self.color)

    def move_ball(self):
        # 移动球的时候，需要控制移动球的方向
        # 每次移动后，球都有一个新的坐标
        self.xpos += self.xvelocity
        self.ypos += self.yvelocity
        # 以下判断是否撞墙，撞了南墙就得回头
        # 注意撞墙的算法判断
        if self.xpos + self.radius >= self.scrnwidth:
            # 撞到了右边墙
            self.xvelocity = -self.xvelocity
        if self.xpos - self.radius <= 0:
            self.xvelocity = -self.xvelocity
        if self.ypos + self.radius >= self.scrnheight:
            self.yvelocity = -self.yvelocity
        if self.ypos - self.radius <= 0:
            self.yvelocity = -self.yvelocity
        # 在画布上挪动画图
        self.canvas.move(self.item, self.xvelocity, self.yvelocity)



class ScreenSaver():
    '''
    定义屏保的类
    可以被启动
    '''
    def __init__(self):
        self.balls = list()
        # 每次启动球的数量随机
        self.num_balls = random.randint(6, 20)

        self.root = tkinter.Tk()
        # 获取屏幕尺寸，作为主窗口尺寸
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        # 取消边框
        self.root.overrideredirect(1)
        # 调整背景透明度
        self.root.attributes('-alpha', 1)
        # 任何鼠标移动都需要取消
        self.root.bind('<Motion>', self.myquit)
        # 按动任何键盘都需要推出屏保
        self.root.bind('<Key>',self.myquit)
        self.root.bind('<Any-Button>', self.myquit)
        self.canvas = tkinter.Canvas(self.root, width=self.width, height=self.height, ba='black')
        self.canvas.pack()
        # 在画布上画球
        for i in range(self.num_balls):
            ball = RandomBall(self.canvas, scrnwidth=self.width, scrnheight=self.height)
            ball.creat_ball()
            self.balls.append(ball)
        self.run_screen_saver()
        self.root.mainloop()

    def run_screen_saver(self):
        for ball in self.balls:
            ball.move_ball()

        # after是200毫秒后自动启动一个函数，需要启动的函数是第二各参数
        self.canvas.after(50, self.run_screen_saver)
    def myquit(self, event):
        # 此处只是利用了事件处理机制
        # 实际上并不关心事件
        self.root.destroy()


if __name__ == "__main__":
    # 启动屏保
    ScreenSaver()

