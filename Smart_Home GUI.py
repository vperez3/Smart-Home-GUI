import sys
import colorsys
import lifxlan
sys.path.append("../")
from appJar import gui
from time import sleep
from lifxlan import BLUE, COLD_WHITE, CYAN, GOLD, GREEN, LifxLAN, \
    ORANGE, PINK, PURPLE, RED, WARM_WHITE, WHITE, YELLOW
from colour import Color


lifxlan = LifxLAN()


def btnPress(btnName):
    if btnName == "ON":
        lifxlan.set_power_all_lights("on", rapid=True)
    elif btnName == "OFF":
        lifxlan.set_power_all_lights("off", rapid=True)
    elif btnName == "Red":
        lifxlan.set_color_all_lights(RED)
    elif btnName == "Orange":
        lifxlan.set_color_all_lights(ORANGE)
    elif btnName == "Yellow":
        lifxlan.set_color_all_lights(YELLOW)
    elif btnName == "Green":
        lifxlan.set_color_all_lights(GREEN)
    elif btnName == "Cyan":
        lifxlan.set_color_all_lights(CYAN)
    elif btnName == "Blue":
        lifxlan.set_color_all_lights(BLUE)
    elif btnName == "Purple":
        lifxlan.set_color_all_lights(PURPLE)
    elif btnName == "Pink":
        lifxlan.set_color_all_lights(PINK)
    elif btnName == "White":
        lifxlan.set_color_all_lights(WHITE)
    elif btnName == "Gold":
        lifxlan.set_color_all_lights(GOLD)
        


def scene_one():
    num_lights = None
    if len(sys.argv) != 2:
        print()
    else:
        num_lights = int(sys.argv[1])

    lifx = LifxLAN(num_lights)
    original_colors = lifx.get_color_all_lights()
    original_powers = lifx.get_power_all_lights()
    lifx.set_power_all_lights(True)
    sleep(1)
    water(lifx, 5, smooth=True)

    #print("Restoring original color to all lights...")
    for light in original_colors:
        light.set_color(original_colors[light])

    sleep(1)

    #print("Restoring original power to all lights...")
    for light in original_powers:
        light.set_power(original_powers[light])

def water(lan, duration_secs=3, smooth=False):
    colors = [WARM_WHITE, WHITE, CYAN, BLUE, BLUE, CYAN, WHITE, WARM_WHITE]
    transition_time_ms = duration_secs*1000 if smooth else 0
    rapid = True if duration_secs < 1 else False
    for color in colors:
        lan.set_color_all_lights(color, transition_time_ms, rapid)
        sleep(duration_secs)

def scene_two():
    num_lights = None
    if len(sys.argv) != 2:
        print()
    else:
        num_lights = int(sys.argv[1])

    lifx = LifxLAN(num_lights)
    original_colors = lifx.get_color_all_lights()
    original_powers = lifx.get_power_all_lights()
    lifx.set_power_all_lights(True)
    sleep(1)
    earth(lifx, 5, smooth=True)

    #print("Restoring original color to all lights...")
    for light in original_colors:
        light.set_color(original_colors[light])

    sleep(1)

    #print("Restoring original power to all lights...")
    for light in original_powers:
        light.set_power(original_powers[light])

def earth(lan, duration_secs=3, smooth=False):
    colors = [WARM_WHITE, GOLD, YELLOW, GREEN, YELLOW, GREEN]
    transition_time_ms = duration_secs*1000 if smooth else 0
    rapid = True if duration_secs < 1 else False
    for color in colors:
        lan.set_color_all_lights(color, transition_time_ms, rapid)
        sleep(duration_secs)

def scene_three():
    num_lights = None
    if len(sys.argv) != 2:
        print()
    else:
        num_lights = int(sys.argv[1])

    lifx = LifxLAN(num_lights)
    original_colors = lifx.get_color_all_lights()
    original_powers = lifx.get_power_all_lights()
    lifx.set_power_all_lights(True)
    sleep(1)
    fire(lifx, 5, smooth=True)

    #print("Restoring original color to all lights...")
    for light in original_colors:
        light.set_color(original_colors[light])

    sleep(1)

    #print("Restoring original power to all lights...")
    for light in original_powers:
        light.set_power(original_powers[light])

def fire(lan, duration_secs=3, smooth=False):
    colors = [WARM_WHITE, ORANGE, RED, PINK, RED, ORANGE]
    transition_time_ms = duration_secs*1000 if smooth else 0
    rapid = True if duration_secs < 1 else False
    for color in colors:
        lan.set_color_all_lights(color, transition_time_ms, rapid)
        sleep(duration_secs)

#GUI settings
with gui("RGB Colours", bg='#404040', font=14, guiPadding='5,5') as app:
    app.setSize(370, 405)
    app.setStretch("none")

    # frame the contains ON/OFF buttons
    with app.labelFrame("On/Off", padding='5,5', sticky="EW"):
        app.buttons(["ON", "OFF"], btnPress)

    # frame that contains color buttons    
    with app.labelFrame("Colors", padding='5,5', sticky='EW'):
        app.buttons(["Red", "Orange", "Yellow", "Green", "Cyan"], btnPress)
        app.buttons(["Blue", "Purple", "Pink", "White", "Gold"], btnPress)

# frame that contains scenes buttons
    with app.labelFrame("Scenes", padding='5,5', sticky='EW'):
        app.addButton("Water", scene_one)
        app.addButton("Earth", scene_two)
        app.addButton("Fire", scene_three)
        
    
