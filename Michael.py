import math

def vm (m_vm = 2.2 , g=9.8, d_vm_x=None, d_vm_y=None):
    if d_vm_x is not None and d_vm_y is None:
        torque = m_vm * g * d_vm_x
        #print(f"torque={torque:.2f} (N.M)")
        return torque

    if d_vm_y is not None:
        for t in range(41):
            if t <= 20 :
                theta = 1.5 * t
            else:
                theta = 60 - 1.5 * t

            theta_rad = math.radians(theta)
            D = math.cos(theta_rad) * d_vm_y
            torque = m_vm * g * D
            (print(f"t={t}، theta={theta} درجه ===> torque={torque:.3f} (N.M)"))

def ta (m_ta = 0.6 , g=9.8, d_ta_x=None, d_ta_y=None):
    if d_ta_x is not None and d_ta_y is None:
        torque = m_ta * g * d_ta_x
        #print(f"torque={torque:.2f} (N.M)")
        return torque

    if d_ta_y is not None:
        for t in range(41):
            if t <= 20 :
                theta = 1.5 * t
            else:
                theta = 60 - 1.5 * t

            theta_rad = math.radians(theta)
            D = math.cos(theta_rad) * d_ta_y
            torque = m_ta * g * D
            print(f"t={t}، theta={theta} درجه ===> torque={torque:.3f} (N.M)")



def Detoid (m_Detoid = 0.8 ,g = 9.8  , d_Detoid_x = None , d_Detoid_y = None):

    if d_Detoid_x is not None and d_Detoid_y is None :
        return m_Detoid * g * d_Detoid_x
    else: return m_Detoid * g * d_Detoid_y


def biceps(m_bi=1, g=9.8, d_bi_x=None, d_bi_y=None, direction="left" or "right"):
    if d_bi_x is not None and d_bi_y is None:
        torque = m_bi * g * d_bi_x
        return torque

    if d_bi_y is not None:
        decrement = 0.04
        for t in range(41):
            if direction == "left":
                if t <= 10:
                    d_bi_y = 0.4 - t * decrement
                elif 11 <= t <= 20:
                    d_bi_y = (t - 10) * decrement
                else:  # t = 21 to t = 40
                    d_bi_y = 0.4
            elif direction == "right":
                if t <= 20:
                    d_bi_y = 0.4
                elif 21 <= t <= 30:
                    d_bi_y = 0.4 - (t - 20) * decrement
                else:  # t = 31 to t = 40
                    d_bi_y = (t - 30) * decrement

            torque = m_bi * g * d_bi_y
            print(f"t={t}، d_bi_y={d_bi_y:.2f} ===> torque={torque:.3f} (N.M)")


def head(m = 4.6 , g = 9.8,  d= 0.2):
    return m * g * d


tvlx = vm( d_vm_x=0.09)

print("گشتاور عضله ران چپ در محور x برابر {:.3f} (N.M) است.".format(tvlx))

print("############################################################")

print("گشتاور عضله ران چپ در محور y :")

tvly = vm(d_vm_y=0.53)

print("############################################################")

tvrx = vm( d_vm_x=0.09)

print("گشتاور عضله ران راست در محور x برابر {:.3f} (N.M) است.".format(tvrx))

print("############################################################")

print("گشتاور عضله ران چپ در محور y :")

tvry = vm(d_vm_y=0.53)

print("############################################################")

ttlx = ta(d_ta_x=0.09)

print(("گشتاور عضله ساق چپ در محور x برابر {:.3f} (N.M) است.".format(ttlx)))

print("############################################################")

print("گشتاور عضله ساق چپ در محور y :")

ttly = ta( d_ta_y=0.83)

print("############################################################")

ttrx = ta( d_ta_x=0.09)

print(("گشتاور عضله ساق راست در محور x برابر {:.3f} (N.M) است.".format(ttrx)))

print("############################################################")

print("گشتاور عضله ساق راست در محور y :")

ttry = ta( d_ta_y=0.83)

print("############################################################")

tdlx = Detoid(d_Detoid_x=0.42)

print(("گشتاور عضله سرشانه چپ در محور x برابر {:.3f} (N.M) است.".format(tdlx)))

print("############################################################")

tdly = Detoid(d_Detoid_y=0.2)

print(("گشتاور عضله سرشانه چپ در محور y برابر {:.3f} (N.M) است.".format(tdly)))

print("############################################################")

tdrx = Detoid(d_Detoid_x=0.42)

print(("گشتاور عضله سرشانه راست در محور x برابر {:.3f} (N.M) است.".format(tdrx)))

print("############################################################")

tdry = Detoid(d_Detoid_y=0.2)

print(("گشتاور عضله سرشانه راست در محور y برابر {:.3f} (N.M) است.".format(tdry)))

print("############################################################")

tblx = biceps(d_bi_x=0.45)

print(("گشتاور عضله بازو چپ در محور x برابر {:.3f} (N.M) است.".format(tblx)))

print("############################################################")

print("گشتاور عضله بازو چپ در محور  y")

tbly = biceps(d_bi_y=0.4 , direction= "left")

print("############################################################")

tbrx = biceps(d_bi_x=0.45)

print(("گشتاور عضله بازو راست در محور x برابر {:.3f} (N.M) است.".format(tbrx)))

print("############################################################")

print(("گشتاور عضله بازو راست در محور y : "))

tbry = biceps(d_bi_y=0.4 , direction= "right")

print("############################################################")

Head = head()

print(("گشتاور عضله سر برابر {:.3f} (N.M) است.".format(Head)))

print("############################################################")


