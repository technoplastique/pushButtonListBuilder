from machine import Pin
import time
from neopixel import Neopixel


spi=SPI(0,2_000_000, mosi=Pin(19),miso=Pin(16),sck=Pin(18))


nic = network.WIZNET5K(spi,Pin(17),Pin(20)) #spi,cs,reset pin
nic.ifconfig(('192.168.1.20','255.255.255.0','192.168.1.1','8.8.8.8'))
while not nic.isconnected():
    time.sleep(1)
    print(nic.regs())
 
numpix = 10
pixels = Neopixel(numpix, 0, 0, "GRB")
button1 = Pin(1, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(2, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)
button4 = Pin(4, Pin.IN, Pin.PULL_DOWN)
button5 = Pin(5, Pin.IN, Pin.PULL_DOWN)
button6 = Pin(6, Pin.IN, Pin.PULL_DOWN)
button7 = Pin(7, Pin.IN, Pin.PULL_DOWN)
button8 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button9 = Pin(9, Pin.IN, Pin.PULL_DOWN)
button0 = Pin(10, Pin.IN, Pin.PULL_DOWN)
 
yellow = (255, 100, 0)
orange = (255, 50, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
off = (0,0,0)

while True:
        conn, addr = s.accept()
        print('Connect from %s' % str(addr))
        request = conn.recv(1024)
        request = str(request)
	##1
        led1_need = request.find('/?led1=need')
        led1_off = request.find('/?led1=off')
        led1_inprocess = request.find('/?led1=inprocess')
        if led1=off == 6:
            print("LED Done")
            pixels.set_pixel(1, off)
        if led1=inprocess == 6:
            print("LED In Process")
            pixels.set_pixel(1, blue)
        if led1=need == 6:
            print("LED Need")
            pixels.set_pixel(1, red)
        if button1.value():
            print("LED Need")
            pixels.set_pixel(1, red)
            time.sleep(0.5)
	##2
        led2_need = request.find('/?led2=need')
        led2_off = request.find('/?led2=off')
        led2_inprocess = request.find('/?led2=inprocess')
        if led2=off == 6:
            print("LED Done")
            pixels.set_pixel(2, off)
        if led2=inprocess == 6:
            print("LED In Process")
            pixels.set_pixel(2, blue)
        if led2=need == 6:
            print("LED Need")
            pixels.set_pixel(2, red)
        if button2.value():
            print("LED Need")
            pixels.set_pixel(2, red)
            time.sleep(0.5)
	##3
        led3_need = request.find('/?led3=need')
        led3_off = request.find('/?led3=off')
        led3_inprocess = request.find('/?led3=inprocess')
        if led3=off == 6:
            print("LED Done")
            pixels.set_pixel(3, off)
        if led3=inprocess == 6:
            print("LED In Process")
            pixels.set_pixel(3, blue)
        if led3=need == 6:
            print("LED Need")
            pixels.set_pixel(3, red)
        if button3.value():
            print("LED Need")
            pixels.set_pixel(3, red)
            time.sleep(0.5)
	##4
        led4_need = request.find('/?led4=need')
        led4_off = request.find('/?led4=off')
        led4_inprocess = request.find('/?led4=inprocess')
        if led4=off == 6:
            print("LED Done")
            pixels.set_pixel(4, off)
        if led4=inprocess == 6:
            print("LED In Process")
            pixels.set_pixel(4, blue)
        if led4=need == 6:
            print("LED Need")
            pixels.set_pixel(4, red)
        if button4.value():
            print("LED Need")
            pixels.set_pixel(4, red)
            time.sleep(0.5)
	##5
        led5_need = request.find('/?led5=need')
        led5_off = request.find('/?led5=off')
        led5_inprocess = request.find('/?led5=inprocess')
        if led5=off == 6:
            print("LED Done")
            pixels.set_pixel(5, off)
        if led5=inprocess == 6:
            print("LED In Process")
            pixels.set_pixel(5, blue)
        if led5=need == 6:
            print("LED Need")
            pixels.set_pixel(5, red)
        if button5.value():
            print("LED Need")
            pixels.set_pixel(5, red)
            time.sleep(0.5)
	##6
        led6_need = request.find('/?led6=need')
        led6_off = request.find('/?led6=off')
        led6_inprocess = request.find('/?led6=inprocess')
        if led6=off == 6:
            print("LED Done")
            pixels.set_pixel(6, off)
        if led6=inprocess == 6:
            print("LED In Process")
            pixels.set_pixel(6, blue)
        if led6=need == 6:
            print("LED Need")
            pixels.set_pixel(6, red)
        if button6.value():
            print("LED Need")
            pixels.set_pixel(6, red)
            time.sleep(0.5)
	##7
        led7_need = request.find('/?led7=need')
        led7_off = request.find('/?led7=off')
        led7_inprocess = request.find('/?led7=inprocess')
        if led7=off == 6:
            print("LED Done")
            pixels.set_pixel(7, off)
        if led7=inprocess == 6:
            print("LED In Process")
            pixels.set_pixel(7, blue)
        if led7=need == 6:
            print("LED Need")
            pixels.set_pixel(7, red)
        if button7.value():
            print("LED Need")
            pixels.set_pixel(7, red)
            time.sleep(0.5)
	##8
        led8_need = request.find('/?led8=need')
        led8_off = request.find('/?led8=off')
        led8_inprocess = request.find('/?led8=inprocess')
        if led8=off == 6:
            print("LED Done")
            pixels.set_pixel(8, off)
        if led8=inprocess == 6:
            print("LED In Process")
            pixels.set_pixel(8, blue)
        if led8=need == 6:
            print("LED Need")
            pixels.set_pixel(8, red)
        if button8.value():
            print("LED Need")
            pixels.set_pixel(8, red)
            time.sleep(0.5)
	##9
        led9_need = request.find('/?led9=need')
        led9_off = request.find('/?led9=off')
        led9_inprocess = request.find('/?led9=inprocess')
        if led9=off == 6:
            print("LED Done")
            pixels.set_pixel(9, off)
        if led9=inprocess == 6:
            print("LED In Process")
            pixels.set_pixel(9, blue)
        if led9=need == 6:
            print("LED Need")
            pixels.set_pixel(9, red)
        if button9.value():
            print("LED Need")
            pixels.set_pixel(9, red)
            time.sleep(0.5)
	##0
        led0_need = request.find('/?led0=need')
        led0_off = request.find('/?led0=off')
        led0_inprocess = request.find('/?led0=inprocess')
        if led0=off == 6:
            print("LED Done")
            pixels.set_pixel(0, off)
        if led0=inprocess == 6:
            print("LED In Process")
            pixels.set_pixel(0, blue)
        if led0=need == 6:
            print("LED Need")
            pixels.set_pixel(0, red)
        if button0.value():
            print("LED Need")
            pixels.set_pixel(0, red)
            time.sleep(0.5)
	##
        response = web_page()
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Connection: close\n\n')
        conn.send(response)
        conn.close()
