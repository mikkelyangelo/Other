#include <stdio.h> #include <stdlib.h> #include <sys/socket.h> #include <sys/types.h> #include <unistd.h> #include <netinet/in.h> #include <arpa/inet.h> #include <netdb.h> #include <string.h> #include <regex.h> #include <libgen.h> #include <fcntl.h> #include <errno.h>

#define BUF_SIZE	256

int cp(const char *to, const char *from); int delete(char * file_name);

int sock; int sock2;

void sock2init(char * buf){
sock2 = socket(AF_INET, SOCK_STREAM, 0); char* firstbracket=strchr(buf, '('); firstbracket++;
char ips[64]; memset(ips, '\0' ,64);

char * tok = strtok(firstbracket, "(),"); char dataip[16];
memset(dataip, '\0' ,16); int i=0;
for(; i<3;i++){
strcat(dataip, tok); strcat(dataip, ".");
tok = strtok(NULL, "(),");
}
strcat(dataip, tok);

unsigned int dataPort = atoi(strtok(NULL, "(),")) * 256 + atoi(strtok(NULL, "(),")); printf("Data connection on %s:%d\n", dataip, dataPort);
struct sockaddr_in addr;

if(sock2<0){
printf("Cannot create socket data socket. Errcode %d\n", sock2); exit(-1);
};

addr.sin_family = AF_INET; addr.sin_port = htons(dataPort);
 
54:
55:
56:
57:
58:
59:
60:
61:
62:
63:
64:
65:
66:
67:
68:
69:
70:
71:
72:
73:
74:
75:
76:
77:
78:
79:
80:
81:
82:
83:
84:
85:
86:
87:
88:
89:
90:
91:
92:
93:
94:
95:
96:
97:
98:
99:
100:
101:
102:
103:
104:
105:
106:
107:
108:
109:
110:
111:
112:
113:
114:
115:
116:
 

addr.sin_addr.s_addr = htonl(inet_addr(dataip));//hostIp->h_addr_list[0] struct hostent * hostIp = gethostbyname(dataip);
bcopy(*hostIp->h_addr_list, &(addr.sin_addr.s_addr), hostIp->h_length); printf("Connecting data port.\n");
int conn2 =	connect(sock2, (struct sockaddr *)&addr, sizeof(addr)); if(conn2 < 0)
{
printf("Data socket Connection failed. Errcode %d\n", conn2); exit(-1);
}
printf("Connected.\n");

}

char* recieve(char* buf){ memset(buf,'\0', 2024);
recv(sock, buf, 2000, 0); printf("%s",buf);
return buf;
}

void sender(char* cmd, char * arg){ char usercomm[1024]; memset(usercomm,'\0', 1024);
sprintf(usercomm, "%s %s\r\n", cmd, arg); printf("Sending: %s" , usercomm); send(sock, usercomm, strlen(usercomm), 0);
}

void fnSendFtpCommand (char * sCommandToSend){ char sOutput[BUF_SIZE];
send(sock, sCommandToSend, strlen(sCommandToSend), 0);//отправляем команду return;
}



int checkip(char * str){
char * token = strtok(str,"."); if(atoi(token)==0) return 0; int c=4;
do{
c--;
if(atoi(token)<0 || atoi(token)>255) return 0; token = strtok(NULL,".");
}while(token!=NULL); if(c) return 0;
return 1;
}


int main(int argc, char* argv[]){ unsigned int ftpPort = 21;

struct sockaddr_in addr;
sock = socket(AF_INET, SOCK_STREAM, 0); if(sock<0){
printf("cannot create socket. Errno %d\n", sock); exit(-1);
 
117:
118:
119:
120:
121:
122:
123:
124:
125:
126:
127:
128:
129:
130:
131:
132:
133:
134:
135:
136:
137:
138:
139:
140:
141:
142:
143:
144:
145:
146:
147:
148:
149:
150:
151:
152:
153:
154:
155:
156:
157:
158:
159:
160:
161:
162:
163:
164:
165:
166:
167:
168:
169:
170:
171:
172:
173:
174:
175:
176:
177:
178:
179:
 

};

struct hostent * hostIp = gethostbyname(argv[1]);

//printf("Test 1\n");

addr.sin_family = hostIp->h_addrtype; addr.sin_port = htons(ftpPort);

if(checkip(argv[1]))
addr.sin_addr.s_addr = htonl(inet_addr(argv[1]));//
else
addr.sin_addr.s_addr = htonl(inet_addr(hostIp->h_addr_list[0]));// bcopy(*hostIp->h_addr_list, &(addr.sin_addr.s_addr), hostIp->h_length);
//printf("Test 2\n");

if(connect(sock, (struct sockaddr *)&addr, sizeof(addr)) < 0 )
{
printf("sock fail"); exit(-1);
}

char buf[2048];

recieve(buf); if(atoi(buf)!=220){
printf("no hello\n"); exit(-1);
}

sender("USER", argv[2]); recieve(buf); if(atoi(buf)!=331){
printf("user\n"); exit(-1);
}

sender("PASS", argv[3]); recieve(buf); if(atoi(buf)!=230){
printf("no pass\n"); exit(-1);
}

sender("TYPE", "I"); recieve(buf);

if(atoi(buf)!=200){
printf("No binary mode\n"); exit(-1);
}

while(atoi(buf)!=227){
fnSendFtpCommand("PASV\r\n"); recieve(buf);
};

sock2init(buf);

char dest[256]; int len = 0;
 
180:
181:
182:
183:
184:
185:
186:
187:
188:
189:
190:
191:
192:
193:
194:
195:
196:
197:
198:
199:
200:
201:
202:
203:
204:
205:
206:
207:
208:
209:
210:
211:
212:
213:
214:
215:
216:
217:
218:
219:
220:
221:
222:
223:
224:
225:
226:
227:
228:
229:
230:
231:
232:
233:
234:
235:
236:
237:
238:
239:
240:
241:
242:
 

//int len = strlen(argv[4]);
//memcpy(dest, argv[4], len); char * base = basename(argv[4]); If(base != argv[4]){
cp(base, argv[4]);}
//printf("%s\n",base);
//memcpy(dest + 12, argv[4], strlen(argv[4]));
//printf("%s\n", dest);
//sender("STOR", dest);

//char dest[256]; memcpy(dest, "pub/htdocs/", 11); memcpy(dest+11, base, strlen(base));
//printf("%s\n", dest); sender("STOR", dest); recieve(buf);

if(atoi(buf)!=150){
printf("STOR err\n"); exit(-1);
}
FILE * fp = fopen(argv[4], "rb"); if(fp==NULL){
printf("Can't open file %s.\n", argv[4]); exit(-1);
}

int fbuf[1024];
unsigned int dcounter=0; int cread;
while(cread=fread(fbuf, 1, 1024, fp)){ dcounter+=cread;
send(sock2, fbuf, cread, 0);
}
printf("%d bytes sent.\n", dcounter);

close(sock2); recieve(buf);

if(atoi(buf)!= 226){
printf("Error while sending.\n"); exit(1);
}
close(sock); printf("Everything is Ok.\n");
If(base != argv[4]){delete(base);}
}


int cp(const char *to, const char *from)
{
int fd_to, fd_from; char buf[4096]; ssize_t nread;
int saved_errno;

fd_from = open(from, O_RDONLY); if (fd_from < 0)
return -1;

fd_to = open(to, O_WRONLY | O_CREAT | O_EXCL, 0666);
 
243:
244:
245:
246:
247:
248:
249:
250:
251:
252:
253:
254:
255:
256:
257:
258:
259:
260:
261:
262:
263:
264:
265:
266:
267:
268:
269:
270:
271:
272:
273:
274:
275:
276:
277:
278:
279:
280:
281:
282:
283:
284:
285:
286:
287:
288:
289:
290:
 

if (fd_to < 0) goto out_error;

while (nread = read(fd_from, buf, sizeof buf), nread > 0)
{
char *out_ptr = buf; ssize_t nwritten;

do {
nwritten = write(fd_to, out_ptr, nread);

if (nwritten >= 0)
{
nread -= nwritten; out_ptr += nwritten;
}
else if (errno != EINTR)
{
goto out_error;
}
} while (nread > 0);
}

if (nread == 0)
{
if (close(fd_to) < 0)
{
fd_to = -1; goto out_error;
}
close(fd_from);

/* Success! */ return 0;
}

out_error: saved_errno = errno;

close(fd_from); if (fd_to >= 0)
close(fd_to);

errno = saved_errno; return -1;
}
 
291:
292:
293:
294:
295:
296:
297:
298:
299:
300:
301:
302:
303:
 
int delete(char * file_name)
{
int status;
//char file_name[25];

//printf("Enter name of a file you wish to delete\n");


status = remove(file_name);


return 0;
}
 




