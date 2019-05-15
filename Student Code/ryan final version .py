import time
import fourletterphat as flp
import button_shim
countdown = 10

while button_shim.button_A == True:
    str_time = time.strftime("%M%S")
    flp.print_number_str(countdown)
    flp.show()
    countdown -=1
    time.sleep(0.55)
    
    if  button_shim.button_A == True and  button_shim.button_B == True and button_shim.button_C == True:
        break
    
    if button_shim.button_E == True or button_shim.button_D == True:
        flp.print_str('BOOM')
        flp.show()
        break
    
    if countdown <= 0:
        flp.print_str('BOOM')
        flp.show()
        break
    
countdown_1 = 60
while button_shim.button_B == True:
    str_time = time.strftime("%M%S")
    flp.print_number_str(countdown_1)
    flp.show()
    countdown_1 -=1
    
    time.sleep(0.55)
    
    if  button_shim.button_A == True and  button_shim.button_B == True and button_shim.button_C == True:
        break
    
    if button_shim.button_E == True or button_shim.button_D == True:
        flp.print_str('BOOM')
        flp.show()
        break
    
    if countdown_1 <= 0:
        flp.print_str('BOOM')
        flp.show()
        break
    
countdown_2 = 1800
while button_shim.button_C == True:
    str_time = time.strftime("%M%S")
    flp.print_number_str(countdown_2)
    flp.show()
    countdown_2 -=1
    time.sleep(0.55)
    
    if  button_shim.button_A == True and  button_shim.button_B == True and button_shim.button_C == True:
        break
    
    if button_shim.button_E == True or button_shim.button_D == True:
        flp.print_str('BOOM')
        flp.show()
        break
    
    if countdown_2 <= 0:
        flp.print_str('BOOM')
        flp.show()
        break
    
countdown_3 = 3600
while button_shim.button_D == True:
    str_time = time.strftime("%M%S")
    flp.print_number_str(countdown_3)
    flp.show()
    countdown_3 -= 1
    time.sleep(0.55)
    
    if  button_shim.button_A == True and  button_shim.button_B == True and button_shim.button_C == True:
        break
    
    if button_shim.button_E == True:
        flp.print_str('BOOM')
        flp.show()
        break
    
    if countdown_3 <= 0:
        flp.print_str('BOOM')
        flp.show()
        break
    
countdown_4 = 240
clock = 60
while button_shim.button_E == True:
    str_time = time.strftime("%H%M")
    flp.print_number_str(countdown_4)
    flp.show()
    clock -= 1
    
    if clock == 0:
        countdown_4 -= 1
        clock = 60
    
    if  button_shim.button_A == True and  button_shim.button_B == True and button_shim.button_C == True:
        break
    
    if button_shim.button_D == True:
        flp.print_str('BOOM')
        flp.show()
        break
    
    if countdown_4 <= 0:
        flp.print_str('BOOM')
        flp.show()
        break

        
        

   
    




