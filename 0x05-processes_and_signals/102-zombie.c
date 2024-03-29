#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * infinite_while - Creates an infinite loop for the main process.
 *
 * Return: Always 0.
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Creates five processes.
 *
 * Return: Always 0.
 */
int main(void)
{
	pid_t zombie_pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		zombie_pid = fork();

		if (zombie_pid == -1)
		{
			perror("Fork failed");
			exit(EXIT_FAILURE);
		}

		if (zombie_pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}

		else
		{
			sleep(1);
		}
	}

	infinite_while();

	return (0);
}
