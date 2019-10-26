import gameFramework
import pico2d
import mainState

if __name__=='__main__':
    pico2d.open_canvas()
    gameFramework.run(mainState)
    pico2d.close_canvas()