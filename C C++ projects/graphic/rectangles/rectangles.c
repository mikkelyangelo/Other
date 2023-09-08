#include <X11/Xlib.h>
#define WIDTH 128 /* repeat element width */
#define HEIGHT 64 /* repeat element height */

int main(int argc, char* argv[]) {
Display* dpy; /* display structure */
int src; /* screen number */
GC gc; /* graphic context */
int depth; /* bit per color pixel */
Window root; /* screen root window */
Pixmap pix; /* Pixel map for ring */
Window win; /* Main window */
XSetWindowAttributes attr; /* window attributes */
unsigned long mask; /* event mask */
XEvent event; /* Event structure */
unsigned int done = 0; /* exit code */

/* X init */

dpy = XOpenDisplay(NULL);
src = DefaultScreen(dpy);
depth = DefaultDepth(dpy, src);
root = DefaultRootWindow(dpy);
gc = DefaultGC(dpy, src);

/* Pixmap block */

pix = XCreatePixmap(dpy, root, WIDTH, HEIGHT, depth);
XSetBackground(dpy, gc, WhitePixel(dpy, src));
XSetForeground(dpy, gc, WhitePixel(dpy, src));
XFillRectangle(dpy, pix, gc, 0, 0, WIDTH, HEIGHT);
XSetForeground(dpy, gc, BlackPixel(dpy, src));

XDrawLine(dpy, pix, gc, 0, 0, 0, HEIGHT);
XDrawLine(dpy, pix, gc, WIDTH * 3/4, 0, WIDTH * 3/4, HEIGHT);
XDrawLine(dpy, pix, gc, 0, HEIGHT/4, WIDTH/4, 0);
XDrawLine(dpy, pix, gc, 0, HEIGHT/4, WIDTH/4, HEIGHT/2);
XDrawLine(dpy, pix, gc, 0, HEIGHT * 3/4, WIDTH/4, HEIGHT/2);
XDrawLine(dpy, pix, gc, 0, HEIGHT * 3/4, WIDTH/4, HEIGHT);
XDrawLine(dpy, pix, gc, WIDTH/2, 0, WIDTH * 3/4, HEIGHT/4);
XDrawLine(dpy, pix, gc, WIDTH/2, HEIGHT/2, WIDTH * 3/4, HEIGHT/4);
XDrawLine(dpy, pix, gc, WIDTH/2, HEIGHT/2, WIDTH * 3/4, HEIGHT * 3/4);
XDrawLine(dpy, pix, gc, WIDTH/2, HEIGHT, WIDTH * 3/4, HEIGHT * 3/4);

XDrawRectangle(dpy, pix, gc, WIDTH/4, 0, WIDTH/4, HEIGHT/2);
XDrawRectangle(dpy, pix, gc, WIDTH/4, HEIGHT/2, WIDTH/4, HEIGHT/2);
XDrawRectangle(dpy, pix, gc, WIDTH * 3/4, HEIGHT/4, WIDTH/4, HEIGHT/2);

XDrawPoint(dpy, pix, gc, WIDTH * 3/8, HEIGHT/4);
XDrawPoint(dpy, pix, gc, WIDTH * 7/8, HEIGHT/2);
XDrawPoint(dpy, pix, gc, WIDTH/8, HEIGHT * 3/4);
XDrawPoint(dpy, pix, gc, WIDTH * 5/8, HEIGHT * 3/4);

/* Window block */

mask = (CWOverrideRedirect | CWBackPixmap);
attr.override_redirect = False;
attr.background_pixmap = pix;
win = XCreateWindow(dpy, root, 0, 0, 800, 600, 1, depth,
InputOutput, CopyFromParent, mask, &attr);
mask = (ButtonPressMask | ButtonReleaseMask |
EnterWindowMask | LeaveWindowMask |
KeyPressMask);
XSelectInput(dpy, win, mask);
XMapRaised(dpy, win);
XSetFunction(dpy, gc, GXinvert); /* XSetFunction(dpy, gc, GXcopyInverted); */

/* Dispatch block */

while(done == 0) {
XNextEvent(dpy, &event);
switch(event.type) {
case EnterNotify:
case LeaveNotify:
case ButtonPress:
case ButtonRelease: XCopyArea(dpy, pix, pix, gc, 0, 0, WIDTH, HEIGHT, 0, 0);
XSetWindowBackgroundPixmap(dpy, win, pix);
XClearWindow(dpy, win);
break;
case KeyPress: done = event.xkey.keycode;
break;
default: break;
} /* switch */
} /* while */

/* X-Exit block */

XFreePixmap(dpy, pix);
XDestroyWindow(dpy, win);
XCloseDisplay(dpy);
return(done);
