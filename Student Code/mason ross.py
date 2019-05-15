import button_shim
import fourletterphat as flp
while True:
  if button_shim.button_B == True:
    flp.show()
    while button_shim.button_B == True:
      pass
    flp.set_digit( 60, 'B' )
    print('Button pressed')
  if button_shim.button_A == True:
    flp.show()
    while button_shim.button_A == True:
      pass
    flp.set_digit( 10, 'B' )
    print('Button pressed')
  if button_shim.button_B == True:
    flp.show()
    while button_shim.button_B == True:
      pass
    flp.set_digit( 10, 'B' )
    print('Button pressed')
  if button_shim.button_C == True:
    flp.show()
    while button_shim.button_C == True:
      pass
    flp.set_digit( 10, 'B' )
    print('Button pressed')
  if button_shim.button_D == True:
    flp.show()
    while button_shim.button_D == True:
      pass
    flp.set_digit( 10, 'B' )
    print('Button pressed')
  if button_shim.button_E == True:
    flp.show()
    while button_shim.button_E == True:
      pass
    flp.set_digit( 10, 'B' )
    print('Button pressed')

