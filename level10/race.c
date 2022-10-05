#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>

int		main(int ac, char **av)
{	
	if (ac != 3)
		return -1;
	while (1)
	{
		renameat2(-2, av[1], -2, av[2], RENAME_EXCHANGE);
	}
	return 0;
}

//     int     renameatx_np(int fromfd, const char *from, int tofd, const char *to, unsigned int flags);
//     RENAME_SWAP
