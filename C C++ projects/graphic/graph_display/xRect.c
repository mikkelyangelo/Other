#include <X11/Xlib.h>
#include <X11/Xutil.h>
#include <stdio.h>
#include <stdlib.h>

#define REDRAWALL 1

#define DELTA 10

typedef struct {
    Window main;
    Window rect;
    Window button_right;
    Window button_left;
    Window button_up;
    Window button_down;
    Window indicate;

    int rect_width;
    int rect_height;
    int rect_x;
    int rect_y;

    int max_h;
    int max_w;

    int ind_size_w;
    int ind_size_h;
} controler;

int x_setup_screen(Display *dpy, GC *gc, const int rect_w, const int rect_h, controler *contr) {
    if (dpy == NULL || gc == NULL || contr == NULL) {
        return -1;
    }

    Window root = DefaultRootWindow(dpy);
    *gc = XCreateGC(dpy, root, 0, NULL);

    int def_scr = DefaultScreen(dpy);
    int depth = DefaultDepth(dpy, def_scr);

    contr->rect_width= rect_w;
    contr->rect_height = rect_h;

    /* Конфигурируем основное окно */
    unsigned long main_win_mask = (CWOverrideRedirect | CWBackPixel);
    XSetWindowAttributes main_attr;
    main_attr.background_pixel = WhitePixel(dpy, def_scr);
    main_attr.override_redirect = False;
    int x = 0;
    int y = 0;
    int main_h = contr->max_h = DisplayHeight(dpy, def_scr);
    int main_w = contr->max_w = DisplayWidth(dpy, def_scr);
    contr->main = XCreateWindow(dpy, root, x, y,
                                main_w, main_h, 1, depth,
                                InputOutput, CopyFromParent,
                                main_win_mask, &main_attr);
    XSizeHints main_hint;
    main_hint.min_width = main_hint.max_width = main_w;
    main_hint.min_height = main_hint.max_height = main_h;
    main_hint.x = x;
    main_hint.y = y;
    XSetNormalHints(dpy, contr->main, &main_hint);
    XStoreName(dpy, contr->main, "RK");

    /* Создаем прямоугольник */
    unsigned long rect_mask = (CWOverrideRedirect | CWBackPixel);
    XSetWindowAttributes rect_attr;
    rect_attr.override_redirect = True;
    rect_attr.background_pixel = WhitePixel(dpy, def_scr);
    contr->rect_x = 0;
    contr->rect_y = 0;
    contr->rect = XCreateWindow(dpy, contr->main, contr->rect_x, contr->rect_y,
                                rect_w, rect_h, 1, depth, InputOutput, CopyFromParent,
                                rect_mask, &rect_attr);

    /* Индикационное поле */
    unsigned long indicate_maks = (CWOverrideRedirect | CWBackPixel | CWEventMask);
    XSetWindowAttributes indicate_attr;
    indicate_attr.event_mask = (ButtonPressMask);
    indicate_attr.background_pixel = WhitePixel(dpy, def_scr);
    indicate_attr.override_redirect = False;
    int indicate_w =  contr->ind_size_w = rect_w / 4;
    int indicate_h =  contr->ind_size_h = rect_h / 4;
    int indicate_x = rect_w / 2 - indicate_w / 2;
    int indicate_y = rect_h / 2 - indicate_h / 2;
    contr->indicate = XCreateWindow(dpy, contr->rect, indicate_x, indicate_y,
                                    indicate_w, indicate_h, 1, depth, InputOutput, CopyFromParent,
                                    indicate_maks, &indicate_attr);

    unsigned long btn_mask = (CWOverrideRedirect | CWBackPixel | CWEventMask);
    XSetWindowAttributes btn_attr;
    btn_attr.override_redirect = False;
    btn_attr.background_pixel = WhitePixel(dpy, def_scr);
    btn_attr.event_mask = (KeyPressMask | ExposureMask | ButtonPressMask);

    int button_size = main_w/20;

    int btn_x = main_w-button_size*5;
    int btn_y = main_h-button_size*2;

    contr->button_left = XCreateWindow(dpy, contr->main, btn_x, btn_y,
                                       button_size, button_size, 1, depth, InputOutput, CopyFromParent,
                                       btn_mask, &btn_attr);
    btn_x += button_size;

    contr->button_right = XCreateWindow(dpy, contr->main, btn_x, btn_y,
                                        button_size, button_size, 1, depth, InputOutput, CopyFromParent,
                                        btn_mask, &btn_attr);
    btn_x += button_size;

    contr->button_up = XCreateWindow(dpy, contr->main, btn_x, btn_y,
                                     button_size, button_size, 1, depth, InputOutput, CopyFromParent,
                                    btn_mask, &btn_attr);
    btn_x += button_size;

    contr->button_down = XCreateWindow(dpy, contr->main, btn_x, btn_y,
                                       button_size, button_size, 1, depth, InputOutput, CopyFromParent,
                                     btn_mask, &btn_attr);
    btn_x += button_size;

    XMapWindow(dpy, contr->main);
    XMapSubwindows(dpy, contr->main);
    XMapSubwindows(dpy, contr->rect);
    return 0;
}

int redraw(short type, Display *dpy, GC *gc, controler *contr) {
    if (dpy == NULL || gc == NULL || contr == NULL) {
        return -1;
    }

    switch (type) {
        case REDRAWALL:
            break;
    }

    int scr = DefaultScreen(dpy);
    unsigned long black = BlackPixel(dpy, scr);
    Font f = XLoadFont(dpy, "-*-*-medium-r-normal-*-12-*-*-*-*-*-*-*");
    XClearWindow(dpy, contr->indicate);
    XSetForeground(dpy, *gc, black);
    XSetFont(dpy, *gc, f);
    char buff[40];
    int size = sprintf(buff, "%d:%d", contr->rect_x, contr->rect_y);
    int button_size = (contr->rect_height > contr->rect_width) ? contr->rect_height/10: contr->rect_width/10;
    XDrawString(dpy, contr->indicate, *gc, contr->ind_size_w/3, contr->ind_size_h/2, buff, size);
    XDrawString(dpy, contr->button_right, *gc, button_size/2, button_size/2, ">", 1);
    XDrawString(dpy, contr->button_left, *gc, button_size/2, button_size/2, "<", 1);
    XDrawString(dpy, contr->button_up, *gc, button_size/2, button_size/2, "^", 1);
    XDrawString(dpy, contr->button_down, *gc, button_size/2, button_size/2, "v", 1);
    XMapSubwindows(dpy, contr->rect);
    XUnloadFont(dpy, f);
    return 0;
}

int left_action(Display *dpy, GC *gc, controler *contr) {
    if (dpy == NULL || gc == NULL || contr == NULL) {
        return -1;
    }

    if (contr->rect_x > 0) {
        contr->rect_x -= DELTA;
    }
    XMoveResizeWindow(dpy, contr->rect, contr->rect_x, contr->rect_y, contr->rect_width, contr->rect_height);
    return 0;
}

int right_action(Display *dpy, GC *gc, controler *contr) {
    if (dpy == NULL || gc == NULL || contr == NULL) {
        return -1;
    }

    if (contr->rect_x < contr->max_w - contr->rect_width) {
        contr->rect_x += DELTA;
    }
    XMoveResizeWindow(dpy, contr->rect, contr->rect_x, contr->rect_y, contr->rect_width, contr->rect_height);
    return 0;
}

int up_action(Display *dpy, GC *gc, controler *contr) {
    if (dpy == NULL || gc == NULL || contr == NULL) {
        return -1;
    }

    if (contr->rect_y > 0) {
        contr->rect_y -= DELTA;
    }
    XMoveResizeWindow(dpy, contr->rect, contr->rect_x, contr->rect_y, contr->rect_width, contr->rect_height);
    return 0;
}

int down_action(Display *dpy, GC *gc, controler *contr) {
    if (dpy == NULL || gc == NULL || contr == NULL) {
        return -1;
    }

    if (contr->rect_y < contr->max_h - contr->rect_height) {
        contr->rect_y += DELTA;
    }
    XMoveResizeWindow(dpy, contr->rect, contr->rect_x, contr->rect_y, contr->rect_width, contr->rect_height);
    return 0;
}

int button_press_processing(Display *dpy, GC *gc, XEvent *event, controler *contr) {
    if (dpy == NULL || gc == NULL || event == NULL || contr == NULL) {
        return -1;
    }

    if (event->xbutton.window == contr->indicate) {
        return 1;
    }

    if (event->xbutton.window == contr->button_right) {
        right_action(dpy, gc, contr);
        redraw(REDRAWALL, dpy, gc, contr);
        return 0;
    }

    if (event->xbutton.window == contr->button_left) {
        left_action(dpy, gc, contr);
        redraw(REDRAWALL, dpy, gc, contr);
        return 0;
    }

    if (event->xbutton.window == contr->button_up) {
        up_action(dpy, gc, contr);
        redraw(REDRAWALL, dpy, gc, contr);
        return 0;
    }

    if (event->xbutton.window == contr->button_down) {
        down_action(dpy, gc, contr);
        redraw(REDRAWALL, dpy, gc, contr);
        return 0;
    }

    return 0;
}

int key_press_processing(Display *dpy, GC *gc, XEvent *event, controler *contr) {
    if (dpy == NULL || gc == NULL || event == NULL || contr == NULL) {
        return -1;
    }
    KeySym sym;
    sym = XKeycodeToKeysym(dpy, event->xkey.keycode, 0);
    if (sym == XK_Down) {
        down_action(dpy, gc, contr);
        redraw(REDRAWALL, dpy, gc, contr);
        return 0;
    }

    if (sym == XK_Up) {
        up_action(dpy, gc, contr);
        redraw(REDRAWALL, dpy, gc, contr);
        return 0;
    }

    if (sym == XK_Right) {
        right_action(dpy, gc, contr);
        redraw(REDRAWALL, dpy, gc, contr);
        return 0;
    }

    if (sym == XK_Left) {
        left_action(dpy, gc, contr);
        redraw(REDRAWALL, dpy, gc, contr);
        return 0;
    }
}

int dispatcher(Display *dpy, GC *gc, controler *contr) {
    if (dpy == NULL || gc == NULL || contr == NULL) {
        return -1;
    }

    XEvent event;
    int done = 0;
    while (done == 0) {
        XNextEvent(dpy, &event);
        switch (event.type) {
            case Expose:
                redraw(REDRAWALL, dpy, gc, contr);
                break;
            case KeyPress:
                done = key_press_processing(dpy, gc, &event, contr);
                break;
            case ButtonPressMask:
                done = button_press_processing(dpy, gc, &event, contr);
                break;
        }
    }

    return 0;
}

int main(int argc, char *argv[]) {
    int rect_width = 400;
    int rect_height = 300;
    if (argc >= 3) {
        rect_width = atoi(argv[1]);
        rect_height = atoi(argv[2]);
    }

    Display *dpy = XOpenDisplay(NULL);
    if (dpy == NULL) {
        return -1;
    }

    GC gc;
    controler contr;

    x_setup_screen(dpy, &gc, rect_width, rect_height, &contr);

    dispatcher(dpy, &gc, &contr);

    XDestroySubwindows(dpy, contr.rect);
    XDestroySubwindows(dpy, contr.main);
    XDestroyWindow(dpy, contr.main);
    XCloseDisplay(dpy);
Имитация процесса регулировки положения прямоугольника