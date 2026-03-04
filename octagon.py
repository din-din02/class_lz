import matplotlib.pyplot as mp
import math
class Octagon:
    def __init__(self,storona):
        self.storona=storona
        self.corner=2*3.14/8
        self.k=1+2**(1/2)

    def opis(self):
        R=self.storona*(self.k/(self.k-1))**(1/2)
        S=3.14*R**2
        print(f"Радиус описанной окружности:{R} Площадь описанной окружности:{S}")
        

    def vpis(self):
        r=(self.k/2)*self.storona
        s=3.14*r**2
        print(f"Радиус вписанной окружности:{r} Площадь вписанной окружности:{s}")
        

    def oct(self):
        P=self.storona*8
        Area=2*self.storona**2*self.k
        print((f"Площадь октагона:{Area} Периметр октагона:{P}"))
    
    def grafik(self):
        R=self.storona*(self.k/(self.k-1))**(1/2)
        r=(self.k/2)*self.storona
        fig, ax = mp.subplots(figsize=(30, 30))  #создаём график и оси https://sky.pro/wiki/media/vyvod-grafikov-matplotlib-v-ipython-notebook/?ysclid=mm9cqmp1o2691985824
        ax.set_aspect('equal') #Установка равного соотношения сторон https://external.software/archives/23129?ysclid=mm9d3ggkuj475114572
        #создаём списки для восьми вершин
        x = [R* math.cos(i * self.corner) for i in range(10)] 
        y = [R* math.sin(i * self.corner) for i in range(10)] 
        #чтобы фигура замыкалась
        x.append(x[0])  
        y.append(y[0])
        ax.plot(x,y,color='yellow',markersize=10) #розовый октагон
        circle_out = mp.Circle((0, 0), R, color='black', fill=False, label=" График описанной окружности" ) #создаем оранжевую описанную без заливки окружность
        ax.add_patch(circle_out) #добавление на график
        circle_in = mp.Circle((0, 0), r, color='red', fill=False, label=" График вписанной окружности" ) #создаем желтую вписанную без заливки окружность
        ax.add_patch(circle_in) #добавление на график
        mp.legend() #цвета
        mp.show() #вывод графика
    def __del__(self):
        print('Сторона удалена',self.storona)    

