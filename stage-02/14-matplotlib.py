import matplotlib.pyplot as plt
import numpy as np
print('---------------简单的使用----------------')
# x = np.linspace(-1,1,50)
# y = 2*x+1
# plt.plot(x,y)
# plt.show()

print('---------------figure的使用----------------')
# #其实就是生成几张图的意思
# x = np.linspace(-1,1,50)
# y1 = 2*x+1
# y2 = x**2
#
# #以figure开头,说明是一组
# plt.figure()
# plt.plot(x,y1)
#
# #另外一组
# plt.figure(num=3,figsize=(8,5))
# plt.plot(x,y2)
# plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')
# plt.show()

print('---------------设置坐标轴1----------------')
# #调整名字和间隔

# x = np.linspace(-1,1,50)
# y1 = 2*x+1
# y2 = x**2
#
# plt.figure(num=3,figsize=(8,5))
# plt.plot(x,y2)
# plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')
#
# plt.xlim((-1,2)) #x轴的取值范围
# plt.ylim((-2,3)) #y轴的取值范围
# plt.xlabel("i am x")
# plt.ylabel("i am y")
#
# new_ticks = np.linspace(-1,2,5) #个数是5
# print(new_ticks)
# plt.xticks(new_ticks)  #x指标具体对应的信息
# plt.yticks([-2,-1.8,-1,1.22,3],[r'$realy\ bad$',r'$bad\ \alpha$',r'$normal$',r'$good$',r'$really\ good$']) #$是为了让显示好看点 \ 是为了能够读取空格  r表示是正则的形式  \alpha 显示阿尔法
#
# plt.show()

print('---------------设置坐标轴2----------------')
# #调整坐标轴
#
# x = np.linspace(-1,1,50)
# y1 = 2*x+1
# y2 = x**2
#
# plt.figure(num=3,figsize=(8,5))
# plt.plot(x,y2)
# plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')
#
# plt.xlim((-1,2)) #x轴的取值范围
# plt.ylim((-2,3)) #y轴的取值范围
# plt.xlabel("i am x")
# plt.ylabel("i am y")
#
# new_ticks = np.linspace(-1,2,5) #个数是5
# print(new_ticks)
# plt.xticks(new_ticks)  #x指标具体对应的信息
# plt.yticks([-2,-1.8,-1,1.22,3],[r'$realy\ bad$',r'$bad\ \alpha$',r'$normal$',r'$good$',r'$really\ good$']) #$是为了让显示好看点 \ 是为了能够读取空格  r表示是正则的形式  \alpha 显示阿尔法
#
# ax = plt.gca()
# ax.spines['right'].set_color('none') #右边的边框消失
# ax.spines['top'].set_color('none') #上边的边框消失
# ax.xaxis.set_ticks_position('bottom')
# ax.yaxis.set_ticks_position("left")
# ax.spines['bottom'].set_position(('data',-1))
# ax.spines['left'].set_position(('data',0))
#
# plt.show()

print('---------------legend图例----------------')
#添加图例
#调整位置和名称

# x = np.linspace(-1,1,50)
# y1 = 2*x+1
# y2 = x**2
#
# plt.figure(num=3,figsize=(8,5))
#
# plt.xlim((-1,2)) #x轴的取值范围
# plt.ylim((-2,3)) #y轴的取值范围
# plt.xlabel("i am x")
# plt.ylabel("i am y")
#
# new_ticks = np.linspace(-1,2,5) #个数是5
# print(new_ticks)
# plt.xticks(new_ticks)  #x指标具体对应的信息
# plt.yticks([-2,-1.8,-1,1.22,3],[r'$realy\ bad$',r'$bad\ \alpha$',r'$normal$',r'$good$',r'$really\ good$'])
#
# l1, = plt.plot(x,y2,label='up')
# l2, = plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--',label='down')
# plt.legend(handles=[l1,l2],labels=['aaa','bbb'],loc='best') #如果想加入到handles里面,l1和l2必须加逗号
#
# plt.show()

print('---------------Anntation标注----------------')
# x = np.linspace(-3, 3, 50)
# y = 2*x + 1
#
# plt.figure(num=1, figsize=(8, 5),)
# plt.plot(x, y,)
#
# ax = plt.gca()
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')
# ax.spines['bottom'].set_position(('data', 0))
# ax.yaxis.set_ticks_position('left')
# ax.spines['left'].set_position(('data', 0))
#
# x0 = 1
# y0 = 2*x0 + 1
# plt.plot([x0, x0], [0, y0], 'k--', linewidth=2.5)  #[x0, x0], [0, y0]根据两点 确定一条直线   k-- k表示黑色
# plt.scatter([x0, ], [y0, ], s=50, color='b')  #scatter是点  s是size  大小
#
# #添加标注
# # method 1:
# #####################
# """
# $2x+1=%s$' % y0  拼接数据
# xy=(x0, y0) 添加的点
# xycoords='data'  添加的这个点是基于data的
# xytext=(+30, -30) 根据textcoords='offset points'  加减30 显示文字
# arrowprops=dict(arrowstyle='->'箭头
# connectionstyle="arc3,rad=.2" 什么样弧度和角度
#
# """
# plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30),
#              textcoords='offset points', fontsize=16,
#              arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))
#
# # method 2:
# ########################
# """
# -3.7, 3  x坐标和y坐标
# """
# plt.text(-3.7, 3, r'$This\ is\ the\ some\ text. \mu\ \sigma_i\ \alpha_t$',
#          fontdict={'size': 16, 'color': 'r'})
# plt.show()


print('---------------tick能见度----------------')
# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.linspace(-3, 3, 50)
# y = 0.1*x
#
# plt.figure()
# plt.plot(x, y, linewidth=10, zorder=1)
# plt.ylim(-2, 2)
# ax = plt.gca()
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')
# ax.spines['bottom'].set_position(('data', 0))
# ax.yaxis.set_ticks_position('left')
# ax.spines['left'].set_position(('data', 0))
#
#
# for label in ax.get_xticklabels() + ax.get_yticklabels():
#     label.set_fontsize(12)
#     # set zorder for ordering the plot in plt 2.0.2 or higher
#     label.set_bbox(dict(facecolor='white', edgecolor='none', alpha=0.8, zorder=2))
# plt.show()

print('---------------scatter散点图----------------')
# import matplotlib.pyplot as plt
# import numpy as np
#
# n = 1024    # data size
# #确定x,y的位置
# X = np.random.normal(0, 1, n)
# Y = np.random.normal(0, 1, n)
# #随机生成颜色
# T = np.arctan2(Y, X)
#
# plt.scatter(X, Y, s=75, c=T, alpha=.5)
#
# plt.xlim(-1.5, 1.5)
# plt.xticks(())  # ignore xticks
# plt.ylim(-1.5, 1.5)
# plt.yticks(())  # ignore yticks
#
# plt.show()

print('---------------bar条形图----------------')
n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

for x, y in zip(X, Y1):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')

for x, y in zip(X, Y2):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x + 0.4, -y - 0.05, '%.2f' % y, ha='center', va='top')

plt.xlim(-.5, n)
plt.xticks(())
plt.ylim(-1.25, 1.25)
plt.yticks(())

plt.show()

# print('---------------contours等高线图----------------')
# def f(x,y):
#     # the height function
#     return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)  #一个计算高度的值
#
# n = 256
# x = np.linspace(-3, 3, n)
# y = np.linspace(-3, 3, n)
# X,Y = np.meshgrid(x, y)
#
# # use plt.contourf to filling contours
# # X, Y and value for (X,Y) point
# plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap=plt.cm.hot)  #contourf就是等高线  8是分成10部分 因为0 默认是2部分
#
# # use plt.contour to add contour lines
# C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5) #开始画线
# # adding label
# plt.clabel(C, inline=True, fontsize=10)
#
# plt.xticks(())
# plt.yticks(())
# plt.show()
#
# print('---------------image图片----------------')
# # image data
# a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
#               0.365348418405, 0.439599930621, 0.525083754405,
#               0.423733120134, 0.525083754405, 0.651536351379]).reshape(3,3)
#
# """
# for the value of "interpolation", check this:
# http://matplotlib.org/examples/images_contours_and_fields/interpolation_methods.html
# for the value of "origin"= ['upper', 'lower'], check this:
# http://matplotlib.org/examples/pylab_examples/image_origin.html
# """
# plt.imshow(a, interpolation='nearest', cmap='bone', origin='lower')
# plt.colorbar(shrink=.92)
#
# plt.xticks(())
# plt.yticks(())
# plt.show()
#
# print('---------------3d数据----------------')
# fig = plt.figure()
# ax = Axes3D(fig)
# # X, Y value
# X = np.arange(-4, 4, 0.25)
# Y = np.arange(-4, 4, 0.25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X ** 2 + Y ** 2)
# # height value
# Z = np.sin(R)
#
# ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
# """
# ============= ================================================
#         Argument      Description
#         ============= ================================================
#         *X*, *Y*, *Z* Data values as 2D arrays
#         *rstride*     Array row stride (step size), defaults to 10
#         *cstride*     Array column stride (step size), defaults to 10
#         *color*       Color of the surface patches
#         *cmap*        A colormap for the surface patches.
#         *facecolors*  Face colors for the individual patches
#         *norm*        An instance of Normalize to map values to colors
#         *vmin*        Minimum value to map
#         *vmax*        Maximum value to map
#         *shade*       Whether to shade the facecolors
#         ============= ================================================
# """
#
# # I think this is different from plt12_contours
# ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.get_cmap('rainbow'))
# """
# ==========  ================================================
#         Argument    Description
#         ==========  ================================================
#         *X*, *Y*,   Data values as numpy.arrays
#         *Z*
#         *zdir*      The direction to use: x, y or z (default)
#         *offset*    If specified plot a projection of the filled contour
#                     on this position in plane normal to zdir
#         ==========  ================================================
# """
#
# ax.set_zlim(-2, 2)
#
# plt.show()
#
#
# print('---------------subplot多合一显示----------------')
# # example 1:
# ###############################
# plt.figure(figsize=(6, 4))
# # plt.subplot(n_rows, n_cols, plot_num)
# plt.subplot(2, 2, 1)
# plt.plot([0, 1], [0, 1])
#
# plt.subplot(222)
# plt.plot([0, 1], [0, 2])
#
# plt.subplot(223)
# plt.plot([0, 1], [0, 3])
#
# plt.subplot(224)
# plt.plot([0, 1], [0, 4])
#
# plt.tight_layout()
#
# # example 2:
# ###############################
# plt.figure(figsize=(6, 4))
# # plt.subplot(n_rows, n_cols, plot_num)
# plt.subplot(2, 1, 1)
# # figure splits into 2 rows, 1 col, plot to the 1st sub-fig
# plt.plot([0, 1], [0, 1])
#
# plt.subplot(234)
# # figure splits into 2 rows, 3 col, plot to the 4th sub-fig
# plt.plot([0, 1], [0, 2])
#
# plt.subplot(235)
# # figure splits into 2 rows, 3 col, plot to the 5th sub-fig
# plt.plot([0, 1], [0, 3])
#
# plt.subplot(236)
# # figure splits into 2 rows, 3 col, plot to the 6th sub-fig
# plt.plot([0, 1], [0, 4])
#
#
# plt.tight_layout()
# plt.show()
#
# print('---------------分格显示----------------')
# # method 1: subplot2grid
# ##########################
# plt.figure()
# ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)  # stands for axes
# ax1.plot([1, 2], [1, 2])
# ax1.set_title('ax1_title')
# ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
# ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
# ax4 = plt.subplot2grid((3, 3), (2, 0))
# ax4.scatter([1, 2], [2, 2])
# ax4.set_xlabel('ax4_x')
# ax4.set_ylabel('ax4_y')
# ax5 = plt.subplot2grid((3, 3), (2, 1))
#
# # method 2: gridspec
# #########################
# plt.figure()
# gs = gridspec.GridSpec(3, 3)
# # use index from 0
# ax6 = plt.subplot(gs[0, :])
# ax7 = plt.subplot(gs[1, :2])
# ax8 = plt.subplot(gs[1:, 2])
# ax9 = plt.subplot(gs[-1, 0])
# ax10 = plt.subplot(gs[-1, -2])
#
# # method 3: easy to define structure
# ####################################
# f, ((ax11, ax12), (ax13, ax14)) = plt.subplots(2, 2, sharex=True, sharey=True)
# ax11.scatter([1,2], [1,2])
#
# plt.tight_layout()
# plt.show()
# print('---------------图中图----------------')
# fig = plt.figure()
# x = [1, 2, 3, 4, 5, 6, 7]
# y = [1, 3, 4, 2, 5, 8, 6]
#
# # below are all percentage
# left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
# ax1 = fig.add_axes([left, bottom, width, height])  # main axes
# ax1.plot(x, y, 'r')
# ax1.set_xlabel('x')
# ax1.set_ylabel('y')
# ax1.set_title('title')
#
# ax2 = fig.add_axes([0.2, 0.6, 0.25, 0.25])  # inside axes
# ax2.plot(y, x, 'b')
# ax2.set_xlabel('x')
# ax2.set_ylabel('y')
# ax2.set_title('title inside 1')
#
#
# # different method to add axes
# ####################################
# plt.axes([0.6, 0.2, 0.25, 0.25])
# plt.plot(y[::-1], x, 'g')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('title inside 2')
#
# plt.show()
# print('---------------次坐标轴----------------')
# x = np.arange(0, 10, 0.1)
# y1 = 0.05 * x**2
# y2 = -1 *y1
#
# fig, ax1 = plt.subplots()
#
# ax2 = ax1.twinx()    # mirror the ax1
# ax1.plot(x, y1, 'g-')
# ax2.plot(x, y2, 'b-')
#
# ax1.set_xlabel('X data')
# ax1.set_ylabel('Y1 data', color='g')
# ax2.set_ylabel('Y2 data', color='b')
#
# plt.show()
# print('---------------Animmation动画----------------')
# import numpy as np
# from matplotlib import pyplot as plt
# from matplotlib import animation
#
# fig, ax = plt.subplots()
#
# x = np.arange(0, 2*np.pi, 0.01)
# line, = ax.plot(x, np.sin(x))
#
#
# def animate(i):
#     line.set_ydata(np.sin(x + i/10.0))  # update the data
#     return line,
#
#
# # Init only required for blitting to give a clean slate.
# def init():
#     line.set_ydata(np.sin(x))
#     return line,
#
# # call the animator.  blit=True means only re-draw the parts that have changed.
# # blit=True dose not work on Mac, set blit=False
# # interval= update frequency
# ani = animation.FuncAnimation(fig=fig, func=animate, frames=100, init_func=init,
#                               interval=20, blit=False)
#
# # save the animation as an mp4.  This requires ffmpeg or mencoder to be
# # installed.  The extra_args ensure that the x264 codec is used, so that
# # the video can be embedded in html5.  You may need to adjust this for
# # your system: for more information, see
# # http://matplotlib.sourceforge.net/api/animation_api.html
# # anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
#
# plt.show()
