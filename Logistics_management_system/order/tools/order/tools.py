import time
def set_order_number():

    k = time.localtime()
    order_number = str(k[0])+str(k[1])+str(k[2])+str(k[3])+str(k[4])
    return order_number

if __name__ == '__main__':
    print(set_order_number())