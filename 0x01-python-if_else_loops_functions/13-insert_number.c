#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - if a singly list is a cycle
 * @head: list to insert in
 * @number: number to insert
 * Return: new list
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *temp;

	temp = malloc(sizeof(listint_t));
	if (temp == NULL)
		return (NULL);
	current = *head;
	while (current != NULL)
	{
		if (number > current->n && number < current->next->n)
		{
			temp->n = number;
			temp->next = current->next;
			current->next = temp;
			break;
		}
		else
			current = current->next;
	}
	return (current);
}
