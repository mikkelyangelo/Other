#include <X11/Xlib.h>
#include <X11/Xutil.h>
#include <stdio.h>
#include "spiral.h"

/* Main function */

int main() {
    Display* dpy;              /* Graphic Display */
    Window win;                /* programm main window */
    GC gc;                  /* Black & White Graphic Context */
    int scr;                   /* screen number = 0 */
    XArrow r;                  /* spiral structure */

    { /* Display Block */
        unsigned long tone;       /* Light drawing tone */
        dpy = XOpenDisplay(NULL);
        scr = DefaultScreen(dpy);
        win = DefaultRootWindow(dpy);
        scr = DefaultScreen(dpy);
        gc = XCreateGC(dpy, win, 0, 0);
        tone = 0xFFFFFF;  /* = 0xFFFFFF; */
        XSetForeground(dpy, gc, tone);      //цвет переднего фона
        tone = 0x000000;  /* = 0xFFFFFF; */
        XSetBackground(dpy, gc, tone);      //цвет заднего фона

    } /* Display block */

    { /* Window block  */
        unsigned w = WIDTH, h = HEIGHT;             /* main window width & height */
        XSetWindowAttributes attr; /* window attributes structure */
        XGCValues gval;            /* GC structure */
        unsigned long amask;       /* window attributes mask */
        Window root=win;            /* Display root window */
        XSizeHints hint;           /* Geometry WM hints */

        configure_arrow(&r, w, h);

        /*создание окна*/
        amask = (CWOverrideRedirect | CWBackPixel);
        XGetGCValues(dpy, gc, GCBackground, &gval);
        attr.background_pixel = gval.background; /* = 0x0 */
        attr.override_redirect = False;
        win = XCreateWindow(dpy, root, 0, 0, w, h, 1, CopyFromParent,
                            InputOutput, CopyFromParent, amask, &attr);

        /*задание фиксированного размера окна*/
        hint.flags = (PMinSize);
        hint.min_width = w;
        hint.min_height = h;
        XSetNormalHints(dpy, win, &hint);
        XStoreName(dpy, win, "spiral");
        XMapWindow(dpy, win);

    } /* window block */

    { /* Multi Block */

        unsigned long emask;       /* window event mask */
        XEvent event;              /* graphic event structure */
        int freeze = -1;              /* window visibility stop state */
        unsigned delay= DELAY;      /* multi delay period = 2^rate */
        int multi = 1;         /* multi code */
        int count = 0;               /* delay count */
        int w = WIDTH, h = HEIGHT;
        int reconf;

        emask = ( KeyPressMask | KeyReleaseMask | ExposureMask | StructureNotifyMask);
        XSelectInput(dpy, win, emask);

        while(multi != PROGRAM_FINISH) { /* Async dispatch event with multic ground */
            event.type = 0;
            XCheckWindowEvent(dpy, win, emask,  &event);
            if (event.type == ConfigureNotify){
                w =  event.xconfigure.width;
                h =  event.xconfigure.height;
                reconf = 1;
            }
            else {
                if (reconf == 1)
                    reconfigure(&r, w, h, SIZE_CHANGE);      //изменение размеров окна
                reconf = 0;

                switch (event.type) {
                    case Expose:
                        redraw(&event, gc, &r);
                        break;
                    case KeyPress:
                        multi = key_check(&event);
                        switch (multi){
                            case ROTATE_RIGHT:             //нажата клавиша +
                                reverse(&r, -1);
                                freeze = 1;         //включение отрисовки
                                break;
                            case ROTATE_LEFT:             //нажата клавиша -
                                reverse(&r, 1);
                                freeze = 1;         //включение отрисовки
                                break;
                            case LEFT:             //нажата клавиша влево вправо ввехр или вниз
                            case RIGHT:
                            case TOP:
                            case BOTTOM:
                                reconfigure(&r, w, h, multi);
                                draw_arrow(dpy, win, gc, &r);
                                break;
                            default: break;
                        }
                        break;
                    case KeyRelease:
                        multi = key_check(&event);
                        switch (multi) {
                            case ROTATE_RIGHT:         //отпущена клавиша - или +
                            case ROTATE_LEFT:
                                freeze = -1;        //заморозка отрисовки
                                break;
                            default:
                                break;
                        }
                        break;
                    default:
                        break;
                } /* switck */
            }


            if((freeze < 0))     /* Freeze display spiral */
                continue;
            if(count++ < delay)                 /* Delay display spiral */
                continue;
            count = 0;                    /* reset count to next delay */
            draw_arrow(dpy, win, gc, &r);         //отрисовка треугольника
            amod2pi(&r);            //запланированное увеличение угла
        } /* while event */
    } /* multi block */

    { /* Exit block */
        XDestroyWindow(dpy, win);
        XCloseDisplay(dpy);
        return(0);
    } /* exit block */

}