import gameFramework
import pico2d
import startState

if __name__=='__main__':
    pico2d.open_canvas()
    gameFramework.run(startState)
    pico2d.close_canvas()