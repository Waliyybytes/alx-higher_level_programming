#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - check the code for palindrome
 * @head: list to check
 * Return: Always 0.
 */


int is_palindrome(listint_t **head)
{
	int i = 0, j;
	listint_t *current;
	int *arr;
	int len;

	if (*head == NULL)
		return (1);

	current = *head;
	while (current->next != NULL)
	{
		current = current->next;
		i++;
	}
	len = i + 1;
	arr = malloc(sizeof(int) * len);
	current = *head;

	j = 0;
	while (current->next != NULL)
	{
		arr[j] = current->n;
		current = current->next;
		j++;
	}
	arr[j] = current->n;

	for (i = 0; i < (int)len / 2; i++)
	{
		if (arr[i] != arr[len - 1 - i])
			return (0);
		continue;
	}

	free(arr);
	return (1);
}
