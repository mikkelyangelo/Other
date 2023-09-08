#include <unistd.h>
#include <sys/types.h>
#include <stdio.h>
int main(int argc, char ** argv)
{
	if (argc < 2)
	{
		printf("Unacceptable number of arguments");
		printf("First - old_folder(input); second - new_folder(output)");
		exit(1);
	}
	int fds[2];
	pipe(fds);
	if (fork())
	{
		dup2(fds[1], 1);
		close(fds[0]);
		close(fds[1]);
		execl("/bin/tar", "tar", "cf", "-", argv[1], NULL);
	}
	else
	{
		dup2(fds[0], 0);
		close(fds[0]);
		close(fds[1]);
		execl("/bin/tar", "tar", "xfC", "-", argv[2], NULL);
	}
	return 0;
}


