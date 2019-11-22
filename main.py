import gameFramework
import pico2d
import startState
import titleState
if __name__=='__main__':
    pico2d.open_canvas()
    gameFramework.run(titleState)
    pico2d.close_canvas()