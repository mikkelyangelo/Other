#define DELAY (1  14)

#define SIZE_CHANGE (-1)
#define LEFT (1)
#define RIGHT (3)
#define TOP (0)
#define BOTTOM (2)

#define WIDTH 640
#define HEIGHT 480

#define ROTATE_RIGHT 24
#define ROTATE_LEFT 25

#define PROGRAM_FINISH 255
#define WRONG_KEY_PRESSED 254



структура стрелы
typedef struct {
    double A[3];           угол поворота стрелки
    int R[3];
    double dA;          приращения угла поворота стрелки
    XPoint c;           центр стрелки
    int R_okr;
} XArrow;

 Spiral Implementation function 

int configure_arrow(XArrow, int, int);               задание точек стрелки 
int reconfigure(XArrow , int , int, int );              изменение параметров треугольника
int reverse(XArrow, int );                              изменение стороны поворота стрелки
int redraw(XEvent, GC, XArrow);               перерисовка потерянных фрагментов окна 
int amod2pi(XArrow);                  изменение координат углов поворота, проверка на выход их из диапазона возможных значений 
int draw_arrow(Display , Window ,GC ,XArrow );       отрисовка стрелы в окне
int key_check(XEvent );       ответ на собития нажатия клавиш 
 2 centred spiral implementation 

#include X11Xlib.h
#include X11keysym.h
#include X11keysymdef.h
#include spiral.h
#include math.h

#define MIN(a,b) (((a)(b))(b)(a))

 задание точек стрелки 
int configure_arrow(XArrow pr, int w, int h) {
    pr-A[0] = M_PI  2;
    pr-A[1] = pr-A[0] + 3  M_PI  4;
    pr-A[2] = pr-A[0] - 3  M_PI  4;
    for (int i = 0; i  3; i++) {
        if (pr-A[i] = 2  M_PI)
            pr-A[i] -= 2  M_PI;
        if (pr-A[i] = 0)
            pr-A[i] += 2  M_PI;
    }



    int min = MIN(w, h);
    pr-R_okr = min  35;

    pr-R[0] = min  2;
    pr-R[2] = pr- R[1] = min  23;

    pr-c.x = w  2;
    pr-c.y = h  2;

    pr-dA = M_PI  360;
    return 0;
}


изменение параметров треугольника
int reconfigure(XArrow pr, int w, int h, int reconf){
    int min;
    switch(reconf){
        case SIZE_CHANGE
            min = MIN(w, h);
            pr-R_okr = min  35;

            pr-R[0] = min  2;
            pr-R[2] = pr- R[1] = min  23;

            pr-c.x = w  2;
            pr-c.y = h  2;
            break;
        case LEFT
        case RIGHT
        case TOP
        case BOTTOM
            pr-A[0] = M_PI  2 + (reconf  M_PI  2);
            pr-A[1] = pr-A[0] + 3  M_PI  4;
            pr-A[2] = pr-A[0] - 3  M_PI  4;
            for (int i = 0; i  3; i++) {
                if (pr-A[i] = 2  M_PI)
                    pr-A[i] -= 2  M_PI;
                if (pr-A[i] = 0)
                    pr-A[i] += 2  M_PI;
            }
            break;
        default
            return 1;
    }
    return 0;
}
Spiral1.c

отрисовка стрелы в окне
int draw_arrow(Display dpy, Window win, GC gc ,XArrow pr){
    XClearWindow(dpy, win);

    XDrawArc(dpy, win, gc, pr-c.x - pr-R_okr, pr-c.y - pr-R_okr, pr-R_okr  2, pr-R_okr  2, 0  64, 360   64);
    int x1, y1, x2, y2;         координаты стрелки

    for (int i = 0; i  3; i++){
        x1 = pr-c.x + pr-R[i]  cos(pr-A[i]);
        x2 = pr-c.x + pr-R[(i + 1) % 3]  cos(pr-A[(i + 1) % 3]);
        y1 = pr-c.y - pr-R[i]  sin(pr-A[i]);
        y2 = pr-c.y - pr-R[(i + 1) % 3]  sin(pr-A[(i + 1) % 3]);

        XDrawLine(dpy, win, gc, x1, y1, x2, y2);
    }

    XFlush(dpy);
    return 0;
}


 перерисовка потерянных фрагментов окна 
int redraw(XEvent ev, GC gc, XArrow pr) {
    if((ev-xexpose.count  0))
        return(0);

    draw_arrow(ev-xexpose.display, ev-xexpose.window, gc, pr);

    return 0;
}  redraw 


изменение стороны поворота стрелки
int reverse(XArrow pr, int where) {
    pr-dA = where  M_PI  360;
    return 0;
}  reverse 



 изменение координат углов поворота, проверка на выход их из диапазона возможных значений 
int amod2pi(XArrow pr) {
    for (int i = 0; i  3; i++) {
        pr-A[i] += pr-dA;
        if (pr-A[i] = 0) {
            pr-A[i] = M_PI  2;
        } else if (pr-A[i] = M_PI  2) {
            pr-A[i] = 0;
        }
    }
    return 0;
}  amod2pi 



 ответ на собития нажатия клавиш 
int key_check(XEvent ev) {
    KeySym ks = XLookupKeysym((XKeyEvent) ev, 1);
    if((ks == XK_A) && (ev-xkey.state == ControlMask))
        return PROGRAM_FINISH;  код выхода
    switch(ks){
        case XK_plus return ROTATE_RIGHT;
        case XK_underscore return ROTATE_LEFT;
        case XK_Up return TOP;
        case XK_Right return RIGHT;
        case XK_Down return BOTTOM;
        case XK_Left return LEFT;
        default  break;
    }
    return WRONG_KEY_PRESSED;
}  rapid 
