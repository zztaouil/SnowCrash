#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>

int	open_file(char *filename)
{
	int fd = open(filename, O_RDONLY);
	
	if (fd < 0)
		return -1;
	
	return fd;
}

int	decrypt(int c, int itr)
{
	return c - itr;
}

void	read_file(int fd)
{	
	unsigned char buff = 0;
	int read_return = read(fd, &buff, 1);
	int itr = 0;

	while (read_return > 0)
	{
		printf("%c", decrypt(buff, itr));
		read_return = read(fd, &buff, 1);
		itr++;
	}
	printf("%c", decrypt(buff, itr));
	return ;
}


int	main(int ac, char **av)
{
	int fd;

	if (ac != 2){
		printf("Enter one argument");
		return 1;
	}
	fd = open_file(av[1]);

	read_file(fd);
	
	close(fd);
	return 0;
}
